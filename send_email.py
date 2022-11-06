import smtplib

import os
import mimetypes
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

# --- <Send Text> -----------------------------------------
def send_plain_text(auth, server, mail, isdegub=False, encode='utf-8'):
	charset = f"Content-Type: text/plain; charset={encode}"
	mime = 'MIME-Version: 1.0'
	body = "\r\n".join((f"From: {auth['login']}", f"To: {mail['to_addr']}", f"Subject: {mail['subject']}", mime, charset, "", mail['text']))

	try:
		smtp = smtplib.SMTP_SSL(host=server['server'], port=server['port'])
		if isdegub:
			smtp.set_debuglevel(1)
		else:
			smtp.set_debuglevel(0)

		smtp.ehlo()

		smtp.login(auth['login'], auth['password'])
		smtp.auth_plain()
		smtp.sendmail(auth['login'], mail['to_addr'], body.encode(encode))
		smtp.quit()
		print("DONE: Text have been sent")
	except smtplib.SMTPException as e:
		print("Что-то пошло не так")
		raise e
		exit(1)

# --- </Send Text> -----------------------------------------

# --- <Send Plain Text and File> ---------------------------

def attach_file(msg, filepath):
	filename = os.path.basename(filepath)
	ctype, encoding = mimetypes.guess_type(filepath)
	if ctype is None or encoding is not None:
		ctype = 'application/octet-stream'
	maintype, subtype = ctype.split('/', 1)
	if maintype == 'text':
		with open(filepath) as fp:
			file = MIMEText(fp.read(), _subtype=subtype)
			fp.close()
	elif maintype == 'image':
		with open(filepath, 'rb') as fp:
			file = MIMEImage(fp.read(), _subtype=subtype)
			fp.close()
	elif maintype == 'audio':
		with open(filepath, 'rb') as fp:
			file = MIMEAudio(fp.read(), _subtype=subtype)
			fp.close()

	else:
		with open(filepath, 'rb') as fp:
			file = MIMEBase(maintype, subtype)
			file.set_payload(fp.read())
			fp.close()
			encoders.encode_base64(file)
	file.add_header('Content-Disposition', 'attachment', filename=filename)
	msg.attach(file)


def process_attachement(msg, files):
	for f in files:
		if os.path.isfile(f):
			attach_file(msg, f)
		elif os.path.exists(f):
			dir = os.listdir(f)
			for file in dir:
				attach_file(msg, f+"/"+file)


def send_plain_text_and_file(auth, server, mail, path_files):
	msg = MIMEMultipart()
	msg['From'] = auth['login']
	msg['To'] = mail['to_addr']
	msg['Subject'] = mail['subject']

	body = mail['text']
	msg.attach(MIMEText(body, 'plaint'))

	process_attachement(msg, path_files)

	smtp = smtplib.SMTP_SSL(server['server'], server['port'])

	smtp.login(auth['login'], auth['password'])
	smtp.send_message(msg)
	smtp.quit()
	print("DONE: Text and File have been sent ")

# --- </Send Plain Text and File> ---------------------------


if __name__ == '__main__':
	print("This is the file of the plug-in library (module). \nShould not be used as the main")