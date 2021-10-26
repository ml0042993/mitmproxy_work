from flask import Flask,render_template
from flask_bootstrap import Bootstrap
import json
__all__ = ["app"]
app = Flask(__name__)
bootstrap = Bootstrap(app)
def readfile():
	with open('info.txt', 'r', encoding='utf8') as f:
		return f.read()
@app.route('/')
def index():
	messages = json.loads(readfile())
	print(type(messages))
	return render_template('index.html', messages=messages)


if __name__ == '__main__':
	app.run(port=5555, debug=True)
