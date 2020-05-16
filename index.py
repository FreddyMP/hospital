from flask import Flask, request
import pymysql.cursors
from flask_json import FlaskJSON, json_response, JsonError, jsonify
import conex

app = Flask(__name__)
app.config['JSON_ADD_STATUS'] = False
@app.route('/showall/')
def index():
    Lista = conex.cone.cursor()
    Lista.execute("select * from hospital")
    resultados = Lista.fetchall()
    return json_response(data = resultados)    
    cone.close()


@app.route('/showid/<id>') 
def showid(id):
    Lista = conex.cone.cursor()
    Lista.execute(f"select * from hospital where id_hospital = {id}")
    resultados = Lista.fetchall()
    return json_response(data = resultados)    
    cone.close()


@app.route('/create/<nombre>/<rcn_hospital>/<direccion>')
def create(nombre, rcn_hospital, direccion):
    cone = conex.cone
    cone.cursor()
    cone.cursor().execute(f"INSERT INTO hospital (nombre_hospital, rcn_hospital, direccion_hospital) values('{nombre}', '{rcn_hospital}', '{direccion}')")
    cone.commit()
    cone.close()
    return "Registro creado"

@app.route('/update/<id>/<nombre>/<rcn_hospital>/<direccion>')
def update(id,nombre,rcn_hospital,direccion):
    cone = conex.cone
    cone.cursor()
    cone.cursor().execute(f"UPDATE hospital SET nombre_hospital = '{nombre}', rcn_hospital='{rcn_hospital}', direccion_hospital='{direccion}' WHERE id_hospital = {id}")
    cone.commit()
    cone.close()
    return "Registro actualizado"

@app.route('/delete/<id>')
def delete(id):
    dele=conex.cone
    dele.cursor().execute(f" DELETE FROM hospital where id_hospital = {id}")
if __name__ == "__main__":
    app.run(debug=True)
