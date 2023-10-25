import model.package_model.Asunto as Asunto
obj_asunto = Asunto.Asunto()
lista_asuntos = obj_asunto.obtener_asuntos()
 
if lista_asuntos!=None:
    for x in lista_asuntos:
        print(x)
else:
    print("No se encontraron datos de asunto")