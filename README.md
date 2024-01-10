#### Парсер для маркетплейса https://www.wildberries.ru/ для категории "блузки и рубашки"

#### Установка

+ Клонировать репозиторий

+ Установить виртуальное окружение
    + python -m venv venv
    + .\venv\Scripts\activate (for windows)
    + source venv/biv/activate (for linux)

+ запустить командой python3 parser.py

#### Описание

Парсер делает запрос на api сервера, откуда приходят данные на сайт https://www.wildberries.ru/.
Приходят данные в формате json. Далле извлекаются следующие данные о товарах:

+ id
+ brand
+ name
+ price
+ promo_price

Эти данные записываются в формат csv в папку data.


