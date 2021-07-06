from flask import Flask, request, jsonify
from embed_and_reduce.emb_and_reduce import EmbAndReduce
import numpy as np

app = Flask(__name__)

EmbedAndReduce = EmbAndReduce()

@app.route('/embed_string', methods=['POST'])
def embed_string():
    if request.method == 'POST':
        post = request.get_json()

        try:
            embedding = EmbedAndReduce.clean_and_embed(post["search_string"])
        except Exception as E:
            raise E
        
        return jsonify({"emb":embedding.tolist()})

@app.route('/dim_reduce', methods=['POST'])
def dim_reduce():
    if request.method == 'POST':
        post = request.get_json()
        embedding = np.asarray(post["embedding"])

        try:
            reduced_emb = EmbedAndReduce.dim_reduce(embedding)
        except Exception as E:
            raise E

        return jsonify({"emb100":reduced_emb.tolist()})
    
@app.route('/embed_and_reduce', methods=['POST'])
def embed_and_reduce():
        if request.method == 'POST':
            post = request.get_json()

        try:
            reduced_emb = EmbedAndReduce.embed_and_reduce(post["search_string"])
        except Exception as E:
            raise E
        
        return jsonify({"emb100":reduced_emb.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug='True')