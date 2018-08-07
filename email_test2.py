import smtplib
from email.message import EmailMessage
#  python email_test2.py


def send_email(content, to="mr.awesome10000@gmail.com", subject="email program"):
	msg = EmailMessage()
	msg.set_content(content)

	msg["Subject"] = subject
	msg["From"] = "mfriedman52@sccs-stu.net"
	msg["To"] = to

	s = smtplib.SMTP("mail.rattlebrain.com")
	s.send_message(msg)
	s.quit()

for i in range(10**3):
	send_email("Hey Aja", to="asbw.inc@gmail.com", subject="Hello")
	print("sent")