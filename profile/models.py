from sqlalchemy import Column, ForeignKey, Integer, String, UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column

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
    user = relationship(
        "User",
        # back_populates="profile",
        uselist=False,
        backref="profile",
    )
