import sqlite3
from datetime import date
from clases import Productos



conexion = sqlite3.connect('./Bases_datos/Base')
try:
        cursor=conexion.cursor()
        cursor.execute('''
            CREATE TABLE producto(nombre varchar(200), precio varchar(200),tienda varchar(50), imagen varchar(500),url varchar(500), fechaCarga date)
        ''')
except Exception as ex:
    print(ex)


today = date.today()

def insert(Productos):
    try:
        conexion = sqlite3.connect('./Bases_datos/Base')
        cursor = conexion.cursor()
        instruccion = f"INSERT INTO producto VALUES ('{Productos.producto}','{Productos.precio}','{Productos.tienda}','{Productos.imagen}','{Productos.url}','{today}')"
        cursor.execute(instruccion)
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()


def select(producto):
    objeto = []
    objetoProducto = []
    try:
        conexion = sqlite3.connect('./Bases_datos/Base')
        cursor = conexion.cursor()
        instruccion = f"""
        select nombre, precio, tienda, imagen,url from producto where nombre like '%{producto}%'
        """
        cursor.execute(instruccion)
        row = cursor.fetchall()

        for x in range(0, len(row)):
            objeto.append(row[x])

        for y in range(0, len(row)):
            p = Productos(row[y][0],row[y][1],row[y][2],row[y][3],row[y][4])
            objetoProducto.append(p)

        return objetoProducto
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()

def limpiarData(fecha):
    try:
        conexion = sqlite3.connect('./Bases_datos/Base')
        cursor = conexion.cursor()
        instruccion = f"""
                delete from producto where fechaCarga like '%{fecha}%'
                """
        cursor.execute(instruccion)
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()