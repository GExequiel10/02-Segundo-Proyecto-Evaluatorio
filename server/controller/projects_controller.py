from typing import List

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ProjectsService

class ProjectsController:
    def __init__(self):
        self.service = ProjectsService()

    def create(self, new_project: NewProjectRequest) -> ProjectResponse:
        try:
            return self.service.create(new_project)
        except BaseHTTPException as ex:
            # TODO logging
            raise ex
        except Exception:
            # Todo logg: error en Projects.create'
            raise InternalServerError()

    # No definimos valores por defecto de limit y offset porque ya esta validado por la ruta
    def get_list(self, limit: int, offset: int) -> List[ProjectResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            # TODO logging
            raise ex
        except Exception:
            # Todo logg: error en Projects.create'
            raise InternalServerError()

    def get_by_id(self, id: int) -> ProjectResponse:
        try:
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            # TODO logging
            raise ex
        except Exception:
            # Todo logg: error en Projects.create'
            raise InternalServerError()

    def update(self, id: int, new_data: ProjectRequest) -> ProjectResponse:
        try:
            return self.service.update(id)
        except BaseHTTPException as ex:
            # TODO logging
            raise ex
        except Exception:
            # Todo logg: error en Projects.create'
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            return self.service.delete(id)
        except BaseHTTPException as ex:
            # TODO logging
            raise ex
        except Exception:
            # Todo logg: error en Projects.create'
            raise InternalServerError()
