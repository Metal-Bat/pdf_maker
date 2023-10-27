from pydantic import BaseModel


class Ticket(BaseModel):
    first_name: str
    last_name: str
    gender: str = "Male"
    date: str = "2077-09-21"
