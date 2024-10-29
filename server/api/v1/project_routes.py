from fastapi import APIRouter

router = APIRouter(prefix='/projects')

@router.get('') #seria: /projects/
async def get_all():
    return []
