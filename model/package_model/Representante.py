import model.package_model.Database as Database
import pymysql
from flask import jsonify
class Representante:
    def __init__(self, id_representante, nombre_representante, celular, telefono,email):
        self.__id_representante=id_representante
        self.__nombre_representante=nombre_representante
        self.__celular=celular
        self.__telefono=telefono
        self.__email=email
    
    @staticmethod    
    def existe_representante(nombre_representante):
        conexion = conexion = Database.Database()
        Representante = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT count(*) as ex FROM REPRESENTANTE WHERE NOMBRE_REPRESENTANTE = %s", nombre_representante)
            Representante = cursor.fetchone()
        conexion.conn.close() 
        return Representante[0]    
    
    def insertar_representante(self, obj_rep):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO REPRESENTANTE(ID_REPRESENTANTE,NOMBRE_REPRESENTANTE,CELULAR,TELEFONO,EMAIL) VALUES (%s, %s, %s, %s, %s)"
                vals=(obj_rep.__id_representante,obj_rep.__nombre_representante, obj_rep.__celular,obj_rep.__telefono,obj_rep.__email)
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
    
    def eliminar_representante(self,id_representante):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM REPRESENTANTE WHERE ID_REPRESENTANTE = %s", (id_representante))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_representante(self, obj_rep ):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected = cursor.execute("UPDATE REPRESENTANTE SET NOMBRE_REPRESENTANTE = %s, CELULAR = %s, TELEFONO = %s, EMAIL = %s WHERE ID_REPRESENTANTE = %s",
        (obj_rep.__nombre_representante, obj_rep.__celular, obj_rep.__telefono, obj_rep.__email, id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_representante(self):
        conexion = Database.Database()
        representantes= []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM REPRESENTANTE")
            representantes = cursor.fetchall()
        conexion.conn.close()
        return representantes
    
    def obtener_representante_por_id(id):
        conexion = conexion = Database.Database()
        representante = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT * FROM REPRESENTANTE WHERE ID_REPRESENTANTE = %s", (id))
            representante = cursor.fetchone()
        conexion.conn.close()
        return representante      