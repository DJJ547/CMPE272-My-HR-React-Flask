from flask import Flask, Response, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
# put your key and secrets in a .env file
# and access it with key_name = os.getenv("<key_name>")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
