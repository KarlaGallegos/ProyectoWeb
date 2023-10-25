import model.package_model.Database as Database
import pymysql
from flask import jsonify
class Alumno:
    def __init__(self, curp_alumno, nombre_alumno, paterno, materno,id_nivel):
        self.__curp_alumno=curp_alumno
        self.__nombre_alumno=nombre_alumno
        self.__paterno=paterno
        self.__materno=materno
        self.__id_nivel=id_nivel
    
    @staticmethod    
    def existe_alumno(curp_alumno):
        conexion = conexion = Database.Database()
        Alumno = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT count(*) as ex FROM Alumno WHERE CURP_ALUMNO = %s", curp_alumno)
            Alumno = cursor.fetchone()
        conexion.conn.close() 
        return Alumno[0]    
    
    def insertar_alumno(self, obj_alu):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO ALUMNO(CURP_ALUMNO,NOMBRE_ALUMNO,PATERNO,MATERNO,ID_NIVEL) VALUES (%s, %s, %s, %s, %s)"
                vals=(obj_alu.__curp_alumno,obj_alu.__nombre_alumno, obj_alu.__paterno,obj_alu.__materno,obj_alu.__id_nivel)
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
    
    def eliminar_alumno(self,curp_alumno):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM ALUMNO WHERE CURP_ALUMNO = %s", (curp_alumno))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_alumno(self, obj_alu ):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("UPDATE ALUMNO SET NOMBRE_ALUMNO = %s, PATERNO = %s, MATERNO = %s,  ID_NIVEL=%s WHERE CURP_ALUMNO = %s",
                       obj_alu.__nombre_alumno, obj_alu.__paterno, obj_alu.__materno,obj_alu.__id_nivel)
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_alumno(self):
        conexion = Database.Database()
        alumnos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM ALUMNO")
            alumnos = cursor.fetchall()
        conexion.conn.close()
        return alumnos
    
    def obtener_alumno_por_curp(curp):
        conexion = conexion = Database.Database()
        alumno = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT * FROM ALUMNO WHERE CURP_ALUMNO = %s", (curp))
            alumno = cursor.fetchone()
        conexion.conn.close()
        return alumno      