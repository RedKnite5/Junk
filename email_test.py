import smtplib
from email.message import EmailMessage
#  python email_test.py


def send_email(content, to="mr.awesome10000@gmail.com", subject="email program"):
	msg = EmailMessage()
	msg.set_content(content)

	msg["Subject"] = subject
	msg["From"] = "mr.awesome10000@gmail.com"
	msg["To"] = to

	s = smtplib.SMTP("mail.rattlebrain.com")
	s.send_message(msg)
	s.quit()

for i in range(10**3):
	send_email("DOS", to="asbw.inc@gmail.com", subject="LOL")
	print("sent")