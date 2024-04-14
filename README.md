﻿# Working with API
 ## Как запустить программу

1) Скачайте проект себе в папку 
2) Добавьте конфигурационный файл ```.venv```, сожержимое которого должно иметь следующий вид:
```
TOKEN = "(ваш токен)"
USER_ID = (ваш ID)
```
где токен вы получаете, [пройдя по ссылке](https://vkhost.github.io/).

Заходите в Настройки -> Выбираете нужные вам права -> Подтвердить -> Разрешить -> В поисковой строке появляется длинная ссылка, в которой знаки от *https://oauth.vk.com/blank.html#access_token=* до *&expires_in=* и есть ваш личный токен.


ID пользователя находите [на этом сайте](https://regvk.com/id/?ysclid=lt4p2qbybd691656600),
где вам понадобится лишь вставить ссылку на ваш профиль в ВК


В случае возникновения проблем с отображением русских букв в итоговом файле: 
File -> Referensis -> Settings -> (в поле вписываем files encoding) -> выбираем кодировку cyrillic (Windows 1251)
(пример решения в VSCode, в других приложениях аналогично).

