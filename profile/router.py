from fastapi import APIRouter, Depends

from user.models import User
from user.service import current_active_user

from .crud import ProfileCrud
from .models import Profile
from .schemas import Profile as schemasP
from .service import profile_manager, profile_depends_query

router = APIRouter()


@router.get("/profile")
async def profile_get(user: User = Depends(current_active_user)):
    if user is None:
        print(None)
    profile: Profile = await user.awaitable_attrs.profile
    print(profile)


@router.post("/profile-1")
async def profile_post(
    data: schemasP = Depends(profile_depends_query),
    profile_crud: ProfileCrud = Depends(profile_manager),
):
    print(await profile_crud.create_or_update(name=data.name, photo=data.photo))
