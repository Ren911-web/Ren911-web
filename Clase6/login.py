from flask import Blueprint, request, jsonify
Login = Blueprint('Login',__name__)

@Login.route('/login', methods=['POST'])
def login_user():
    username = request.json.get('username')
    password = request.json.get('password')
    print("Headers", request.headers)
    print(f"Usuario: {username}, Password: {password}")

    codRes,menRes,accion= login(username, password)

    salida = {
        "codRes": "ok",
        "menRes": "Login exitoso",
        "user": username,
        "accion": "Login"
    }
    return jsonify(salida)
def login(user, password):
    userLocal = "Leandro"
    passLocal = "Leogl.09876"
    codRes= "SIN_ERROR"
    menRes= "OK"

    try:
        print("Verificar login")
        if user == userLocal and apssword == passlocal:
            print("Login exitoso")
            accion="Succes"
        else:
            print("Usuario o contraseña incorrectos")
            codRes= "Error"
            menRes= "Usuario o password incorrecto"
            print("Login fallido")
    except Exception as e:
        print("ERROR", str(e))
        codRes= "ERROR"
        menRes='Msg: ' +str(e)
        accion= "Error interno"
    return codRes, menRes, accion