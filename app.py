from flask import Flask, jsonify, render_template
import dictionary
import os
my_dir = os.path.dirname(__file__)
file_path = os.path.join(my_dir, 'templates')
app = Flask(__name__, template_folder=file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve/<string:word>')
def solver(word):
    resultset = dictionary.find_largest_anagram(word)
    results = list(resultset)

    return jsonify(anagrams= results)
