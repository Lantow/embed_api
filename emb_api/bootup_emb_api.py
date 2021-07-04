from flask import Flask, session, render_template, request, redirect, url_for, jsonify, send_from_directory, abort

app = Flask(__name__)

@app.route('/embed_string', methods=['POST'])
def embed_string():
    if request.method == 'POST':
        post = request.get_json()
        embedding = None # TODO: do the embedding here
        return embedding

@app.route('/dim_reduce', methods=['POST'])
def dim_reduce():
    if request.method == 'POST':
        post = request.get_json()
        reduced_emb = None # TODO: do the dimensionality reduction here
        return reduced_emb
    
@app.route('/dim_reduce_and_emb', methods=['POST'])
def embed_and_reduce():
        if request.method == 'POST':
            post = request.get_json()
            embedding = None # TODO: do the embedding here
            reduced_emb = None # TODO: do the dimensionality reduction here
            return reduced_emb