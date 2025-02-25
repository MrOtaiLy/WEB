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
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Отбор астронавтов</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .form-wrapper {
            max-width: 800px;
            margin: 40px auto;
            padding: 30px;
            background: #f8f9fa;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-weight: 700;
        }
        .form-label {
            font-weight: 600;
            color: #495057;
        }
        .btn-custom {
            background: #4a76a8;
            color: white;
            padding: 12px 25px;
            transition: all 0.3s;
        }
        .btn-custom:hover {
            background: #3b5f8a;
            transform: translateY(-2px);
        }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="form-wrapper">
        <h1>Анкета претендента на участие в миссии</h1>
        <form method="post">
          <div class="row g-4">
            <!-- Персональные данные -->
            <div class="col-md-6">
              <div class="mb-3">
                <input type="text" class="form-control form-control-lg" name="surname" placeholder="Фамилия" required>
              </div>
            </div>
            
            <div class="col-md-6">
              <div class="mb-3">
                <input type="text" class="form-control form-control-lg" name="name" placeholder="Имя" required>
              </div>
            </div>

            <div class="col-12">
              <div class="mb-3">
                <input type="email" class="form-control form-control-lg" name="email" placeholder="Электронная почта" required>
              </div>
            </div>

            <!-- Образование и профессия -->
            <div class="col-md-6">
              <div class="mb-3">
                <label class="form-label">Образование</label>
                <select class="form-select form-select-lg" name="education">
                  <option value="Начальное">Начальное</option>
                  <option value="Среднее">Среднее</option>
                  <option value="Высшее">Высшее</option>
                </select>
              </div>
            </div>

            <div class="col-md-6">
              <div class="mb-3">
                <label class="form-label">Профессия</label>
                <select class="form-select form-select-lg" name="profession">
                  <option value="инженер-исследователь">Инженер-исследователь</option>
                  <option value="пилот">Пилот</option>
                  <option value="строитель">Строитель</option>
                  <option value="экзобиолог">Экзобиолог</option>
                  <option value="врач">Врач</option>
                  <option value="инженер по терраформированию">Инженер по терраформированию</option>
                  <option value="климатолог">Климатолог</option>
                  <option value="специалист по радиационной защите">Специалист по радиационной защите</option>
                  <option value="астрогеолог">Астрогеолог</option>
                  <option value="гляциолог">Гляциолог</option>
                  <option value="инженер жизнеобеспечения">Инженер жизнеобеспечения</option>
                  <option value="метеоролог">Метеоролог</option>
                  <option value="оператор марсохода">Оператор марсохода</option>
                  <option value="киберинженер">Киберинженер</option>
                  <option value="штурман">Штурман</option>
                  <option value="пилот дронов">Пилот дронов</option>
                </select>
              </div>
            </div>

            <!-- Пол -->
            <div class="col-12">
              <div class="mb-3">
                <label class="form-label">Пол</label>
                <div class="d-flex gap-4">
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                    <label class="form-check-label" for="male">Мужской</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                    <label class="form-check-label" for="female">Женский</label>
                  </div>
                </div>
              </div>
            </div>

            <!-- Мотивация -->
            <div class="col-12">
              <div class="mb-3">
                <label class="form-label">Мотивация</label>
                <textarea class="form-control" name="motivation" rows="4" 
                  placeholder="Почему вы хотите стать участником миссии?" required></textarea>
              </div>
            </div>

            <!-- Чекбокс -->
            <div class="col-12">
              <div class="form-check mb-4">
                <input class="form-check-input" type="checkbox" id="ready" name="ready" value="true">
                <label class="form-check-label" for="ready">Готов(а) остаться на Марсе</label>
              </div>
            </div>

            <!-- Кнопка отправки -->
            <div class="d-grid">
              <button type="submit" class="btn btn-custom btn-lg">Отправить заявку</button>
            </div>
          </div>
        </form>
      </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>"""
    else:
        return "Форма успешно отправлена!"

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
