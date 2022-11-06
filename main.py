from config_loader import get_config
from send_email import send_plain_text
from send_email import send_plain_text_and_file as send_file

if __name__ == '__main__':
	mail = dict(to_addr='', subject='', text='')
	auth, server = get_config()

	print("1 - Отправить простой текст.\n2 - Отправить текст + файл\n<aky key> - Выход")
	action = input("action:> ")
	if action == '1':
		print("Enter the subject, text, and recipient address")
		mail['subject'] = input("Subject :>")
		mail['text'] = input("Text :>")
		mail['to_addr'] = input("Address to:>").split(';')
		send_plain_text(auth, server, mail)
	elif action == '2':
		print("Enter the subject, text, path to file and recipient address")
		mail['subject'] = input("Subject :>")
		mail['text'] = input("Text :>")
		path_arr = input("File path :>").split(';')
		mail['to_addr'] = input("Address to:>")
		send_file(auth, server, mail, path_arr)
	else:
		exit(0)



