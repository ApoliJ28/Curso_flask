from flask import Flask, redirect, url_for, render_template

# Creamos la instancia de Flask
app = Flask(__name__)

@app.route('/')
def index():
    encabezado = "Encabezado desde flask"
    datos = {'titulo': 'Pagina principal',
            'encabezado': 'Bienvienido a mi pagina web'}
    return render_template('index.html', dato = datos)
    #return "Estamos en index o pagina principal"

@app.route('/redirecciona')
@app.route('/redirecciona/<string:sitio>')
def redirecciona(sitio = None):
    if sitio is not None:
        return redirect(url_for(sitio))
    else:
        return redirect(url_for('acercade'))

@app.route('/acercade')
def acercade():
    #return "<h1>Acerca de mi</h1>"
    return render_template('acercade.html')

@app.route('/saludame')
@app.route('/saludame/<string:nombre>')
@app.route('/saludame/<string:nombre>/<int:edad>')
def saludame(nombre = 'Victor', edad = None):
    if edad != None:
        return f"""
            <h1>Hola, </h1>
            <h3>{nombre}</h3>
            <h3>Tienes: {edad} años </h3>
    """
    else:
        return f"""
        <h1>Hola, </h1>
        <h3>{nombre}</h3>
    """

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"


if __name__ == '__main__':
    app.run(debug= True, port=8080)