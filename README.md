# Описание сервиса
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы»,
«Музыка».

# Алгоритм регистрации пользователей
1. Пользователь отправляет запрос с параметром email на /auth/email/.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email .
3. Пользователь отправляет запрос с параметрами email и confirmation_code на /auth/token/, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на /users/me/ и заполняет поля в своём профайле (описание полей — в документации).
