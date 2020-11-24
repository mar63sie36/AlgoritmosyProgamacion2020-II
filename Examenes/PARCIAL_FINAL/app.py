from flask import Flask, request, make_response, redirect, render_template, url_for

app= Flask(__name__) 

@app.errorhandler(404) 
def not_found(error): 
    return render_template('404.html') 

@app.route('/home') 
def home(): 
    return render_template('home.html') 

@app.route('/patients') 
def patientsRoute(): 
    patients= request.cookies.get('patients') 
    ip= request.cookies.get('ip')
    return render_template('patients.html', tipo= patients, userIp= ip)

@app.route('/doctors') 
def doctorsRoute(): 
    doctors= request.cookies.get('doctors') 
    ip= request.cookies.get('ip')
    return render_template('doctors.html', tipo= doctors, userIp= ip)

@app.route('/knowus') 
def knowussRoute(): 
    knowus= request.cookies.get('knowus') 
    ip= request.cookies.get('ip')
    return render_template('knowus.html', tipo= knowus, userIp= ip)  

@app.route('/contact')
def contactRoute(): 
    contact= request.cookies.get('contact') 
    ip= request.cookies.get('ip')
    return render_template('contact.html', tipo= contact, userIp= ip)

@app.route('/curious') 
def curiousRoute(): 
    curious= request.cookies.get('curious') 
    ip= request.cookies.get('ip')
    return render_template('curious.html', tipo= curious, userIp= ip) 

 
