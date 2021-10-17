from flask import Flask, request

app = Flask("something")


@app.route('/cars', methods=['GET', 'POST', 'DELETE'])
def get_cars():
    if request.method == 'GET':
        car_list = open("car-list.txt", "r").read()
        car_list
        return car_list
    elif request.method == "POST":
        return "saved new car"


@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)
