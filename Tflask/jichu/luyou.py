from flask import Flask
app = Flask(__name__)
@app.route('/')
def fristpage():
    return "fristpage"
@app.route('/second')
def secondpage1():
    return "second page"
@app.route('/second/thridpage/')
def thridpage():
    return "thridpage"
@app.route('/second1/<username>')
def username(username):
    return "the name is %s" %username
@app.route('/second2/<float:number>')
def percent(number):
    return "percent is %d" %number

if __name__ == "__main__":
    app.run(debug=True)
