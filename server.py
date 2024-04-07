from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

URL = 'https://newsapi.org/v2/everything'
API_KEY = "9e5144c33bb04094ad1ecedd097f448f"
QUERY = "machine learning"


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/test', methods=['GET'])
def test():
    url = URL

    # Set up the query parameters
    parameters = {
        'q': 'machine learning',  # Query term
        'pageSize': 5,
        'sortBy': 'publishedAt',  # Sort by the most recent articles first
        'language': 'en',  # Get articles written in English
        'apiKey': API_KEY,  # Your API key
    }

    # Make the GET request
    response = requests.get(url, params=parameters)
    return response.json()["articles"]


def everything_endpoint(query, page_size, page):
    # Set up the query parameters
    parameters = {
        'q': query,  # Query term
        'pageSize': page_size,
        'page': page,
        'sortBy': 'publishedAt',  # Sort by the most recent articles first
        'language': 'en',  # Get articles written in English
        'apiKey': API_KEY,  # Your API key
    }

    # Make the GET request
    response = requests.get(URL, params=parameters)
    return response.json()


@app.route('/get_data', methods=['GET'])
def get_data():
    response = everything_endpoint(QUERY, 5, 1)["articles"]
    return response


@app.route('/articles', methods=['GET'])
def articles():
    response = everything_endpoint(QUERY, 5, 1)["articles"]
    article_list = {}
    for i, article in enumerate(response):
        article_list[str(i)] = {
            "title": article["title"],
            "author": article["author"],
            "source": article["source"],
            "publishedAt": article["publishedAt"]
        }
    return article_list


@app.route('/articles/<number>', methods=['GET'])
def get_article(number):
    response = everything_endpoint(QUERY, 5, 1)["articles"][int(number)]
    return response


@app.route('/ml', methods=['GET'])
def get_article(number):
    response = everything_endpoint(QUERY, 5, 1)["articles"][int(number)]
    return response


if __name__ == '__main__':
    app.run()
