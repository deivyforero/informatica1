from flask import Flask, render_template
from fabricas import *
from random import choice

app = Flask(__name__)


@app.route('/')
def principal():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()

    productos = []

    productos.append(arma)
    productos.append(escudo)

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)
