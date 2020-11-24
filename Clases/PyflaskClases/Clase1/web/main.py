desde el  matraz  import  Flask , request , make_response , redirect ,   render_template , url_for
#se crea un objeto tipo app
aplicación =  Frasco ( __nombre__ )

@ aplicación . manejador de errores ( 404 ) 
def  not_found ( error ):
    return  render_template ( 404 )

@ aplicación . ruta ( '/' ) 
def  hogar ():
    user_ip  =  solicitud . remote_addr
    respuesta =  make_response ( redireccionar ( 'hola' ))
    respuesta . set_cookie ( 'ip' , user_ip )
    respuesta . set_cookie ( 'neko' , 'miau' )
     respuesta de retorno 

@ aplicación . ruta ( '/ hola' )
def  helloRoute ():
    neko =  solicitud . galletas . obtener ( 'neko' )
    ip =  solicitud . galletas . obtener ( 'ip' )
    return  render_template ( 'hola.html' , mascota =  neko , userIp =  ip )

@ aplicación . ruta ( '/ hey' )
def  heyRoute ():
    return  render_template ( 'hey.html' )


if  __name__  ==  '__main__' :
    aplicación . correr () 