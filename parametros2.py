from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo"

#Recibiendo rutas como parametros en mis rutas, si quiero recibir enteros en lugar de string, le coloco la palabra int
@app.route('/params/<name>/<int:num>')
def params(name = 'default', num = 0):
    return "El parametro es: {}, {}".format(name, num)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)