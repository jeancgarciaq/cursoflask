from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo"

#Recibiendo parametros en mis rutas tipo get
#http://localhost:5000/params?params1=JeanGarcia
# También se puede recibir dos parametros
#http://localhost:5000/params?params1=JeanGarcia&params2=JanaGarcia
@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene el parametro')
    # Se tendrìa que añadir una segunda variable y asì sucesivamente para parámetro
    return "El parametro es: {}".format(param)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)