import sqlite3 as sQ
Conexion = sQ.connect("BaseDatosAudio.db")
Cursor = Conexion.cursor()
Cursor.execute("""CREATE TABLE Reconocimientos(NVOZ INTEGER PRIMARY KEY, VozTexto TEXT, GrabacionWB BLOB)""")
Conexion.commit()
Conexion.close()