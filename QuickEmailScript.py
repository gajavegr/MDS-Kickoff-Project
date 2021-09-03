import ssl,smtplib

port = 465
sender_email = "c7z062022@gmail.com"
password = "Sarerem@22"
receiver_email = ["gajavegr@rose-hulman.edu","hartle@rose-hulman.edu","davignwh@rose-hulman.edu","hallmr@rose-hulman.edu"]
message = """\
Subject: Trying Out Python Writing Emails


Hello team K4! This is Ganesh."""
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", port,context=context)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()