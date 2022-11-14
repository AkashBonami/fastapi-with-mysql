from pydantic import BaseModel

class User(BaseModel):
    id : int
    name :str
    lname : str
    salary : int