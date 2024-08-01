"""
qrcode app service
"""
import qrcode
from io import BytesIO
from qrcode.main import QRCode
from qrcode.image.pil import PilImage

from src.qrcode.schemas import QrCodeInfo
from src.exceptions import InternalServerErrorException


class BytesArrayGenerator:
    async def to_bytes(self, img: PilImage):
        img_byte_arr = BytesIO()
        img.save(img_byte_arr)
        img_byte_arr.seek(0)
        return img_byte_arr


class QrCodeService:
    def __init__(self, bytes_array_generator: BytesArrayGenerator):
        self.bytes_array_generator = bytes_array_generator
    
    async def generate(self, qr_info: QrCodeInfo):
        try:
            qr = QRCode(
                version=1,
                error_correction=qrcode.ERROR_CORRECT_L,
                box_size=qr_info.box_size,
                border=qr_info.border,
            )
            qr.add_data(qr_info.data)
            qr.make(fit=True)
            image = qr.make_image(fill_color=qr_info.fill, back_color=qr_info.back_color)
            image_bytes = await self.bytes_array_generator.to_bytes(image)
            return image_bytes
        except Exception as e:
            raise InternalServerErrorException(detail=str(e))
    
