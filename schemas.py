from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class postBase(BaseModel):
    #model_config = ConfigDict(from_attributes=True)
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class postCreate(postBase):
    pass

class postResponse(postBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int = Field()
    date_posted: datetime = Field()