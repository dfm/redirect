import flask

app = flask.Flask(__name__)
app.config.debug = False


@app.route("/")
def index():
    return flask.redirect("http://dan.iel.fm")


@app.errorhandler(404)
def page_not_found(e):
    return flask.redirect("http://bit.ly/" + flask.request.path)


if __name__ == "__main__":
    app.run()
