# Send Email Script
Скрипт для отправки эектронной почты.

# Инструкция
Авторизационные данные *Пароль и Логин* загружаются из файла **config.ini**
1. Создайте в папке проекта файл **config.ini** и отформатируйте его как показано в примере ниже 

    
    [smtp]  
    server=smtp.domain.ru  
    port=465   
    [auth]  
    login=username@domain.ru  
    password=1234567890  


### Где: 
* **server** Имя сервера с которого бедете отправлять письмо, например *smtp.yandex.ru*
* **port** Порт для подключения, мы используем протокол *smtp* c *SSL* по этому оставляем **465**
* **login** Логин, с которого вы хотите отправить письмо, например *username@ya.ru*
* **password** Пароль к вашему ящику. *Создайте в сервисе* __ПАРОЛЬ ПРИЛОЖЕНИЯ__ и используйте его

2. Запустите скрипт **main.py** на выполнение
3. Следуя подсказкам введите  *Тему*, *Текст* и *Адрес получателя*
4. В случае удачного отправления в термитале высветится **DONE**

# Примечание
В файле **config.ini** используйте *server* и *login* одного сервиса