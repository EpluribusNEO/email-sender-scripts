import os
from os import path
from configparser import ConfigParser

def get_config():
	"""
	Загружает данные из config.ini:
	Авторизационные данные
	Данные для подключения к почтовому серверу
	:return: Кортеж: два Хеша - {login, passwd}, {server, port}
	"""

	auth = dict(login='', password='')
	server = dict(server='', port=0)

	base_path = os.path.dirname(os.path.abspath(__file__))
	config_path = os.path.join(base_path, 'config.ini')

	# провнрка наличия файла
	if os.path.exists(config_path):
		cfg = ConfigParser()
		cfg.read(config_path)
		# извлечение переменных из конфигурации
		try:
			server['server'] = cfg.get("smtp", "server")
			server['port'] = cfg.get('smtp', 'port')
			auth['login'] = cfg.get('auth', 'login')
			auth['password'] = cfg.get('auth', 'password')
		except:
			print("Файл конфигурации повреждён...")
			exit(1)
	else:
		print("Config 'config.ini' not found.")

	return (auth, server)
