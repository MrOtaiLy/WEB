from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def mission():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    lines = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    ]
    return "<br>".join(lines)


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
  </head>
  <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/Mars.gif')}" alt="здесь должна была быть картинка, но не нашлась">
    <p>Вот она какая, красная планета!</p>
  </body>
</html>"""

@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Колонизация Марса</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
  </head>
  <body>
    <h1>Жди нас, Марс!</h1>
    <div class="alert alert-dark" role="alert">
      Человечество вырастает из детства.
    </div>
    <div class="alert alert-success" role="alert">
      Человечеству мала одна планета.
    </div>
    <div class="alert alert-secondary" role="alert">
      Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-warning" role="alert">
      И начнем с Марса!
    </div>
    <div class="alert alert-danger" role="alert">
      Присоединяйся!
    </div>
    <img src="{url_for('static', filename='img/mars.png')}" alt="Mars" class="img-fluid">
  </body>
</html>"""

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
