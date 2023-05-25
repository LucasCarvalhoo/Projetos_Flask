# importando framework's
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 
import sqlite3
from flask_cors import CORS

app = Flask(__name__)

# configurando banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'
app.config['SQLALQUEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)
CORS(app)

# criando as tabelas
from app.models.alunos import Alunos
with app.app_context(): 
    db.create_all()

# criando as rotas
from app.resources.registro_alunos import Index, CriarAluno, PesquisarAlunos, AtualizarAluno, DeletarAluno
api.add_resource(Index, '/')
api.add_resource(CriarAluno, '/criar')
api.add_resource(PesquisarAlunos, '/buscar_alunos')
api.add_resource(AtualizarAluno, '/atualizar')
api.add_resource(DeletarAluno, '/deletar')
