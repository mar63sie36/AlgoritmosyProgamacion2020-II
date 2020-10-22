from flask import flask
#Se crea un objeto del tipo app
app = Flask (_name_)

@app.route('/')
def home():
    return 'Gracias por visitar nuestra página'

if _name_ == '__main__':
    app.run()
    
