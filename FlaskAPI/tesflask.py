from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/home")
def hello():
    #print("Hello") 
    return "Hello"
    #return "<h1>HELLOW</h1>"  #HTML

@app.route("/postdata", methods=['POST'])
def postdata():
    try: #client succes
        res = {}
        data = request.json
        print("receivce paylad => " , data)
        
        res['isSucces'] = True
        res['data'] = data 
        return jsonify(res),200
    except Exception as e: #server EROOR
        res={}
        res['isSucces'] = False
        res['data'] = str(e)
        return jsonify(res),500 

# @app.route("/siswa/daftarbaru", methods=['POST'])
# def insert_siswabaru():
    

        

if __name__ == "__main__":
    ip = "192.168.0.104"
    port = 5001
    app.run(ip,port,debug=True)