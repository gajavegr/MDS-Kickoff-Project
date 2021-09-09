import ssl,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
sender_email = "c7z062022@gmail.com"
password = "Sarerem@22"
receiver_email = ["gajavegr@rose-hulman.edu","hartle@rose-hulman.edu","davignwh@rose-hulman.edu","hallmr@rose-hulman.edu"]
message = MIMEMultipart('This is test mail')
message['Subject'] = 'Test mail'
message['From'] = "c7z062022@gmail.com"
message['To'] = "gajavegr@rose-hulman.edu"
text = """\

Hello, new email format with an actual subject."""
part1 = MIMEText(text, "plain")
message.attach(part1)

context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", port,context=context)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()