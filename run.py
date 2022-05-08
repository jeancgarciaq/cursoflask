from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo"

if __name__ == '__main__':
    """
        port me permite establecer el puerto donde quiero que se ejecuta el programa
        debug cuando está en True muestra todos los cambios que se realizan al proyecto
    """
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    #probando el puerto 8000
    app.run(port=8000,debug=True)
