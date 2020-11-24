desde el  matraz  import  Flask , request , make_response , redirect , render_template , url_for

# se crea un objeto del tipo app
aplicación  =  Frasco ( __nombre__ )

@ aplicación . manejador de errores ( 404 )
def  not_found ( error ):
    return  render_template ( '404.html' )


@ aplicación . ruta ( '/' )
def  baseRoute ():
    return  redirect ( url_for ( 'iniciar sesión' ))

@ aplicación . ruta ( '/ casa' )
def  hogar ():
    return  render_template ( 'inicio.html' )

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