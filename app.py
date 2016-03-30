from flask import Flask, jsonify
import dictionary

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Countdown Solver API'

@app.route('/solve/<string:word>')
def solver(word):
    resultset = dictionary.find_largest_anagram(word)
    results = list(resultset)
    return jsonify(anagrams= results)
