import model.package_model.Alumno as Alumno

# Crea una instancia de Ticket_Turno con valores
obj_alumno = Alumno.Alumno('1', '123', 'John Doe', 'ABC123', 2)

# Inserta el ticket en la base de datos
resultado_insercion = obj_alumno.insertar_alumno(obj_alumno)

if resultado_insercion == "1":
    print("El ticket se ha insertado correctamente.")
    
    # Después de insertar, obtén la lista actualizada de tickets
    lista_tickets = obj_alumno.obtener_alumno()
    
    if lista_tickets is not None:
        for x in lista_tickets:
            print(x)
    else:
        print("No se encontraron datos de nivel educativo")
else:
    print("Hubo un error al insertar el ticket.")