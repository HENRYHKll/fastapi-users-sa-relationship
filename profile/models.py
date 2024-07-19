from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class Profile(Base):
    __tablename__ = "profile"
    user_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey("user.id"),
        nullable=False,
        primary_key=True,
    )
    name: Mapped[str | None]
    photo: Mapped[str | None]
    users = relationship("User", back_populates="profile")
