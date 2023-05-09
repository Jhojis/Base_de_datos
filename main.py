import datetime
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
        
file.close()

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
            fecha = base_datos.get("fechas")
            for i in range(0, len(muni)):
                print(f"{i+1}. {muni[i]}")
            print(f"{len(muni)+1}. Volver al menu principal")
            opcion_operador1 = int(input("Selecciona un municipio: "))
            if opcion_operador1 == len(muni)+1:
                break
            else:
                while True:
                    print(u.dUser(muni[opcion_operador1-1], base_datos, "estaciones"))
                    print(f"{len(muni)+1}. Volver a seleccionar municipio")
                    opcion_operador2 = int(input("Selecciona la estacion: "))
                    if opcion_operador2 == len(muni)+1:
                        break
                    else:
                        menu2 = int(input("1. Mostrar medidas\n2. Ingresar medidas\n"))
                        if menu2 == 1:
                            for i in fecha:
                                if str(opcion_operador2) in i:
                                    encabezado = ['Fecha','Estacion','Variables']
                                    u.imprimir_tabla([i], 25, encabezado)
                                elif int(opcion_operador2) > len(fecha):
                                    print("No hay informacion para la estacion seleccionada.")
                                    break
                        elif menu2 == 2:
                            pm10 = u.valVariables(Vmin=0,Vmax=100,variable='PM10')
                            pm25 = u.valVariables(Vmin=0,Vmax=200,variable='PM25')
                            temp = u.valVariables(Vmin=-20,Vmax=50,variable='Temperatura')
                            hume = u.valVariables(Vmin=0,Vmax=100,variable='Humedad')
                            fecha_actual = datetime.datetime.now()
                            fecha_actual_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
                            lines_variables = '{fecha};{num};{{{PM10},{PM25},{temp},{hume}}}\n'.format(fecha=fecha_actual_str, num=len(fecha)+1, PM10=pm10,PM25=pm25,temp=temp,hume=hume)
                            u.write_txt('registros_.txt', lines_variables)
                    break
                
    elif u.dUser(documento, base_datos, "usuario") == "Administrador":
        esta = base_datos.get("estaciones")
        muni = base_datos.get("municipios")
        opcion_admin1 = input("1. Gestionar estaciones\n2. Gestionar usuario\n3. Depuración de registros inconsistentes en la base de datos\n4. Volver al menu inicial\n")
        if opcion_admin1 == "1":
            opcion_admin2 = input("1. Crear estacion\n2. Editar estacion\n3. Eliminar estacion\n")
            if opcion_admin2 == "1":
                nombre_estacion = input("Ingresa el nombre de la estacion: ")
                for i in range(0, len(muni)):
                    print(f"{i+1}. {muni[i]}")
                opcion_admin_municipio = int(input("Selecciona un municipio: "))
                lines_estacion = '{num},{nombre_estacion},{municipio}\n'.format(num=len(esta)+1, nombre_estacion=nombre_estacion, municipio=muni[opcion_admin_municipio-1])
                u.write_txt('registros_.txt', lines_estacion)
            elif opcion_admin2 == "2":
                u.imprimir_tabla([esta], 30)
                selec_estacion = input("Selecciona la estacion a editar: ")
                estacion = u.dUser(selec_estacion, base_datos, "estaciones")
                print(estacion)
                linea_str = f"{estacion[0]},{estacion[1]},{estacion[2]}"
                print(linea_str)
                u.edit("registros_.txt", linea_str)
                nueva_estacion = input("Ingrese el nombre de la nueva estacion: ")
                for i in range(0, len(muni)):
                    print(f"{i+1}. {muni[i]}")
                opcion_admin_municipio = int(input("Selecciona un municipio: "))
                lines_estacion = '{num},{nombre_estacion},{municipio}\n'.format(num=selec_estacion, nombre_estacion=nueva_estacion, municipio=muni[opcion_admin_municipio-1])
                u.write_txt('registros_.txt', lines_estacion)
                