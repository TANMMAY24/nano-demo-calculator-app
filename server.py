from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    """
    Add two given numbers.

    Parameters:
        first (number): The first number to add.
        second (number): The second number to add.

    Returns:
        JSON object: A JSON object with the following properties:
            result (number): The result of the summation.
    """
    # data = json.loads(request.data)
    first = data['first']
    second = data['second']
    result = first + second
    # return json.dumps({'result': result})
    return result

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    """
    Subtract two given numbers.

    Parameters:
        first (number): The first number to subtract.
        second (number): The second number to subtract.

    Returns:
        JSON object: A JSON object with the following properties:
            result (number): The result of the subtraction.
    """
    
    first = data['first']
    second = data['second']
    result = first - second
    return result
if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
