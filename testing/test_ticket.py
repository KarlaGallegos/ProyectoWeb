import model.package_model.Ticket_Turno as Ticket

# Crea una instancia de Ticket_Turno con valores
obj_ticket = Ticket.Ticket_Turno(4, 123, '123', '1', 1, 2)

# Inserta el ticket en la base de datos
resultado_insercion = obj_ticket.insertar_ticket(obj_ticket)

if resultado_insercion == "1":
    print("El ticket se ha insertado correctamente.")
    
    # Después de insertar, obtén la lista actualizada de tickets
    lista_tickets = obj_ticket.obtener_ticket()
    
    if lista_tickets is not None:
        for x in lista_tickets:
            print(x)
    else:
        print("No se encontraron datos de nivel educativo")
else:
    print("Hubo un error al insertar el ticket.")