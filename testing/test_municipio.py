import model.package_model.Municipio as Municipio
obj_municipio = Municipio.Municipio()
lista_municipios = obj_municipio.obtener_municipios()
 
if lista_municipios!=None:
    for x in lista_municipios:
        print(x)
else:
    print("No se encontraron datos de municipio")