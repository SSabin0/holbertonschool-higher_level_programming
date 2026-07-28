from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    return render_template('items.html', items=data['items'])
    # items=data['items'] passes the list to the template
    # now inside items.html you can use {{ items }} or loop over it

if __name__ == '__main__':
    app.run(debug=True, port=5000)
