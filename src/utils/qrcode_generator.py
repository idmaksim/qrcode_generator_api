from io import BytesIO
import qrcode
from qrcode.main import QRCode
from schemas.qrcode_info import QRCodeInfo


class QRCodeGenerator:
    @staticmethod
    async def generate(qr_info: QRCodeInfo):
        qr = QRCode(
            version=1,
            error_correction=qrcode.ERROR_CORRECT_L,
            box_size=qr_info.box_size,
            border=qr_info.border,
        )

        qr.add_data(qr_info.data)

        return qr.make_image(fill=qr_info.fill, back_color=qr_info.back_color)


class BytesArrayGenerator:
    @staticmethod
    async def to_bytes(img):
        img_byte_arr = BytesIO()
        img.save(img_byte_arr)
        img_byte_arr.seek(0)
        return img_byte_arr