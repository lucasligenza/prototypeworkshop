from flask import Flask
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

load_dotenv()

# 
app.config['Debug'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello():
    return "Hello lucas!"

@app.route('/api/data')
def example():
    return "Hello Everyone"

if __name__ == '__main__':
    app.run(debug=True)