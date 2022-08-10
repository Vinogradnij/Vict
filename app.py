from flask import Flask, render_template

app = Flask(__name__)

categories = ['География', 'История', 'Информатика']
server = 'http://localhost'


@app.route('/')
def index():
    return render_template('index.html', title='Викторина', categories=categories)


@app.route('/geography')
def geography():
    return render_template('categorie.html', title='География', categorie='География', server=server)


@app.route('/history')
def history():
    return render_template('categorie.html', title='История', categorie='История', server=server)


@app.route('/informatics')
def informatics():
    return render_template('categorie.html', title='Информатика', categorie='Информатика', server=server)


if __name__ == '__main__':
    app.run()
