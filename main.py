from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables

from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("The database has been cleared")
    await create_tables()
    print("The database is launched")
    yield
    print("Turn off")



app = FastAPI(lifespan=lifespan)
app.include_router(task_router)


