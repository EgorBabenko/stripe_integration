## Локальный старт:
Склонируйте репозиторий на локальный компьютер, выполнив в терминале команду:
```
git clone https://github.com/EgorBabenko/stripe_integration.git
```
Находясь в корневой директории проекта, создайте docker image:
```
docker build -t stripe .
```
Создайте/запустите docker container следующей командой:
```
docker run -p 8000:8000 stripe
```

Проект станет доступен на локальном сервере:
http://127.0.0.1:8000/

### Тестовый пользователь с правами администратора:
username: admin

password: admin

Доступ в админ-панель: http://127.0.0.1:8000/admin