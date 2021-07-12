from flask import Flask, request, jsonify
from embed_and_reduce.emb_and_reduce import EmbAndReduce
import numpy as np
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
pca_path = Path(ROOT_DIR).parent / "pca.pkl"
app = Flask(__name__)

EmbedAndReduce = EmbAndReduce(pca_path, Path.home() / "bert")

@app.route('/embed_string', methods=['POST'])
def embed_string():
    if request.method == 'POST':
        string = request.form['string']
        try:
            embedding = EmbedAndReduce.clean_and_embed(string)
        except Exception as E:
            raise E
        
        return jsonify({"emb":embedding.tolist()})

@app.route('/dim_reduce', methods=['POST'])
def dim_reduce():
    if request.method == 'POST':
        embedding = request.form["embedding"]
        embedding = np.asarray(embedding)
        try:
            reduced_emb = EmbedAndReduce.dim_reduce(embedding)
        except Exception as E:
            raise E

        return jsonify({"emb100":reduced_emb.tolist()})

@app.route('/embed_and_reduce', methods=['POST'])
def embed_and_reduce():
    if request.method == 'POST':
        string = request.form['string']
        try:
            reduced_emb = EmbedAndReduce.embed_and_reduce(string)
        except Exception as E:
            raise E
        
        return jsonify({"emb100":reduced_emb.tolist()})

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug='True')