# Создать собственный файл маршрутов для приложения news (news/urls.py)

# Через функцию include подключить маршруты в основные маршруты (itg/urls.py)

# Создать новый маршрут get_news_by_id (динамический) и создать для него представление
# в итоге при переходе по URL 127.0.0.1:8000/news/5 на странице должна появляться надпись
# Новость 5

# Задать структуру для хранения шаблонов, например news/templates/news/
# Создать там первый шаблон catalog.html:
# <!DOCTYPE html>
# <!-- ЭТО ТОЧНО ДАННЫЕ ИЗ ШАБЛОНА -->
# <html lang="ru">
#     <head>
#         <meta charset="UTF-8">
#         <title>Каталог</title>
#     </head>
#     <body>
#         <h1>Каталог новостей</h1>
#     </body>
# </html>

# создать маршрут и представление для рендера этого шаблона

# Создать простую структуру данных в представлениях по типу:
# info = {
#     "users_count": 100600,
#     "news_count": 100600,
#     "menu": [
#         {"title": "Главная",
#          "url": "/",
#          "url_name": "index"},
#         {"title": "О проекте",
#          "url": "/about/",
#          "url_name": "about"},
#         {"title": "Каталог",
#          "url": "/news/catalog/",
#          "url_name": "catalog"},
#     ]
# }
# Передать данные в шаблон catalog.html
# Меню "Главная - О проекте - Каталог" должно выводиться с помощью цикла

#   Описать маршруты 
#   /catalog,
#   /catalog/<int:news_id/>,
#   /catalog/<slug:slug>
#   и создали соответствующие представления в файле views.py
#   catalog возвращает HttpResponse("Каталог новостей")
#   get_news_by_id возвращает HttpResponse(f"Новость {news_id}")
#   get_category_by_name возвращает HttpResponse(f"Категория {slug}")
