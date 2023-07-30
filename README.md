# telegram_username_checker


In this repository you can find the code that will help you check if the telegram login is free

//

В данном репозитории вы сможете найти код, который поможет вам проверить свободен ли логин телеграмма.



Принцип действия программы: в функцию передается файл с сессией telethon и ник, который нужно будет проверить.
Для проверки используется telethon.TelegramClient.get_entity() и в случае удачной проверки с помощью functions.account.CheckUsernameRequest проверяется валидность юзернейма

//

The principle of operation of the program: a file with a telethon session and a nickname is passed to the function, which will need to be checked.
Telethon is used for verification.TelegramClient.get_entity() and in case of successful verification using functions.account.CheckUsernameRequest validates the username

