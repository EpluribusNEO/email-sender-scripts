from config_loader import get_config
from send_email import send_flat_text

if __name__ == '__main__':
	mail = dict(to_addr='', subject='', text='')
	auth, server = get_config()
	print(auth)

	print("Enter the subject, text, and recipient address")
	mail['subject'] = input("Subject :>")
	mail['text'] = input("Text :>")
	mail['to_addr'] = input("Address to:>")

	send_flat_text(auth, server, mail)

