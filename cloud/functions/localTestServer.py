from flask import Flask, request
from functions.searchArticles import search_articles
from functions.cors import run_function_with_cors_enabled
from functions.demo_fetchArticleDetail import demo_fetchArticleDetail
from functions.fetchArticleDetail import fetchArticleDetail

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/search', methods=['GET'])
def search():
    return run_function_with_cors_enabled(request, search_articles)

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    return run_function_with_cors_enabled(request, fetchArticleDetail)

@app.route('/demo_detail', methods=['GET', 'POST'])
def demo_detail():
    return run_function_with_cors_enabled(request, demo_fetchArticleDetail)


if __name__ == '__main__':
    app.run()
