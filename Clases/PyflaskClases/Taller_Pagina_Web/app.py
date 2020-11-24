from flask import Flask, request, make_response, redirect, render_template, url_for

app= Flask(__name__) 

@app.errorhandler(404) 
def not_found(error): 
    return render_template('404.html') 

@app.route('/') 
def home(): 
    return render_template('home.html') 

@app.route('/doctors') 
def doctorsRoute(): 
    doctores= request.cookies.get('doctores') 
    ip= request.cookies.get('ip')
    return render_template('doctors.html', tipo= doctores, userIp= ip)

@app.route('/services') 
def servicesRoute(): 
    servicios= request.cookies.get('servicios') 
    ip= request.cookies.get('ip')
    return render_template('services.html', tipo= servicios, userIp= ip)  

@app.route('/about') 
def abaoutRoute(): 
    Informacion= request.cookies.get('Informacion') 
    ip= request.cookies.get('ip')
    return render_template('about.html', tipo= Informacion, userIp= ip) 

@app.route('/contact')
def contactRoute(): 
    contactos= request.cookies.get('contactos') 
    ip= request.cookies.get('ip')
    return render_template('contact.html', tipo= contactos, userIp= ip) 
