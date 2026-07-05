from bottle import route, run, template, static_file


@route("/")
def index():
    return template("index.html")


@route("/static/<filename:path>")
def static(filename):
    return static_file(filename, root="static")


@route("/llms.txt")
def llms():
    return static_file("llms.txt", root=".")


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)
