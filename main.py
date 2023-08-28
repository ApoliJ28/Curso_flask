from flask import Flask, redirect, url_for, render_template, request, flash

# Creamos la instancia de Flask
app = Flask(__name__)

@app.before_request
def before_request():
    print("Antes de la petición")
@app.after_request
def after_request(response):
    print("Despues de la petición")
    return response
@app.route('/')
def index():
    flash('Has iniciado en el index del proyecto Flask')
    print("Accediendo al index o pagina principal")
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
    diccionario = {'title': 'Acerca de',
                'encabezado': 'Acerca de mi'}
    return render_template('acercade.html', datos = diccionario)

@app.route('/condicionybucle')
def condicionybucle():
    datos = {
        'edad': 50,
        'nombre': ['Jose','Mar', 'Lucia', 'Eva']
    }
    return render_template('condicionybucle.html', datos = datos)

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

def pagina_no_encontrada(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.secret_key = 'clave-flask'
    app.run(debug= True, port=8080)