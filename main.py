import datetime
import  utilidades as u
file = open('registros_.txt',encoding='utf-8')
contenido=file.readlines()
base_datos=u.base_datos(contenido)
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
                    if u.validar_password(password, base_datos, documento) == True:
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
            
            #fechas = base_datos.get("fechas")
            opcion_admin1 = input("1. Gestionar estaciones\n2. Gestionar usuario\n3. Depuración de registros inconsistentes en la base de datos\n4. Volver al menu inicial\n")
            if opcion_admin1 == "1":
                esta = base_datos.get("estaciones")
                muni = base_datos.get("municipios")
                opcion_admin2 = input("1. Crear estacion\n2. Editar estacion\n3. Eliminar estacion\n")
                if opcion_admin2 == "1":
                    nombre_estacion = input("Ingresa el nombre de la estacion: ")
                    for i in range(0, len(muni)):
                        print(f"{i+1}. {muni[i]}")
                    opcion_admin_municipio = int(input("Selecciona un municipio: "))
                    lines_estacion = '{num},{nombre_estacion},{municipio}\n'.format(num=len(esta)+1, nombre_estacion=nombre_estacion, municipio=muni[opcion_admin_municipio-1])
                    u.write_txt('registros_.txt', lines_estacion)
                elif opcion_admin2 == "2":
                    u.imprimir_tabla(esta, 30)
                    selec_estacion = input("Selecciona la estacion a editar: ")
                    estacion = u.dUser(selec_estacion, base_datos, "estaciones")
                    linea_str = f"{estacion[0]},{estacion[1]},{estacion[2]}"
                    print(linea_str)
                    u.edit("registros_.txt", linea_str)
                    nueva_estacion = input("Ingrese el nombre de la nueva estacion: ")
                    for i in range(0, len(muni)):
                        print(f"{i+1}. {muni[i]}")
                    opcion_admin_municipio = int(input("Selecciona un municipio: "))
                    lines_estacion = '{num},{nombre_estacion},{municipio}\n'.format(num=selec_estacion, nombre_estacion=nueva_estacion, municipio=muni[opcion_admin_municipio-1])
                    u.write_txt('registros_.txt', lines_estacion)
                elif opcion_admin2 == "3":
                    u.imprimir_tabla(esta, 30)
                    selec_estacion = input("Selecciona la estacion a eliminar: ")
                    fecha = u.dUser(selec_estacion, base_datos, "fechas")
                    if len(fecha) == 0:
                        estacion = u.dUser(selec_estacion, base_datos, "estaciones")
                        linea_str = f"{estacion[0]},{estacion[1]},{estacion[2]}"
                        u.edit("registros_.txt", linea_str)
                    else:
                        print("Esta estacion tiene registro de valores asociado a ella, no se puede eliminar.")

            elif opcion_admin1 == "2":
                usuarios = base_datos.get("usuario")
                opcion_admin2 = input("1. Crear usuario\n2. Editar usuario\n3. Eliminar usuario\n")
                if opcion_admin2 == "1":
                    doc = u.creacionUser("documento")
                    nombre = u.creacionUser("nombre")
                    new_password = u.creacionUser("contraseña")
                    rol = u.creacionUser("rol")
                    lines_usuario = '<{doc};{nombre};{password};{rol}>\n'.format(doc=doc, nombre=nombre, password=new_password, rol=rol)
                    u.write_txt("registros_.txt", lines_usuario)

                elif opcion_admin2 == "2":
                    u.imprimir_tabla(usuarios, 30)
                    while True:
                        selec_usuario = input("Introduce el documento del usuario a editar: ")
                        if u.validar_datos(selec_usuario, base_datos) == True and u.validar_documento(selec_usuario) == True:
                            u.edit("registros_.txt", selec_usuario)
                            doc = u.creacionUser("documento")
                            nombre = u.creacionUser("nombre")
                            new_password = u.creacionUser("contraseña")
                            rol = u.creacionUser("rol")
                            lines_usuario = '<{doc};{nombre};{password};{rol}>\n'.format(doc=doc, nombre=nombre, password=new_password, rol=rol)
                            u.write_txt("registros_.txt", lines_usuario)
                            break
                        else:
                            print("Documento no encontrado, intente nuevamente")
                            continue

                elif opcion_admin2 == "3":
                    u.imprimir_tabla(usuarios, 30)
                    while True:
                        selec_usuario = input("Introduce el documento del usuario a eliminar: ")
                        if u.validar_datos(selec_usuario, base_datos) == True and u.validar_documento(selec_usuario) == True:
                            u.edit("registros_.txt", selec_usuario)
                            print("Usuario eliminado con exito.")
                            break
                        else:
                            print("Documento no encontrado, intente nuevamente")
                            continue
                        
            elif opcion_admin1 == "3":
                print("Depuracion de registros iconsistentes")
                with open("registros_.txt", "r", encoding="utf-8") as orig, open("registros_v2.txt", "r", encoding="utf-8") as dup:
                    fecha1 = u.base_datos(orig.readlines())
                    fecha2 = u.base_datos(dup.readlines())
                    fecha1 = fecha1.get("fechas")
                    fecha2 = fecha2.get("fechas")
                    print("Las medidas repetidas son: ")
                    for i, j in zip(fecha1, fecha2):
                        if i == j:
                            print(i)
                    print("Medidas que que aparecen en cualquiera de los dos archivos: ")
                    for i, j in zip(fecha1, fecha2):
                        if i == j:
                            print(i)
                        elif i != j:
                            print(i)
                            print(j)
                        