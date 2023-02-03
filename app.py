from flask import render_template, Flask

app = Flask(__name__, static_folder='src/')


@app.route("/")
def hello_world():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)
