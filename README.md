# nginx HTTP load balancer
Использование nginx в качестве балансировщика нагрузки.

![nginx_meme](https://user-images.githubusercontent.com/104680106/200335888-73c02cdd-e32a-4748-85d7-917552b738f1.jpg)

# Описание проекта
- В докере поднимается 6 инстансов приложения, после них поднимается nginx
- Начинает работать скрипт, отправляющий запросы на сервер nginx, который распределяет нагрузку по серверам
- Через 50с останавливается один из контейнеров, и nginx распределяет нагрузку на оставшиеся сервера
- Xерез 150с контейнер с сервером запускается и всё стабилизируется
- Каждые 10 секунд на экран будет выводиться статистика по каждому серверу и количеству запросов на нем


# Установка и запуск
+ Склонировать репозиторий с Github
'git@github.com:kam1dere/nginx-HTTP-load-balancer.git'
+ Перейти в директорию проекта
+ Запустить скрипты

'chmod u+x ./run.sh'

'sudo ./run.sh'!

+ Остановка работы

Автоматически остановиться через 300с
