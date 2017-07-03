from flask import Flask
app = Flask(__name__)
@app.route('/')
def helloworld():
    return "hello world "
@app.route('/user/<username>')
def get_username(username):
    return "user %s" %username
if __name__ =="__main__":
    app.debug =True
    app.run()
