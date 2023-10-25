import model.package_model.Database as Database
class Municipio():
    def __init__(self,id_municipio='',nombre_municipio=''):
        self.__id_municipio=id_municipio
        self.__nombre_municipio=nombre_municipio

    def obtener_municipios(self):
        conexion = Database.Database()
        municipios = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_MUNICIPIO,NOMBRE_MUNICIPIO FROM MUNICIPIO")
            municipios = cursor.fetchall()
        conexion.conn.close()
        return municipios

    def obtener_municipio_por_id(self,id):
        conexion = conexion = Database.Database()
        municipio = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_MUNICIPIO,NOMBRE_MUNICIPIO FROM MUNICIPIO WHERE ID_MUNICIPIO= %s",(id)) 
            municipio = cursor.fetchone()
            conexion.conn.close()
            return municipio  