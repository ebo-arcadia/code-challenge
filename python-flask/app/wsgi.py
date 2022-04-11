from flask import Flask, request, render_template, jsonify, Blueprint
from flask_cors import CORS
import requests

investment_products = Blueprint("investment_products", __name__)

app = Flask(__name__, template_folder='templates')
CORS(app)


@investment_products.route('/value/<int:price>')
def value(price=None):
    return "the price of this investment product is ${price} per share".format(price=price)


@investment_products.route('/marketcap/<int:marketcap>')
def cap(marketcap=None):
    return "market cap is ${marketcap} per share".format(marketcap=marketcap)


@investment_products.route('/exchange/<string:exchange>')
def cryptocurrency(exchange=None):
    return "This cryptocurrency is traded on {exchange}.".format(exchange=exchange)


app.register_blueprint(investment_products, name="stock", url_prefix="/stock")
app.register_blueprint(investment_products, name="bond", url_prefix="/bond")
app.register_blueprint(investment_products, name="cryptocurrency", url_prefix="/cryptocurrency")


@app.route('/')
def greeting():
    return render_template('base.html')


@app.route('/user/<username>/')
def display_user(username):
    return render_template('user.html', username=username)


@app.route('/todos/<int:todo_id>/', methods=['GET', 'POST'])
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


countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries/")
def get_countries():
    # return countries
    # this line works too as Flask automatically convert python list to json but not lists
    return jsonify(countries)

@app.post("/countries/")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)

