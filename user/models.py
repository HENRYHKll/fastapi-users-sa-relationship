from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID
from sqlalchemy.orm import relationship

from models import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    Profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
    )


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass
