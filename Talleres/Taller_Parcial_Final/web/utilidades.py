importar  pandas  como  pd 

def  leerArchivo ( nombreArchivo ):
    diccionario =  pd . read_csv ( nombreArchivo , encoding =  'UTF-8' , header = 0 , delimiter = ';' ). to_dict ()
    volver  diccionario

def  validatePassword ( diccionario , userIn , passwordIn ):
    usuarios =  lista ( diccionario [ 'usuario' ]. valores ())
    contraseñas =  lista ( diccionario [ ' contraseña ' ]. valores ())
    salida  =  ''
    si  userIn  no está  en  usuarios :
        salida  =   'Usuario no registrado'

    otra cosa :
        posicion  =  usuarios . índice ( userIn )
        originalPsw  =  str ( contraseñas [ posicion ])

        si ( originalPsw  ==  passwordIn ):
            salida  =  Verdadero
        otra cosa :
            salida  =  Falso

     salida de regreso

def  saveUser ( originalDict , nombreArchivo , user , psw ):
    listaNombres  =  lista ( originalDict [ 'usuario' ]. valores ())
    listaNombres . añadir ( usuario )
    listaPsw  =   lista ( originalDict [ 'pasar' ]. valores ())
    listaPsw . añadir ( psw )
    originalDict [ 'usuario' ] =  listaNombres
    originalDict [ 'pass' ] =  listaPsw
    dataFrameUser  =  pd . DataFrame ( originalDict )
    dataFrameUser . to_csv ( nombreArchivo , index =  False , sep = ';' )
    regresar  Ninguno