from pydantic import BaseModel
from datetime import date

class ChequeRequest(BaseModel):
    emitter: str
    payee: str
    amount: float
    date: date
    cheque_number: str
