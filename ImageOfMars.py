from flask import Flask, url_for, request

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


@app.route("/promotion_image")
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


@app.route("/astronaut_selection", methods=["GET", "POST"])
def astronaut_selection():
    if request.method == "GET":
        return """<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Отбор астронавтов</title>
  </head>
  <body>
    <h1>Анкета претендента</h1>
    <form method="post">
      <input type="text" name="surname" placeholder="Фамилия"><br>
      <input type="text" name="name" placeholder="Имя"><br>
      <input type="email" name="email" placeholder="Email"><br>
      <label for="education">Образование:</label>
      <select id="education" name="education">
        <option value="Начальное">Начальное</option>
        <option value="Среднее">Среднее</option>
        <option value="Высшее">Высшее</option>
      </select><br>
      <label for="profession">Профессия:</label>
      <select id="profession" name="profession">
        <option value="инженер-исследователь">инженер-исследователь</option>
        <option value="пилот">пилот</option>
        <option value="строитель">строитель</option>
        <option value="экзобиолог">экзобиолог</option>
        <option value="врач">врач</option>
        <option value="инженер по терраформированию">инженер по терраформированию</option>
        <option value="климатолог">климатолог</option>
        <option value="специалист по радиационной защите">специалист по радиационной защите</option>
        <option value="астрогеолог">астрогеолог</option>
        <option value="гляциолог">гляциолог</option>
        <option value="инженер жизнеобеспечения">инженер жизнеобеспечения</option>
        <option value="метеоролог">метеоролог</option>
        <option value="оператор марсохода">оператор марсохода</option>
        <option value="киберинженер">киберинженер</option>
        <option value="штурман">штурман</option>
        <option value="пилот дронов">пилот дронов</option>
      </select><br>
      Пол: <input type="radio" name="sex" value="male"> Мужской
          <input type="radio" name="sex" value="female"> Женский<br>
      <textarea name="motivation" placeholder="Мотивация"></textarea><br>
      Готовы ли остаться на Марсе? <input type="checkbox" name="ready" value="true"><br>
      <button type="submit">Отправить</button>
    </form>
  </body>
</html>"""
    else:
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
