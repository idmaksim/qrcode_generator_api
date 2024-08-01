"""
qrcode schemas
"""

from pydantic import BaseModel


class QrCodeInfo(BaseModel):
    data: str
    fill: str = 'black'
    back_color: str = 'white'
    box_size: int = 10
    border: int = 4

