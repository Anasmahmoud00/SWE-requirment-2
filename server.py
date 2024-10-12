from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Task3.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['fname']
    last_name = request.form['lname']
    email = request.form['Email']
    number = request.form['phone']

    return render_template('success.html', first_name=first_name, last_name=last_name, email=email, number=number)

if __name__ == '__main__':
    app.run(debug=True)
