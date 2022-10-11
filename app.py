from flask import Flask, render_template, request, url_for
from Bases_datos.conexion_sqlite import select

app = Flask(__name__, template_folder='plantillas',static_folder='static')
objeto = []
@app.route('/')
@app.route('/index')
def buscador():
    return render_template('index.html')

@app.route('/addrec', methods= ['POST', 'GET'])
def addrec():
    busqueda = request.form['busqueda']
    msg = ""
    if request.method == 'POST':
        try:
            valorP = select(busqueda)
            msg = valorP
        except:
            pass

        finally:
            return render_template('results.html', msg=msg)
            con.close()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)