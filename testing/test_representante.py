import model.package_model.Representante as Representante

# Crea una instancia de Ticket_Turno con valores
obj_representante = Representante.Representante(1, '123', 'John Doe', 'ABC123', 2)

# Inserta el ticket en la base de datos
resultado_insercion = obj_representante.insertar_representante(obj_representante)

if resultado_insercion == "1":
    print("El ticket se ha insertado correctamente.")
    
    # Después de insertar, obtén la lista actualizada de tickets
    lista_tickets = obj_representante.obtener_representante()
    
    if lista_tickets is not None:
        for x in lista_tickets:
            print(x)
    else:
        print("No se encontraron datos de nivel educativo")
else:
    print("Hubo un error al insertar el ticket.")