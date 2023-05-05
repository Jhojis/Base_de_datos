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

while True:
    print("   --Menu principal--    ")

    opcion = input("1. Usuario registrado\n2. Usuario visitante\n3. Salir del sistema\n")

    if opcion == "1":
        while True:
            documento = input("Introduce el numero de documento: ")
            if u.validar_documento(documento) == True and u.validar_datos(documento, base_datos) == True:
                while True:
                    password = input("Introduce la contraseña: ")
                    if u.validar_password(password, base_datos, documento) == True and len(password) >= 4:
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
        while True:
            muni = base_datos.get("municipios")
            esta = base_datos.get("fechas")
            for i in range(0, len(muni)):
                print(f"{i+1}. {muni[i]}")
            print(f"{len(muni)+1}. Volver al menu principal")
            opcion_operador1 = int(input("Selecciona un municipio: "))
            if opcion_operador1 == len(muni)+1:
                break
            else:
                print(u.dUser(muni[opcion_operador1-1], base_datos, "estaciones"))
                opcion_operador2 = input("Selecciona la estacion: ")
                menu2 = input("1. Mostrar medidas\n2. Ingresar medidas\n")
                if menu2 == "1":
                    for i in esta:
                        if opcion_operador2 in i:
                            u.imprimir_tabla([i], 25)
                        elif int(opcion_operador2) > len(esta):
                            print("No hay informacion para la estacion seleccionada.")
                            break
                elif menu2 == "2":
                    pm10 = u.valVariables(Vmin=0,Vmax=100,variable='PM10')
                    pm25 = u.valVariables(Vmin=0,Vmax=200,variable='PM25')
                    temp = u.valVariables(Vmin=-20,Vmax=50,variable='Temperatura')
                    hume = u.valVariables(Vmin=0,Vmax=100,variable='Humedad')
                    lines = '{fecha};{num};{PM10},{PM25},{temp},{hume}\n'.format(fecha="2019-04-01 00:00:00", num=len(esta)+1, PM10=pm10,PM25=pm25,temp=temp,hume=hume)
                    u.write_txt('registros_.txt', lines)
        