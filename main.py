import xml.etree.ElementTree as ET

tree = ET.parse('notas.xml')
root = tree.getroot()


# Insertar una nueva nota.
def insertar(insertarTitulo, insertarTexto):
    nota = ET.Element('nota')
    titulo = ET.SubElement(nota, 'titulo')
    texto = ET.SubElement(nota, 'texto')

    titulo.text = insertarTitulo
    texto.text = insertarTexto

    root.insert(0, nota)

    tree.write('notas.xml')


# Imprimir todas las notas por pantalla.

def imprimir():
    for nota in root.findall('nota'):
        titulo = nota.find('titulo').text
        texto = nota.find('texto').text
        print(titulo)
        print(texto)
        print('')


# Modificar una nota. (título)
def modificarPorTitulo(modificarTituloAntes, modificarTituloDespues):
    for nota in root:
        for sub in nota:
            if sub.tag == 'titulo':
                if nota.find('titulo').text == modificarTituloAntes:
                    for titulo in nota.iter('titulo'):
                        titulo.text = modificarTituloDespues
    tree.write('notas.xml')


# Modificar una nota. (texto)

def modificarPorTexto(modificarTitulo, modificarTexto):
    for nota in root:
        for sub in nota:
            if sub.tag == 'texto':
                if nota.find('texto').text == modificarTitulo:
                    for texto in nota.iter('titulo'):
                        texto.text = modificarTexto
    tree.write('notas.xml')


# Buscar una nota.

def buscar(tituloBuscar):
    for nota in root.findall('nota'):
        titulo = nota.find('titulo').text
        texto = nota.find('texto').text
        if titulo == tituloBuscar:
            print(titulo)
            print(texto)
            print('')


print('******************************************************')
print('Bienvenid@ a tus notas.')

hacer = 'Y'

while hacer != 'N':
    tarea = 0
    print('¿Qué deseas hacer? (Introduzca el número por pantalla)\n'
          '* 1. Insertar una nueva nota.\n'
          '* 2. Imprimir todas las notas por pantalla.\n'
          '* 3. Modificar una nota.\n'
          '* 4. Buscar una nota.')
    print('******************************************************')

    while tarea != 1 and tarea != 2 and tarea != 3 and tarea != 4 and hacer != 'N':
        tarea = int(input())
        if tarea == 1:
            print('Insertar una nueva nota.')
            print('------------------------')
            print('Introduzca el título que deseas ponerle a la nueva nota.')
            tituloInsertar = str(input())
            print('Introduzca el texto de la nueva nota.')
            textoInsertar = str(input())
            insertar(tituloInsertar, textoInsertar)
        elif tarea == 2:
            print('Imprimir todas las notas por pantalla.')
            print('--------------------------------------')
            imprimir()
        elif tarea == 3:
            print('Modificar una nota.')
            print('-------------------')
            print('¿Qué deseas modificar?\n'
                  '* 1. Título\n'
                  '* 2. Texto')
            modificar = 0
            while modificar != 1 and modificar != 2:
                modificar = int(input())
            if modificar == 1:
                print('Introduzca el título que deseas modificar.')
                tituloModificarAntes = str(input())
                print('¿Qué título deseas poner?')
                tituloModificarDespues = str(input())
                modificarPorTitulo(tituloModificarAntes, tituloModificarDespues)
            elif modificar == 2:
                print('Introduzca el título de la nota que deseas modificar su texto.')
                tituloModificar = str(input())
                print('¿Qué texto deseas poner?')
                textoModificar = str(input())
                modificarPorTexto(tituloModificar, textoModificar)
            else:
                print('Error. Introduzca de nuevo')
        elif tarea == 4:
            print('Buscar una nota.')
            print('----------------')
            print('Introduzca el título de la nota que deseas buscar.')
            tituloBuscar = str(input())
            buscar(tituloBuscar)
        else:
            print('Error. Introduzca de nuevo')
    print('¿Deseas hacer otra cosa? Y/N')
    hacer = str(input()).upper()
print('***********************')
print('Has salido de tus notas')
print('***********************')
