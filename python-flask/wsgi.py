from flask import Flask, request, render_template
from flask_cors import CORS
import requests
from markupsafe import escape

app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/')
def greeting():
    return render_template("todo.html")


@app.route('/user/<username>')
def display_user(username):
    return "<h1>Welcome, </h1>" + f'{escape(username)}' + "!"


@app.route('/todos/<int:todo_id>', methods=['GET', 'POST'])
def get_or_post_todo(todo_id):
    if request.method == 'GET':
        api_url = "https://jsonplaceholder.typicode.com/todos/" + f'{todo_id}'
        response = requests.get(api_url)
        data = response.json()
        return data
    if request.method == 'POST':
        userId = f'{todo_id}'
        id = request.form['id']
        title = request.form['title']
        completed = request.form['completed']
    else:
        return "Post error 405 method not allowed"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)

