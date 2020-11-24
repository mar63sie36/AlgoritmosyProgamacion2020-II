from flask import Flask, request, make_response, redirect,  render_template, url_for
import utilidades as helper
#se crea un objeto tipo app
app= Flask(__name__)
fileNameCredential= 'usuarios.csv'
data= helper.leerArchivo(fileNameCredential)

@app.errorhandler(404) 
def not_found(error): 
    return render_template(404)
    return render_template('404.html')

@app.route('/') 
def home(): 

    return render_template('home.html')
    data= helper.leerArchivo('usuarios.csv')
    print (list(data['user'].values()))
    return redirect(url_for('login')) 

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/hello')
def helloRoute(): 
    neko= request.cookies.get('neko')
    ip= request.cookies.get('ip')
    return render_template ('hello.html', mascota= neko, userIp= ip)
@app.route('/hey')
def heyRoute():
    return render_template('hey.html')
@app.route('/personajes')
def personajesRoute(): 
    personajes= request.cookies.get('personajes') 
    ip= request.cookies.get('ip')
    return render_template('personajes.html', tipo= personajes,userip= ip  )
@app.route('/lugares') 
def lugaresRoute():  
    lugares= request.cookies.get('lugares')
    ip= request.cookies.get('ip')
    return  render_template('lugares.html', tipo= lugares, userip= ip)

@app.route('/signin', methods = ['POST','GET'])
def singin():

    if request.method == 'POST':
        helper.saveUser (data, fileNameCredential,request.form['name'],request.form ['pass'] )
        return redirect(url_for('success'))
    else: 
        return render_template('signIn.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    data = helper.leerArchivo(fileNameCredential)
    if request.method == 'POST':
        nameUser = request.form['name']
        passUser = request.form ['pass']
        output = helper.validatePassword (data, nameUser, passUser)
        if (output == True):
            return  redirect(url_for('home'))
        elif (output == 'Usuario no registrado'):
            return  redirect(url_for('singin'))
        if (passUser == 'hola1234'):
            return  redirect(url_for('home'))
        else:
            return 'Falló proceso de autenticación'
    else: 
        return render_template('login.html')
if __name__ == '__main__': 
    app.run()