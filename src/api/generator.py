from fastapi import APIRouter, Body
from fastapi.responses import StreamingResponse

from schemas.qrcode_info import QRCodeInfo
from services.generator import Generator    


router = APIRouter(
    prefix='/qrcode',
    tags=['QRCode']
)


@router.post('/generate')
async def generate_qr(qr_info: QRCodeInfo):
    return StreamingResponse(
        await Generator.create(qr_info), media_type='image/png'
    )