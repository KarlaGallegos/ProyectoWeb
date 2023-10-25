import model.package_model.Database as Database
class Nivel_Educativo():
    def __init__(self,id_nivel='',descripcion_nivel=''):
        self.__id_nivel=id_nivel
        self.__descripcion_nivel=descripcion_nivel

    def obtener_niveles(self):
        conexion = Database.Database()
        niveles = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_NIVEL,DESCRIPCION_NIVEL FROM NIVEL_EDUCATIVO")
            niveles = cursor.fetchall()
        conexion.conn.close()
        return niveles
    

    def obtener_nivel_por_id(self,id):
        conexion = conexion = Database.Database()
        nivel = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_NIVEL,DESCRIPCION_NIVEL FROM NIVEL_EDUCATIVO WHERE ID_NIVEL= %s",(id)) 
            nivel = cursor.fetchone()
            conexion.conn.close()
            return nivel  