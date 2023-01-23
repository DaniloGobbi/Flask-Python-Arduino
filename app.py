from pyfirmata import Arduino, util
import time
from flask import Flask, render_template, request

app = Flask(__name__)

Uno = Arduino("COM3")
it = util.Iterator(Uno)
it.start()

@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST":
        if request.form.get("botaoverde") == "verde":
            Uno.digital[5].write(1)
        elif request.form.get("botaoverde") == "verdeoff":
            Uno.digital[5].write(0)
        elif request.form.get("botaovermelho") == "vermelho":
            Uno.digital[6].write(1)
        elif request.form.get("botaovermelho") == "vermelhooff":
            Uno.digital[6].write(0)
        elif request.form.get("botaoamarelo") == "amarelo":
            Uno.digital[7].write(1)
        elif request.form.get("botaoamarelo") == "amarelooff":
            Uno.digital[7].write(0)
    return render_template("index.html")
    
    
