from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/')
def rgtuj():
    return 'Миссия Колонизация Марса'


@app.route('/promotion')
def rgtudthfbdfvfvdfvj():
    return 'Человечество вырастает из детства.<br>Человечеству мала одна планета.' \
           '<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!'


@app.route('/image_mars')
def fwefwefwefwefwefwefwefwefwef():
    return '''<h1>Заголовок первого уровня</h1>
    <img src="https://cdn.vashurok.ru/system/news/images/000/006/582/og/kolonist.jpg?1620984458"><br> Вот она какая, красная планета!'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="style.css">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 class="title">Жди нас марс</h1>
                    <img src="https://sun6-20.userapi.com/s/v1/ig2/qFa1Fc7Wd2mP_UHpG-XFY690gm-rNTgFQE2q_HACpfYvVOOxX_NvInxhPAd3J18tgZ_OVIufE4FiyHI5TEKKuwMQ.jpg?size=400x0&quality=96&crop=1,294,718,718&ava=1">
                    <p class="alert alert-primary">Человечество вырастает из детства.</p>
                    <p class="alert alert-primary">Человечеству мала одна планета.</p>
                    <p class="alert alert-primary">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="alert alert-primary">И начнем с Марса!</p>
                    <p class="alert alert-primary">Присоединяйся!</p>
                  </body>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')