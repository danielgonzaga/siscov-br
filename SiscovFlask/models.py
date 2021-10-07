from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:siscov@localhost:5432/casos_covid'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    municipios = db.relationship('Municipio', backref='estado')

    def __init__(self, nome):
        self.nome = nome

class Municipio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'))
    casos = db.relationship('Casos', backref='municipio')

    def __init__(self, nome, estado_id):
        self.nome = nome
        self.estado_id = estado_id

class Casos(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    dataNotificacao = db.Column(db.String(50), nullable=False)
    dataInicioSintomas = db.Column(db.String(50))
    idade = db.Column(db.Integer)
    condicoes = db.Column(db.String(500))
    evolucaoCaso = db.Column(db.String(500))
    classificacaoFinal = db.Column(db.String(500))
    municipio_id = db.Column(db.Integer, db.ForeignKey('municipio.id'))

    def __init__(self, id, dataNotificacao, dataInicioSintomas, idade, condicoes, evolucaoCaso, classificacaoFinal, municipio_id):
        self.id = id
        self.dataNotificacao = dataNotificacao
        self.dataInicioSintomas = dataInicioSintomas
        self.idade = idade
        self.condicoes = condicoes
        self.evolucaoCaso = evolucaoCaso
        self.classificacaoFinal = classificacaoFinal
        self.municipio_id = municipio_id

class EstadoSchema(ma.Schema):
    class Meta:
        fields=('id', 'nome')
