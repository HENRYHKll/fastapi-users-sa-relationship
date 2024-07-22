from user.router import router as router_user
from profile.router import router as router_profile
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_user)
app.include_router(router_profile)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", log_level="info", reload=True)