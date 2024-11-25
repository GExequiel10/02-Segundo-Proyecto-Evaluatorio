import logging
import json
import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

request_logger = logging.getLogger('request_logger')


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    SENSITIVE_FIELDS = ['password']
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        method = request.method
        url = str(request.url.path)
        client_ip = request.client.host
        query_params = request.query_params
        body_param = await request.body()
        body_param = self.__hide_sensitive_fields(body_param)
        
        start_time = time.time()
        
        response = await call_next(request)
        
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        
        info_data = (f'{client_ip} - "{method} {url} {query_params}" {response.status_code}'
                     f' in {elapsed_time_ms:.2f} ms'
                     )
        if body_param:
            info_data += f'\nBODY: {str(body_param)}'
        request_logger.info(info_data)
        
        return response
    
    
    def __hide_sensitive_fields(self, body: bytes) -> str:
        if not body: return ''

        try:
            body_json = json.loads(body)
            for field in self.SENSITIVE_FIELDS:
                if field in body_json:
                    body_json[field] = '***********'
            return json.dumps(body_json)
        except json.JSONDecodeError:
            body.decode('utf-8')