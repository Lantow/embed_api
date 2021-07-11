import numpy as np
from flask import Flask, request, jsonify
from embed_and_reduce.emb_and_reduce import ReduceDim, CleanAndEmb, EmbAndReduce, Tokenize
app = Flask(__name__)

@app.route('/tokenize_tekst', methods=['POST'])
def tokenize_tekst():
    if request.method == 'POST':
        post = request.get_json()
        
        try:
            T = Tokenize()
            text = post["search_string"]
            sent_tokenized_text = T.tokenize_raw_text_data(text)
        except Exception as E:
            raise E
        
        return jsonify({"tknz_txt": sent_tokenized_text})

@app.route('/embed_string', methods=['POST'])
def embed_string():
    if request.method == 'POST':
        post = request.get_json()
        
        try:
            CE = CleanAndEmb()
            text = post["search_string"]
            embedding = CE.clean_and_embed(text)
        except Exception as E:
            raise E
        
        return jsonify({"emb": embedding.tolist()})

@app.route('/dim_reduce', methods=['POST'])
def dim_reduce():
    if request.method == 'POST':
        post = request.get_json()
        
        try:
            RD = ReduceDim()
            embedding = post["emb"]
            if type(embedding) is list:
                embedding = np.array(embedding)
            reduced_embedding = RD.reduce_dim(embedding)
        except Exception as E:
            raise E
        
        return jsonify({"emb100": reduced_embedding.tolist()})

@app.route('/dim_reduce_and_emb', methods=['POST'])
def embed_and_reduce():
        if request.method == 'POST':
            post = request.get_json()
        
        try:
            ER = EmbAndReduce()
            text = post["search_string"]
            reduced_embedding = ER.embed_and_reduce(text)
        except Exception as E:
            raise E
        
        return jsonify({"emb100": reduced_embedding.tolist()})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug='True')