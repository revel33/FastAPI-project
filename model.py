from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form("")):
        return cls(item=item)

    model_config = {
        "json_schema_extra": {"examples": [{"id": 1, "item": "Example schema!"}]}
    }

class TodoItem(BaseModel):
    item: str

class TodoItems(BaseModel):
    todos: List[TodoItem]