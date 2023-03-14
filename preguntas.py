"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
#importar la libreria necesaria para leer un CSV
import csv

#defino la función que me va a leer el CSV y lo deto y giardo en una lista
def leer_archivo():
    data=[]

    with open ("data.csv", newline='') as f:
        contenido = csv.reader(f, delimiter=" ")
        for row in contenido:
            data.append(row[0].split("\t"))
    return data

data = leer_archivo()

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_segunda_fila=0
    for fila in data:
        suma_segunda_fila=suma_segunda_fila+int(fila[1])
    return suma_segunda_fila


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    contadorA,contadorB,contadorC,contadorD,contadorE=0,0,0,0,0
    for fila in data:
        if fila[0]=="A":
            contadorA+=1
        elif fila[0]=="B":
            contadorB+=1
        elif fila[0]=="C":
            contadorC+=1
        elif fila[0]=="D":
            contadorD+=1
        else:
            contadorE+=1
    lista_tuplas=[("A",contadorA),("B",contadorB),("C",contadorC),("D",contadorD),("E",contadorE)]
    return lista_tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    sumaA,sumaB,sumaC,sumaD,sumaE=0,0,0,0,0
    for fila in data:
        if fila[0]=="A":
            sumaA+=int(fila[1])
        elif fila[0]=="B":
            sumaB+=int(fila[1])
        elif fila[0]=="C":
            sumaC+=int(fila[1])
        elif fila[0]=="D":
            sumaD+=int(fila[1])
        else:
            sumaE+=int(fila[1])
    lista_tuplas=[("A",sumaA),("B",sumaB),("C",sumaC),("D",sumaD),("E",sumaE)]
    return lista_tuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    contador1,contador2,contador3,contador4,contador5,contador6,contador7,contador8,contador9,contador10,contador11,contador12=0,0,0,0,0,0,0,0,0,0,0,0
    fechas=[]
    for fila in data:
        fechas.append((fila[2].split("-")))
    for meses in fechas:
        if meses[1]=="01":
            contador1+=1
        elif meses[1]=="02":
            contador2+=1
        elif meses[1]=="03":
            contador3+=1
        elif meses[1]=="04":
            contador4+=1
        elif meses[1]=="05":
            contador5+=1
        elif meses[1]=="06":
            contador6+=1
        elif meses[1]=="07":
            contador7+=1
        elif meses[1]=="08":
            contador8+=1
        elif meses[1]=="09":
            contador9+=1
        elif meses[1]=="10":
            contador10+=1
        elif meses[1]=="11":
            contador11+=1
        else:
            contador12+=1
    conteo_meses=[("01",contador1),("02",contador2),("03",contador3),("04",contador4),("05",contador5),("06",contador6),("07",contador7),("08",contador8),("09",contador9),("10",contador10),("11",contador11),("12",contador12)]
    return conteo_meses


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letraA, letraB, letraC, letraE, letraD =[],[],[],[],[]
    for fila in data:
        if fila[0]=="A":
            letraA.append(int(fila[1]))
        elif fila[0]=="B":
            letraB.append(int(fila[1]))
        elif fila[0]=="C":
            letraC.append(int(fila[1]))
        elif fila[0]=="D":
            letraD.append(int(fila[1]))
        else:
            letraE.append(int(fila[1]))
    tuplas_mayores_menores=[("A",max(letraA),min(letraA)),
    ("B",max(letraB),min(letraB)),("C",max(letraC),min(letraC)),("D",max(letraD),min(letraD)),("E",max(letraE),min(letraE))]
    return tuplas_mayores_menores


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    diccionarios,list_aaa,list_bbb,list_ccc,list_ddd,list_eee,list_fff,list_ggg,list_hhh,list_iii,list_jjj=[],[],[],[],[],[],[],[],[],[],[]
    for fila in data:
        lista_diccionarios=fila[4].split(",")
        for dic in lista_diccionarios:
            diccionarios.append(dic)
    for i in diccionarios:
        if i[0:3]=="aaa":
            list_aaa.append(int(i[4:]))
        elif i[0:3]=="bbb":
            list_bbb.append(int(i[4:]))
        elif i[0:3]=="ccc":
            list_ccc.append(int(i[4:]))
        elif i[0:3]=="ddd":
            list_ddd.append(int(i[4:]))
        elif i[0:3]=="eee":
            list_eee.append(int(i[4:]))
        elif i[0:3]=="fff":
            list_fff.append(int(i[4:]))
        elif i[0:3]=="ggg":
            list_ggg.append(int(i[4:]))
        elif i[0:3]=="hhh":
            list_hhh.append(int(i[4:]))
        elif i[0:3]=="iii":
            list_iii.append(int(i[4:]))
        else:
            list_jjj.append(int(i[4:]))
    dic_ordenados=[("aaa",min(list_aaa),max(list_aaa)),("bbb",min(list_bbb),max(list_bbb)),("ccc",min(list_ccc),max(list_ccc)),("ddd",min(list_ddd),max(list_ddd)),("eee",min(list_eee),max(list_eee)),("fff",min(list_fff),max(list_fff)),("ggg",min(list_ggg),max(list_ggg)),("hhh",min(list_hhh),max(list_hhh)),("iii",min(list_iii),max(list_iii)),("jjj",min(list_jjj),max(list_jjj))]
    return dic_ordenados


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    list0,list1,list2,list3,list4,list5,list6,list7,list8,list9=[],[],[],[],[],[],[],[],[],[]
    for fila in data:
        if fila[1]=="0":
            list0.append(fila[0])
        elif fila[1]=="1":
            list1.append(fila[0])
        elif fila[1]=="2":
            list2.append(fila[0])
        elif fila[1]=="3":
            list3.append(fila[0])
        elif fila[1]=="4":
            list4.append(fila[0])
        elif fila[1]=="5":
            list5.append(fila[0])
        elif fila[1]=="6":
            list6.append(fila[0])
        elif fila[1]=="7":
            list7.append(fila[0])
        elif fila[1]=="8":
            list8.append(fila[0])
        else:
            list9.append(fila[0])
    columnas0_1=[(0,list0),(1,list1),(2,list2),(3,list3),(4,list4),(5,list5),(6,list6),(7,list7),(8,list8),(9,list9)]
    return columnas0_1


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    list0,list1,list2,list3,list4,list5,list6,list7,list8,list9=[],[],[],[],[],[],[],[],[],[]
    for fila in data:
        if fila[1]=="0":
            list0.append(fila[0])
        elif fila[1]=="1":
            list1.append(fila[0])
        elif fila[1]=="2":
            list2.append(fila[0])
        elif fila[1]=="3":
            list3.append(fila[0])
        elif fila[1]=="4":
            list4.append(fila[0])
        elif fila[1]=="5":
            list5.append(fila[0])
        elif fila[1]=="6":
            list6.append(fila[0])
        elif fila[1]=="7":
            list7.append(fila[0])
        elif fila[1]=="8":
            list8.append(fila[0])
        else:
            list9.append(fila[0])
    ordenados_sin_duplicados=[(0,sorted(list(set(list0)))),(1,sorted(list(set(list1)))),(2,sorted(list(set(list2)))),(3,sorted(list(set(list3)))),(4,sorted(list(set(list4)))),(5,sorted(list(set(list5)))),(6,sorted(list(set(list6)))),(7,sorted(list(set(list7)))),(8,sorted(list(set(list8)))),(9,sorted(list(set(list9))))]
    return ordenados_sin_duplicados


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    diccionario_retorno={"aaa":0,"bbb":0,"ccc":0,"ddd":0,"eee":0,"fff":0,"ggg":0,"hhh":0,"iii":0,"jjj":0}
    diccionarios=[]
    for fila in data:
        lista_diccionarios=fila[4].split(",")
        for dic in lista_diccionarios:
            dic=dic.split(":")
            diccionarios.append(dic[0])
    for i in diccionarios:
        if i[0:3]=="aaa":
            diccionario_retorno['aaa']+=1
        elif i[0:3]=="bbb":
            diccionario_retorno['bbb']+=1
        elif i[0:3]=="ccc":
            diccionario_retorno['ccc']+=1
        elif i[0:3]=="ddd":
            diccionario_retorno['ddd']+=1
        elif i[0:3]=="eee":
            diccionario_retorno['eee']+=1
        elif i[0:3]=="fff":
            diccionario_retorno['fff']+=1
        elif i[0:3]=="ggg":
            diccionario_retorno['ggg']+=1
        elif i[0:3]=="hhh":
            diccionario_retorno['hhh']+=1
        elif i[0:3]=="iii":
            diccionario_retorno['iii']+=1
        else:
            diccionario_retorno['jjj']+=1
    return diccionario_retorno


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista_tuplas=[]
    for fila in data:
        columna4=fila[3].split(",")
        columna5=fila[4].split(",")
        lista_tuplas.append((fila[0],len(columna4),len(columna5)))
    return lista_tuplas


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    diccionario_suma={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}
    for fila in data:
        letras=fila[3].split(",")
        for letra in letras:
            if letra == "a":
                diccionario_suma['a']+=int(fila[1])
            elif letra == "b":
                diccionario_suma['b']+=int(fila[1])
            elif letra == "c":
                diccionario_suma['c']+=int(fila[1])
            elif letra == "d":
                diccionario_suma['d']+=int(fila[1])
            elif letra == "e":
                diccionario_suma['e']+=int(fila[1])
            elif letra == "f":
                diccionario_suma['f']+=int(fila[1])
            else:
                diccionario_suma['g']+=int(fila[1])
    return diccionario_suma


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_columna5={"A":0,"B":0,"C":0,"D":0,"E":0}
    for fila in data:
        diccionarios=fila[4].split(",")
        suma_diccionarios=0
        for diccionario in diccionarios:
            suma_diccionarios+=int(diccionario[4:])
        if fila[0]=="A":
            suma_columna5['A']+=suma_diccionarios
        elif fila[0]=="B":
            suma_columna5['B']+=suma_diccionarios
        elif fila[0]=="C":
            suma_columna5['C']+=suma_diccionarios
        elif fila[0]=="D":
            suma_columna5['D']+=suma_diccionarios
        else:
            suma_columna5['E']+=suma_diccionarios
    return suma_columna5
