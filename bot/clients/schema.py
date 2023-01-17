from pydantic import BaseModel


class User(BaseModel):
    uid: int


class Generation(BaseModel):
    uid: int
    prompt: str
