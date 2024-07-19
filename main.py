from user.router import router as router_user
from fastapi import FastAPI


app = FastAPI()
app.include_router(router_user)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")