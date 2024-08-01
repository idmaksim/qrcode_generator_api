"""
FastAPI dependencies for the app qrcode
"""

from src.qrcode.service import BytesArrayGenerator, QrCodeService 


def get_qrcode_service():
    return QrCodeService(BytesArrayGenerator())