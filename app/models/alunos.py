from app import db

# definição do modelo de dados e mapeamento dos 
# atributos para uma tabela de banco de dados
class Alunos(db.Model):
    __tablename__ = 'alunos'
    __table_args__ = {'sqlite_autoincrement': True}
    cpf = db.Column(db.String(25), primary_key=True)
    nome = db.Column(db.String(100))
    data_nascimento = db.Column(db.String(15))
    sexo = db.Column(db.String(10))
    idade = db.Column(db.Integer)
    av1 = db.Column(db.Float)
    av2 = db.Column(db.Float)
    media = db.Column(db.Float)

    # Esse metodo recebe os atributos sempre que a classe alunos for chamada
    def __init__(self, cpf, nome, sexo, data_nascimento, idade, av1, av2, media):
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.idade = idade
        self.av1 = av1
        self.av2 = av2
        self.media = (av1 + av2 ) / 2 

    # retorna um dicionario com os atributos da classe
    def json(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'sexo': self.sexo,
            'data de nascimento': self.data_nascimento,
            'idade': self.idade,
            'Av1': self.av1,
            'Av2': self.av2,
            'media': self.media
        }

    # salva aluno no nosso banco de dados
    def salvar_alunos(self): # lembrar de usar
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(error)

    # atualiza os atributos do aluno pela chave primaria(cpf), se ele existir
    def atualizar_alunos(self, cpf, nome, sexo, data_nascimento, idade, av1, av2):
        try:
            db.session.query(Alunos).filter(Alunos.cpf==cpf).update(
                {
                "nome": self.nome,
                "sexo": self.sexo,
                "data de nascimento": self.data_nascimento,
                "idade": self.idade,
                "av1": self.av1,
                "av2": self.av2,
                "media": self.media
                }
            )
        except Exception as e:
            print(error)

    # excluir um aluno do banco de dados com base no chave primaria(cpf) se ele existir
    def deletar_alunos(self, cpf):
        try:
            db.session.query(Survivors).filter(Survivors.cpf==cpf).delete()
            db.session.commit()
        except Exception as e:
            print(e)