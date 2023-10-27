from fastapi.templating import Jinja2Templates
from fastapi import FastAPI

from app.api import home, sample


app = FastAPI()


templates = Jinja2Templates(directory="templates")


app.include_router(home.router)
app.include_router(sample.router)
