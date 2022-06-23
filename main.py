from flask import Flask, jsonify, request
import csv

all_movies= []

with open('movies.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movie = []
unliked = []
not_watched = []

app = Flask(__name__)
@app.route('/get-movie')

def get_movie():
    return jsonify({
        'data':all_movies[0],
        'status':'success'

    })

@app.route('/like-movie', methods = ['POST'])

def like_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movie.append(movie)
    return jsonify({
        'status':'success'
    }), 201

@app.route('/unlike-movie', methods = ['POST'])

def unlike_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked.append(movie)
    return jsonify({
        'status':'success'
    }), 201

@app.route('/not_watched-movie', methods = ['POST'])

def not_watched_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched.append(movie)
    return jsonify({
        'status':'success'
    }), 201

if __name__ == '__main__':
    app.run()