from flask import Flask,jsonify,request
import csv

all_articles = []
liked_articles = []
unliked_articles = []
with open('articles.csv',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
app=Flask(__name__)
@app.route('/get-articles')

def get_aricles():
    return jsonify({
        'data':all_articles[0],
        'status':'success'
    })

@app.route("/liked-movies",methods=['POST'])
def likeds_movies():
    articles = all_movies[0]
    all_movies = all_movies[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":'success'
    }),201
@app.route("/unliked-movies",methods=['POST'])
def unlikeds_movies():
    articles = all_movies[0]
    all_movies = all_movies[1:]
    unliked_articles.append(articles)
    return jsonify({
        "status":'success'
    }),201

if __name__ == "__main__":
    app.run()