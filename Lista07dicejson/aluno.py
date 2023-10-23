import json
class Aluno:
  def __init__(self, id, nome, matricula, nasc):
    self.__id = id
    self.__nome = nome
    self.__matricula = matricula
    self.__nasc = nasc
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_matricula(self): return self.__matricula
  def get_nasc(self): return self.__nasc
  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_matricula(self, matricula): self.__matricula = matricula
  def set_nasc(self, nasc): self.__nasc = nasc
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__matricula} - {self.__nasc}"

class NAluno:
  __alunos = []         # lista de alunos inicia vazia
  @classmethod
  def inserir(cls, obj):
    NAluno.abrir()
    id = 0 # encontrar o maior id já usado
    for aluno in cls.__alunos:
      if aluno.get_id() > id: id = aluno.get_id()
    obj.set_id(id + 1)
    cls.__alunos.append(obj)  # insere um aluno (obj) na lista
    NAluno.salvar()
    
  @classmethod
  def listar(cls):
    NAluno.abrir()    
    return cls.__alunos       # retorna a lista de alunos
  @classmethod
  def listar_id(cls, id):
    NAluno.abrir()
    for aluno in cls.__alunos:
      if aluno.get_id() == id: return aluno
    return None
    
  @classmethod
  def atualizar(cls, obj):
    NAluno.abrir()
    aluno = cls.listar_id(obj.get_id())
    aluno.set_nome(obj.get_nome())
    aluno.set_matricula(obj.get_matricula())
    aluno.set_nasc(obj.get_nasc())
    NAluno.salvar()
    
  @classmethod
  def excluir(cls, obj):
    NAluno.abrir()
    aluno = cls.listar_id(obj.get_id())
    cls.__alunos.remove(aluno)    
    NAluno.salvar()
    
  @classmethod
  def abrir(cls):
    try:
      cls.__alunos = []
      with open("alunos.json", mode="r") as f:
        s = json.load(f)
        for aluno in s:
          a = Aluno(aluno["_Aluno__id"], aluno["_Aluno__nome"],
                    aluno["_Aluno__matricula"], aluno["_Aluno__nasc"])
          cls.__alunos.append(a)
    except FileNotFoundError:
      pass
      
  @classmethod
  def salvar(cls):
    with open("alunos.json", mode="w") as f:
      json.dump(cls.__alunos, f, default=vars)


class UI:
  @classmethod
  def Main(cls):
    op = 0
    while(op != 99):
      op = UI.Menu(cls)
      if op == 1: UI.AlunoInserir()
      if op == 2: UI.AlunoListar()
      if op == 3: UI.AlunoAtualizar()
      if op == 4: UI.AlunoExcluir()
  def Menu(cls):
    print("1-Inserir aluno, 2-Listar aluno, 3-Atualizar aluno, 4-Excluir aluno, 99-Sair")
    return int(input())

  @classmethod
  def AlunoInserir(cls):
    # id = int(input("Id: "))
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    nasc = input("Data de nascimento: ")
    aluno = Aluno(0, nome, matricula, nasc)
    NAluno.inserir(aluno)

  @classmethod
  def AlunoListar(cls):
    for aluno in NAluno.listar():
      print(aluno)

  @classmethod
  def AlunoAtualizar(cls):
    UI.AlunoListar()
    id = int(input("Id do aluno a ser atualizado: "))
    nome = input("Novo nome: ")
    matricula = input("Nova matrícula: ")
    nasc = input("Nova data de nascimento: ")
    aluno = Aluno(id, nome, matricula, nasc)
    NAluno.atualizar(aluno)   

  @classmethod
  def AlunoExcluir(cls):
    UI.AlunoListar()
    id = int(input("Id do aluno a ser excluído: "))
    aluno = Aluno(id, "", "", "")
    NAluno.excluir(aluno)


UI.Main()
      

  


