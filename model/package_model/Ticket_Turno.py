import model.package_model.Database as Database
import pymysql
from flask import jsonify

class Ticket_Turno:
    def __init__(self, id_municipio,numero_turno, nombre_representante, curp_alumno, id_asunto,id_estatus):
        self.__id_municipio=id_municipio
        self.__numero_turno=numero_turno
        self.__nombre_representante=nombre_representante
        self.__curp_alumno=curp_alumno
        self.__id_asunto=id_asunto
        self.__id_estatus=id_estatus
    
    @staticmethod    
    def existe_ticket(id_municipio,numero_turno):
        conexion = conexion = Database.Database()
        ticket = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT count(*) as ex FROM TICKET_TURNO WHERE ID_MUNICIPIO = %s AND NUMERO_TURNO = %s", id_municipio,numero_turno)
            Representante = cursor.fetchone()
        conexion.conn.close() 
        return ticket[0]    
    
    def insertar_ticket(self, obj_tic):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO TICKET_TURNO(ID_MUNICIPIO,NUMERO_TURNO,NOMBRE_REPRESENTANTE,CURP_ALUMNO,ID_ASUNTO,ID_ESTATUS) VALUES (%s, %s, %s, %s, %s, %s)"
                vals=(obj_tic.__id_municipio,obj_tic.__numero_turno,obj_tic.__nombre_representante, obj_tic.__curp_alumno,obj_tic.__id_asunto,obj_tic.__id_estatus)
                #return (query % vals) ver sentencia
                affected=cursor.execute(query,vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
            finally:
                conexion.conn.close() 
    
    def eliminar_ticket(self,id_municipio,numero_turno):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM TICKET_TURNO WHERE ID_MUNICIPIO = %s AND NUMERO_TURNO = %s", (id_municipio,numero_turno))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_ticket(self, obj_tic ):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("UPDATE TICKET_TURNO SET NOMBRE_REPRESENTANTE = %s, CURP_ALUMNO = %s, ID_ASUNTO = %s, ID_ESTATUS=%s WHERE ID_MUNICIPIO = %s AND NUMERO_TURNO = %s",
                       obj_tic.__nombre_representante, obj_tic.__curp_alumno, obj_tic.__id_asunto,obj_tic.__estatus)
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_ticket(self):
        conexion = Database.Database()
        tickets = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM TICKET_TURNO")
            tickets = cursor.fetchall()
        conexion.conn.close()
        return tickets
    
    def obtener_ticket_por_id(id_municipio, numero_turno):
        conexion = Database.Database()
        ticket = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM TICKET_TURNO WHERE ID_MUNICIPIO = %s AND NUMERO_TURNO = %s", (id_municipio, numero_turno))
            ticket = cursor.fetchone()
        conexion.conn.close()
        return ticket
