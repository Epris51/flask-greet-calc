from flask import Flask, request
import operations  # Assuming operations.py contains the arithmetic functions

app = Flask(__name__)

def do_math(operation, a, b):
    """Perform the math operation with a and b."""
    operation_funcs = {
        'add': operations.add,
        'sub': operations.sub,
        'mult': operations.mult,
        'div': operations.div
    }
    return operation_funcs[operation](a, b)

@app.route('/add')
def add_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.add(a, b)
    return str(result)

@app.route('/sub')
def sub_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.sub(a, b)
    return str(result)

@app.route('/mult')
def mult_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.mult(a, b)
    return str(result)

@app.route('/div')
def div_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.div(a, b)
    return str(result)

@app.route('/math/<operation>')
def all_in_one(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = do_math(operation, a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)

