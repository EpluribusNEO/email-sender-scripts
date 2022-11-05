import smtplib

def send_flat_text(auth, server, mail, isdegub=False, encode='utf-8'):
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
		print("DONE")
	except smtplib.SMTPException as e:
		print("Что-то пошло не так")
		raise e
		exit(1)
	finally:
		smtp.quit()