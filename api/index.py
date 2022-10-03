from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get('/')
def index():
    return RedirectResponse('/docs')
