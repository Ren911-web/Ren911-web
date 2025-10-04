from flask import Flask
from login import Login


app = Flask(__name__)
app.register_blueprint (Login)
app.register_blueprint (Logout)
@app.route('/')
def home():
    return "Hola, Mundo. Usa ctrl + shift + i para acceder a la configuracion de la página"
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='127.0.0.1') #La ultima Ip es solo para local host, en caso de querer una host online tiene que ser "0.0.0.0"
