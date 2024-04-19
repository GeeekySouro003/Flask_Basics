from flask import Flask,request

app=Flask(__name__)



@app.route('/hello') ## Differrent ways of route creation
def hello():
    return "<h2>Hello Flask!</h2>"
@app.route('/') 
def index():
    return "<h1>Hello World</h1>"


@app.route('/greet/<name>') ## This is how Dynamic URLS are created and work
def greet(name):
    return f"Hello {name}"

@app.route('/cal/<int:num1>/<int:num2>')  ## URL PARAMETERS
def cal(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route('/handle_url_params')
def handle_url():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get['greeting']
        name=request.args.get['name']
        return f"{greeting},{name}"
    else:
        return "Some parameters are missing"
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555,debug=True)