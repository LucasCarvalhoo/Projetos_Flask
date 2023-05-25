from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.alunos import  Alunos

# adicionar aluno
argumentos = reqparse.RequestParser()
argumentos.add_argument('cpf', type=str)
argumentos.add_argument('nome', type=str)
argumentos.add_argument('sexo', type=str)
argumentos.add_argument('data_nascimento', type=str)
argumentos.add_argument('idade', type=int)
argumentos.add_argument('av1', type=float)
argumentos.add_argument('av2', type=float)
argumentos.add_argument('media', type=float)

# atualuzar aluno
argumentos_atualizar = reqparse.RequestParser()
argumentos_atualizar.add_argument('cpf', type=str)
argumentos_atualizar.add_argument('nome', type=str)
argumentos_atualizar.add_argument('sexo', type=str)
argumentos_atualizar.add_argument('data_nascimento', type=str)
argumentos_atualizar.add_argument('idade', type=int)
argumentos_atualizar.add_argument('av1', type=float)
argumentos_atualizar.add_argument('av2', type=float)
argumentos_atualizar.add_argument('media', type=float)

#deletar aluno
argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument('cpf', type=str)

class Index(Resource):
    def get(self):
        pass

# metodo cria um novo aluno
class CriarAluno(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            usuario = Alunos(**datas)
            usuario.salvar_alunos()
            return {"message": 'Aluno criado com sucesso!'}, 201

        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

# metodo retorna uma lista de alunos
class PesquisarAlunos(Resource):
    
    def get(self):
        try:
            return {'alunos': [Alunos.json() for Alunos in Alunos.query.all()]}
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

# metodo atualiza as informações do aluno existente
class AtualizarAluno(Resource):

    def put(self):
        try:
            datas = argumentos_update.parse_args()
            atualizar = Alunos.update_survivors(self, datas['id'], 
                                                   datas['name'],
                                                   datas['gender'],
                                                   datas['lat'], 
                                                   datas['lon'])
            return {"message": 'Aluno atualizado com sucesso!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

# metodo deleta um aluno existente
class DeletarAluno(Resource):

    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            atualizar = Alunos.delete_survivors(self, datas['cpf'])
            return {"message": 'Aluno deletado com sucesso!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500