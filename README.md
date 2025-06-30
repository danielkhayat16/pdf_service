# PDF Service

This FastAPI service generates PDF files for digital cheques. It renders a Jinja2 HTML template and converts it to PDF using WeasyPrint.

## Running the server

```bash
uvicorn app.main:app --reload
```

## Generating a cheque

Send a POST request to `/cheque` with JSON body:

```json
{
  "emitter": "ACME Corp",
  "payee": "John Doe",
  "amount": 100.50,
  "date": "2023-01-01",
  "cheque_number": "000123"
}
```

The service returns the generated PDF document.
