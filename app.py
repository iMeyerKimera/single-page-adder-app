from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world!"

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        value_one = int(request.form['number-one'])
        value_two = int(request.form['number-two'])
        total = value_one + value_two
        return render_template('index.html', string='World', value=total)
    return render_template('index.html', string='World')

if __name__ == '__main__':
    app.run(debug=True)