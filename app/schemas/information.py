# python
from datetime import datetime

# fastapi
from pydantic import BaseModel, Field
from typing import Optional

class InformationRequest(BaseModel):
    field_one: int
    field_two: str
