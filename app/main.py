from fastapi import FastAPI, Response
from .schemas import ChequeRequest
from .pdf_utils import render_cheque_pdf

app = FastAPI()

@app.post("/cheque")
async def generate_cheque(req: ChequeRequest):
    pdf_bytes = render_cheque_pdf(req.dict())
    return Response(content=pdf_bytes, media_type="application/pdf")
