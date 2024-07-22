from fastapi import Form
from pydantic import BaseModel


class Profile(BaseModel):
    name: str | None = None
    photo: str | None = None

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        photo: str = Form(...),
    ):
        return cls(name=name, photo=photo)
