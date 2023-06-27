import difflib

base_de_datos = {
    'Toyota':['yaris','Rav4'], 
    'Honda':['Civic'], 
    'Kia':['Rio', 'sorento'], 
    'Chevrolet': ['Corvette']
}

def buscarMarca():
    buscador = input("Buscar Marca: ")
    encontrado = False
    
    resultados = difflib.get_close_matches(buscador,base_de_datos.keys())
    if len(resultados) != 0:
        print(buscador,base_de_datos[resultados[0]]) 
        encontrado = True
    
    if not encontrado:
        for marca, modelos in base_de_datos.items():

            resultados = difflib.get_close_matches(buscador,modelos)
            if len(resultados) != 0:
                modelo = "".join(resultados)
                print(f"{marca} {modelo}")
                encontrado = True
                break
    if not encontrado:
        print("No se econtro ni la marca ni el modelo")
    

buscarMarca()