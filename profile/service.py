from fastapi import Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from .crud import ProfileCrud
from .schemas import Profile as schemasP
from user.models import User
from user.service import current_active_user


async def profile_manager(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
) -> ProfileCrud:
    profile =  ProfileCrud(
        session=session,
        user=user,
    )
    await profile.get_by_profile()
    return profile
    

def profile_depends_query(
        profile: schemasP = Depends(schemasP.as_form),
        # paswword = Form(...),
):
    print(profile)
    return profile
    
