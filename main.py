import requests
from flask import Flask,render_template
from extra import get_similarity

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/get_response')
def get_response():
    api_url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
    response = requests.get(api_url)
    response = get_similarity(response)
    if response:
        return response
    else:
        return 'Failed to fetch data from the remote API', 500  # Return an error message if the request failed


if __name__ == '__main__':
    app.run(port=8000,debug=True)