desde el matraz import  Flask , request , make_response , redirect ,   render_template , url_for
#se crea un objeto tipo app
aplicación =  Frasco ( __nombre__ )

@ aplicación . manejador de errores ( 404 ) 
def  not_found ( error ):
    return  render_template ( 404 )

@ aplicación . ruta ( '/' ) 
def  hogar ():

    return  render_template ( 'inicio.html' )

@ aplicación . ruta ( '/ hola' )
def  helloRoute ():
    neko =  solicitud . galletas . obtener ( 'neko' )
    ip =  solicitud . galletas . obtener ( 'ip' )
    return  render_template ( 'hola.html' , mascota =  neko , userIp =  ip )

@ aplicación . ruta ( '/ hey' )
def  heyRoute ():
    return  render_template ( 'hey.html' )

@ aplicación . ruta ( '/ personajes' )
def  personajesRoute ():
    personajes =  solicitud . galletas . get ( 'personajes' )
    ip =  solicitud . galletas . obtener ( 'ip' )
    return  render_template ( 'personajes.html' , tipo =  personajes , userip =  ip   )

@ aplicación . ruta ( '/ lugares' ) 
def  lugaresRoute ():  
    lugares =  solicitud . galletas . get ( 'lugares' )
    ip =  solicitud . galletas . obtener ( 'ip' )
    return   render_template ( 'lugares.html' , tipo =  lugares , userip =  ip )

@ aplicación . route ( '/ login' , métodos  = [ 'POST' , 'GET' ])
def  login ():
    si lo  solicita . método  ==  'POST' :
        nameUser  =  solicitud . forma [ 'nombre' ]
        passUser  =  solicitud . formulario [ 'pasar' ]
        si ( passUser  ==  'hola1234' ):
            return   redirect ( url_for ( 'inicio' ))
        otra cosa :
            volver  'Falló proceso de autenticación'
    otra cosa :
        return  render_template ( 'login.html' )


if  __name__  ==  '__main__' :
    aplicación . correr () 