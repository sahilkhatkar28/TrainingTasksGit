from pydantic import BaseModel

class FileResponse(BaseModel):
    filename: str
    filetype: str
    filesize: int

    class Config:
        orm_mode = True
