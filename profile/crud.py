from sqlalchemy.ext.asyncio import AsyncSession

from user.models import User

from .models import Profile
from .schemas import Profile as schemasP


class ProfileCrud:
    def __init__(
        self,
        session: AsyncSession,
        user: User,
    ):
        self.session = session
        self.user = user

    async def get_by_profile_relationship(
        self,
    ) -> list[Profile] | None:
        return await self.user.awaitable_attrs.profile

    async def get_by_profile(
        self,
    ) -> Profile | None:
        self.profile = await self.session.get(Profile, self.user.id)
        return self.profile

    async def create_or_update(
        self,
        name: str,
        photo: str,
    ) -> Profile:
        if self.profile is None:
            self.profile = Profile(
                user_id=self.user.id,
                name=name,
                photo=photo,
            )
            self.session.add(self.profile)
        else:
            self.profile.photo = photo
            self.profile.name = name
        await self.session.commit()
        await self.session.refresh(self.profile)
        return self.profile

    # async def update(self, access_token: AP, update_dict: Dict[str, Any]) -> AP:
    #     for key, value in update_dict.items():
    #         setattr(access_token, key, value)
    #     self.session.add(access_token)
    #     await self.session.commit()
    #     await self.session.refresh(access_token)
    #     return access_token

    # async def delete(self, access_token: AP) -> None:
    #     await self.session.delete(access_token)
    #     await self.session.commit()
