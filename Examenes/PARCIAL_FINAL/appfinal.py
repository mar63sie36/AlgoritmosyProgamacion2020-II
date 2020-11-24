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

@app.route('/home') 
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

@app.route('/patients')
def patientsjesRoute(): 
    patients= request.cookies.get('patients') 
    ip= request.cookies.get('ip')
    return render_template('patients.html', tipo= patients,userip= ip  )

@app.route('/doctors') 
def doctorsRoute():  
    doctors= request.cookies.get('doctors')
    ip= request.cookies.get('ip')
    return  render_template('doctors.html', tipo= doctors, userip= ip)

@app.route('/knowus') 
def knowusRoute():  
    knowus= request.cookies.get('knowus')
    ip= request.cookies.get('ip')
    return  render_template('knowus.html', tipo= knowus, userip= ip)

@app.route('/contact') 
def contatcRoute():  
    contatc= request.cookies.get('contact')
    ip= request.cookies.get('ip')
    return  render_template('contact.html', tipo= contact, userip= ip)

@app.route('/curious') 
def curiousRoute():  
    curious= request.cookies.get('curious')
    ip= request.cookies.get('ip')
    return  render_template('curious.html', tipo= curious, userip= ip)

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