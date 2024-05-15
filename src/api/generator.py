from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse

from utils.error_handler import handle_route_error

from schemas.qrcode_info import QRCodeInfo
from services.generator import Generator    


router = APIRouter(
    prefix='/qrcode',
    tags=['QRCode']
)


@router.post('/generate')
async def generate_qr(qr_info: QRCodeInfo, request: Request):
    try:

        new_qr_code = await Generator.create(qr_info)
        return StreamingResponse(commt
            new_qr_code, media_type='image/png'
        )
    except Exception as e:
        await handle_route_error(e, status.HTTP_500_INTERNAL_SERVER_ERROR)
