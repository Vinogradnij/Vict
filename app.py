from handler_questions import HandlerQuestions
from flask import Flask, render_template, request

app = Flask(__name__)

topics = [{'name': 'География', 'url': '/geography'},
          {'name': 'История', 'url': '/history'},
          {'name': 'Информатика', 'url': '/informatics'}]

server = 'http://localhost'

handler = None


@app.route('/')
def index():
    return render_template('index.html', title='Викторина', topics=topics)


@app.route('/geography')
def geography():
    return render_template('topic.html', title='География', topic='География', server='/questions')


@app.route('/history')
def history():
    return render_template('topic.html', title='История', topic='История', server='/questions')


@app.route('/informatics')
def informatics():
    return render_template('topic.html', title='Информатика', topic='Информатика', server='/questions')


@app.route('/questions', methods=['POST', 'GET'])
def questions():
    global handler
    record = {}
    if request.method == 'POST':
        if 'topic' in request.form:
            if request.form['topic'] == 'География':
                handler = HandlerQuestions(1)
                record = handler.get_question()
            elif request.form['topic'] == 'История':
                pass
            elif request.form['topic'] == 'Информатика':
                pass
        if 'answer' in request.form:
            handler.check_answer(request.form['answer'])
            record = handler.get_question()
            if not record:
                return render_template('congratulations.html', points=handler.points)

    return render_template('questions.html', title='Вопросы', question=record['question'],
                           answers=record['wrong_answers'])


if __name__ == '__main__':
    app.run(debug=True)
