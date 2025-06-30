import os
import sys
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.main import generate_cheque
from app.schemas import ChequeRequest


def test_generate_cheque_pdf():
    payload = ChequeRequest(
        emitter="ACME Corp",
        payee="John Doe",
        amount=123.45,
        date="2023-01-01",
        cheque_number="000123",
    )
    response = asyncio.run(generate_cheque(payload))
    assert response.status_code == 200
    assert response.media_type == "application/pdf"
    assert len(response.body) > 0
