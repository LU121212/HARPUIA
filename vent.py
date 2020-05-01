from flask import Flask,render_template # llamando al framework

app1= Flask(__name__)#definimos el nombre de la variable
@app1.route('/') # para ir a la url
def home(): #una vez establecida la ruta establecemos los define
    return render_template("contenido.html")

@app1.route('/zero')
def zero(): #una funcion que va a manejar la ruta por usa usa el define
    return render_template("contenidozero.html")   
@app1.route('/harpuia')
def harpuia(): #una funcion que va a manejar la ruta por usa usa el define
    return render_template("contenidoharpuia.html")       

if __name__== "__main__": #se jecuta el archivo principal y no un modulo
    app1.run(debug=True) #cada cambio que haga se actualiza solo

