from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p> """

if __name__ == '__main__':
    app.run()
