from flask import Flask

# Creamos la instancia de Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "texto nuevo sobre la marcha"

if __name__ == '__main__':
    app.run(debug= True, port=8080)