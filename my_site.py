from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def get_index():
    return """<html>ß
    <body><h1>Hello, World!</h1></body>
    </html>"""


# http://127.0.0.1:5001/hello/jsadjflsdjfla
@app.route('/hello/<firstname>/<lastname>')
def hello(firstname, lastname):
    return f"""<html>
    <body><h1>Hello</h1>
    <p>Hello, {firstname}, {lastname}</p>
    """

# http://127.0.0.1:5001/multiply/3/6
@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    return render_template("multiply.html", x=x, y=y)


@app.route("/form", methods=['GET', 'POST'])
def show_form():
    x = request.values.get('x')
    y = request.values.get('y')
    errormessage = None
    if x and y:
        try:
            product = int(x) * int(y)
        except ValueError:
            product = None
            errormessage = "Unkown error occured!!!"
    else:
        product = None
    return render_template("form.html", x=x, y=y, product=product,
                           errormessage=errormessage)


if __name__ == "__main__":
    app.run(port=5001)
