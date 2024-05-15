from schemas.qrcode_info import QRCodeInfo
from utils.qrcode_generator import BytesArrayGenerator, QRCodeGenerator


class Generator:
    @staticmethod
    async def create(qr_info: QRCodeInfo):
        return await BytesArrayGenerator.to_bytes(await QRCodeGenerator.generate(qr_info))