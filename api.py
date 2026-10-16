from fastapi import FastAPI

from todo import todo_router

app = FastAPI(
    title="FastAPI: Todo",
)

@app.get("/", tags=["Главная"])
async def welcome() -> dict:
    return {
        "message": "Hello World!"
    }

app.include_router(todo_router)