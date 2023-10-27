from fastapi import APIRouter, status
from fastapi import APIRouter, status
from fastapi import status, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="", tags=["home"])
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def main(request: Request) -> HTMLResponse:
    """every project needs a home, and home sweet home

    Args:
        request (Request): http/https request

    Returns:
        HTMLResponse: html file as returning data
    """
    return templates.TemplateResponse("project_template/home.html", context={"request": request}, status_code=status.HTTP_200_OK)


@router.get("/teapot", response_class=HTMLResponse)
async def teapot(request: Request) -> HTMLResponse:
    """old joke from ieee students, it's just hilarious

    Args:
        request (Request): http/https request

    Returns:
        HTMLResponse: html file as returning data
    """
    return templates.TemplateResponse("project_template/teapot.html", context={"request": request}, status_code=status.HTTP_418_IM_A_TEAPOT)
