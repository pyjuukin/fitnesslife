'''главная страница запуска приложения'''
from flask import Flask, render_template, request, blueprints

app = Flask(__name__)

# Тут пока обычные громозкие роуты, позже будут компктные блюпринты
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/news')
def news_page():
    return render_template('news.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/price')
def price_page():
    return render_template('price.html')

@app.route('/trainers')
def trainers_page():
    return render_template('trainers.html')

@app.route('/articles')
def articles_page():
    return render_template('articles.html')

@app.route('/photos')
def photos_page():
    return render_template('photos.html')

@app.route('/buy')
def buy_page():
    return render_template('buy.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run()


