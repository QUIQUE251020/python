from flask import Flask, request
import sett

app = Flask(__name__)

@app.route("/bienvenido", methods=["GET"])
def bienvenidos():
    return "Hola mundo desde Flask"


@app.route("/webhook", methods=["GET"])
def verificar_token():
    try:    
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == sett.token and challenge != None:
            return challenge
        else:
            return "token incorrecto",403

    except Exception as e:
        return e, 403
    


if __name__=="__main__":
    app.run()