import  utilidades as u
file= open('registros_.txt',encoding='utf-8')
contenido=file.readlines()
base_datos={}
base_datos['usuario']=[]
base_datos['municipios']=[]
base_datos['estaciones']=[]
base_datos['variables']=[]
base_datos['fechas']=[]
for linea in contenido:
    if linea[0]=='<':
        base_datos['usuario']+=[u.sepWords(linea[1:-2],';')]
    elif linea[0]==':':
        string_municipios=linea[1:-1]
        words=u.sepWords(string_municipios,',')
        base_datos['municipios']+=words
    elif 'PM10' in linea:
        base_datos['variables']+=[u.sepWords(linea,';')]
    elif linea[4]=='-':
        base_datos['fechas']+=[u.sepWords(linea,';')]
    else:
        base_datos['estaciones']+=[u.sepWords(linea,',')]
menu = True
while menu == True:
    print("   --Menu principal--    ")

    opcion = input("1. Usuario registrado\n2. Usuario visitante\n3. Salir del sistema\n")

    if opcion == "1":
        while True:
            documento = input("Introduce el numero de documento: ")
            if u.validar_documento(documento) == True and u.validar_datos(documento, base_datos, "usuario") == True:
                while True:
                    password = input("Introduce la contraseña: ")
                    if u.validar_datos(password, base_datos, "usuario") == True and len(password) >= 4:
                        print("Sesion iniciada")
                        break
                    else:
                        print("Contraseña incorrecta, intente nuevamente.")
                        continue
            else:
                print("Documento incorrecto, intente nuevamente.")
                continue
            break  
        
    if u.dUser(documento, base_datos, "usuario") == "Operador":
        muni = base_datos.get("municipios")
        for i in range(0, len(muni)):
            print(f"{i+1}. {muni[i]}")
                
        opcion_operador1 = int(input("Selecciona un municipio: "))
        print(u.dUser(muni[opcion_operador1-1], base_datos, "estaciones"))
    