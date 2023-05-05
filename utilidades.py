# -*- coding: utf-8 -*-
from datetime import datetime

def sepWords(palabras,separador):
    word=''
    words=[]
    for i in palabras:
      word+=i
      if i== separador:
        words.append(word[:-1])
        word=''
    
    if '\n' in word:
        words.append(word[:-1])
    else:
      words.append(word)    
    return  words 

def validar_nombre(nombre):
    '''
    Valida nombre válido (solo letras y espacios)
    Argumentos:
        nombre: String a validar
    return -> Boolean (True or False) si es valido o no
    '''
    for i in range(0, len(nombre)):
        if nombre[i].isdigit():
            es = False
            break
        else:
            es = True
            continue
    return es
def validar_documento(documento):
    '''
    Valida un número de documento. Debe contener 10 caracteres, todos numéricos.
    
    Argumentos:
        documento: string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    if len(documento) == 10:
        for i in range(0, len(documento)):
            if documento[i].isdigit():
                es = True
                continue
            else:
                es = False
                break
        return es
    else:
        return False
    
def validar_datos(documento, base_datos):
    datos = base_datos.get("usuario")
    cont = False
    for i in datos:
        if documento in i:
            cont = True
            break
    return cont

def validar_password(password, base_datos, documento):
    datos = base_datos.get("usuario")
    cont = False
    for i in datos:
        if documento in i:
            if password in i:
                cont = True
                break
    return cont
def dUser(documento, base_datos, llave):
    datos = base_datos.get(llave)
    for i in datos:
        if llave == "usuario":
            if documento in i:
                return i[-1]
        elif llave == "estaciones":
            if documento in i:
                print(i[:-1])

def write_txt(filename, lines):
    with open(filename, 'a') as f:
        f.writelines(lines)
    return (print("archivo_modificado"))
    
def validar_fecha(fecha):
    '''
    Valida que un string corresponda a una fecha válida (con formato yyyy-mm-dd).
    
    Argumentos:
        fecha -> string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def limpiar_pantalla():
    '''
    Imprime varias líneas en blanco, para dar la ilusión 
    de limpiar la pantalla
    '''
    print('\n'*20)

def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
    '''
    def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        se: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)
        
    def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        # Imprimir celda
        if type(texto) == type(0.0):
            #print(texto)
            texto = '{:^7.2f}'.format(texto)
            #print(type(texto), texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
    def imprimir_fila(fila):
        '''
        fila: Lista con los textos de las celdas de la fila
        '''
        impresos = []   
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto)//(ancho[i]-4)
            if len(texto)%(ancho[i]-4) != 0:
                alto1+=1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            print('| ',end='')
            for j in range(len(fila)):
                relleno = ancho[j]-3
                if j == len(fila)-1:
                    relleno = ancho[j] -4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' |')
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' | ',end='')   
    if not len(tabla) > 0:
        return
    if not type(tabla[0]) is list:
        return
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho+3]*ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i]+=3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado != None:
        dividir_fila(ancho,'=')
        imprimir_fila(encabezado)
        dividir_fila(ancho,'=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)

def valVariables(Vmin,Vmax,variable):
    while True:
        try:
            variables = float(input(f"Ingresa el valor sensado para la varible {variable}: ".format(variable=variable)))

            if variables >= Vmin and variables <= Vmax:
                print(f"{variable}: {variables}".format(variable = variables))
                
                return variables
            else:
                print(f"Valor invalido para {variable}".format(variable=variable))

        except:
            print("Valor invalido")
            continue
