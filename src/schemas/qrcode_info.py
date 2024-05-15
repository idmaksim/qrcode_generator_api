from pydantic import BaseModel


class QRCodeInfo(BaseModel):
    data: str
    fill: str = 'green'
    back_color: str = 'white'
    box_size: int = 10
    border: int = 4