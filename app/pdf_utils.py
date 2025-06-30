from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

def render_cheque_pdf(data: dict) -> bytes:
    template = env.get_template("cheque.html")
    html_content = template.render(**data)
    pdf_bytes = HTML(string=html_content).write_pdf()
    return pdf_bytes
