from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route('/<name>')
def test(name=None):
	return render_template('index.html', name=name)