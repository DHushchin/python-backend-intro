from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aircraft')
def aircraft():
    return render_template('aircraft.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()
