from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
database_name = "siscov"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:siscov@localhost:5432/' + database_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    municipios = db.relationship('Municipio', backref='estado')

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Municipio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    populacao = db.Column(db.Integer)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'))
    casos = db.relationship('Casos', backref='municipio')

    def __init__(self, id, nome, populacao, estado_id):
        self.id = id
        self.nome = nome
        self.populacao = populacao
        self.estado_id = estado_id

class Casos(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    dataNotificacao = db.Column(db.String(50), nullable=False)
    dataInicioSintomas = db.Column(db.String(50))
    evolucaoCaso = db.Column(db.String(500))
    classificacaoFinal = db.Column(db.String(500))
    municipio_id = db.Column(db.Integer, db.ForeignKey('municipio.id'))

    def __init__(self, id, dataNotificacao, dataInicioSintomas, evolucaoCaso, classificacaoFinal, municipio_id):
        self.id = id
        self.dataNotificacao = dataNotificacao
        self.dataInicioSintomas = dataInicioSintomas
        self.evolucaoCaso = evolucaoCaso
        self.classificacaoFinal = classificacaoFinal
        self.municipio_id = municipio_id

class EstadoSchema(ma.Schema):
    class Meta:
        fields=('id', 'nome')

class RegionSchema(ma.Schema):
    class Meta:
        fields=('id', 'nome')

class CountySchema(ma.Schema):
    class Meta:
        fields=('id', 'nome')