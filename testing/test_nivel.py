import model.package_model.Nivel_Educativo as NE
obj_nivel = NE.Nivel_Educativo()
lista_niveles = obj_nivel.obtener_niveles()
 
if lista_niveles!=None:
    for x in lista_niveles:
        print(x)
else:
    print("No se encontraron datos de nivel educativo")