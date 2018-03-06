from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Mars!"

if __name__ == "__main__":
    application.run()
