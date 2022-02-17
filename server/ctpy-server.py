import flask
from questions import question_bp

app = flask.Flask(__name__)
app.register_blueprint(question_bp)

@app.route('/')
def hello():
    return 'Hello. Use the http://<url>:<port>/question/<question number> endpoint to get started.'

if __name__=='__main__':
    app.run()
