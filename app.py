from flask import Flask, render_template

app = Flask(__name__)

categories = ['География', 'История', 'Информатика']


@app.route('/')
def index():
    return render_template('index.html', title='Викторина', categories=categories)


if __name__ == '__main__':
    app.run()
