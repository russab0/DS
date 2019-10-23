from flask import Flask, render_template, send_file

app = Flask(__name__, template_folder="templates")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', )


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', )


@app.route('/screen1.png')
def image1():
    return send_file('screen1.png', mimetype='image/png')

@app.route('/screen2.png')
def image2():
    return send_file('screen2.png', mimetype='image/png')

@app.route('/screen3.png')
def image3():
    return send_file('screen3.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
