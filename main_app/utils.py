from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
  template = get_template(template_src)
  html  = template.render(context_dict)
  result = BytesIO()
  pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
  if not pdf.err:
    return HttpResponse(result.getvalue(), content_type='application/pdf')
  return None

def generate_pdf():
  # data = {
  #   'today': datetime.date.today(), 
  #   'amount': 39.99,
  #   'customer_name': 'Cooper Mann',
  #   'order_id': 1233434,
  # }
  # pdf = render_to_pdf('email/invoice_email.html', data)
  # return HttpResponse(pdf, content_type='application/pdf')

  template = get_template('email/invoice.html')
  context = {
      "invoice_id": 123,
      "customer_name": "John Cooper",
      "amount": 1399.99,
      "today": "Today",
    }
  # html = template.render()
  pdf = render_to_pdf('email/invoice.html', context)
  if pdf:
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Invoice_.pdf"
    content = "attachment; filename='Invoice_.pdf'"
    response['Content-Disposition'] = content
    print('this is printed in generate_pdf', response)
    return response
