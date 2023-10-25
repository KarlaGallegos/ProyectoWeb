import model.package_model.Database as Database
class Asunto():
    def __init__(self,id_asunto='',descripcion_asunto=''):
        self.__id_asunto=id_asunto
        self.__descripcion_asunto=descripcion_asunto

    def obtener_asuntos(self):
        conexion = Database.Database()
        asuntos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_ASUNTO,DESCRIPCION_ASUNTO FROM ASUNTO")
            asuntos = cursor.fetchall()
        conexion.conn.close()
        return asuntos
    

    def obtener_asunto_por_id(self,id):
        conexion = conexion = Database.Database()
        asunto = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_ASUNTO,DESCRIPCION_ASUNTO FROM ASUNTO WHERE ID_ASUNTO= %s",(id)) 
            asunto = cursor.fetchone()
            conexion.conn.close()
            return asunto  