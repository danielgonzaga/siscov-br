from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#sql
#dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:siscov@localhost:5432/casos_covid'

#routes

'''@app.route('/')
#renderiza o html passado 
def index():
    return render_template('index.html')
'''
@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route('/teste', methods=['GET'])
def teste():
    if request.method == 'GET':
        #realiza uma consulta aqui
        print("get")

if __name__ == '__main__':
    app.run()