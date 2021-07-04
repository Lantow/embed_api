from flask import Flask, request, jsonify
from embed_and_reduce.emb_and_reduce import ReduceDim, CleanAndEmb, EmbAndReduce
app = Flask(__name__)

@app.route('/embed_string', methods=['POST'])
def embed_string():
    if request.method == 'POST':
        post = request.get_json()
                
        try:
            CE = CleanAndEmb(post["search_string"])
            CE.clean_and_embed()
            embedding = CE.embedding
        except Exception as E:
            raise E
        
        return jsonify({"emb":embedding.tolist()})

@app.route('/dim_reduce', methods=['POST'])
def dim_reduce():
    if request.method == 'POST':
        post = request.get_json()
        
        try:
            RD = ReduceDim(post["embedding"])
            RD.reduce_dim()
            reduced_emb = RD.emb100
        except Exception as E:
            raise E
        
        return jsonify({"emb100":reduced_emb.tolist()})
    
@app.route('/dim_reduce_and_emb', methods=['POST'])
def embed_and_reduce():
        if request.method == 'POST':
            post = request.get_json()
            
        try:
            ER = EmbAndReduce(post["search_string"])
            ER.clean_and_embed()
            ER.reduce_dim()
            reduced_emb = ER.emb100
        except Exception as E:
            raise E
        
        return jsonify({"emb100":reduced_emb.tolist()})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug='True')