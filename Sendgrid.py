import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("shauryaguliani@gmail.com")
to_email = To("shauryaguliani@gmail.com")
subject = "Hello Friend"
content = Content("text/plain", "Hello friend, My name is Shaurya.")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)