import json
class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id = id
    self.__descricao = descricao
    self.__valor  = valor
    self.__duracao = duracao
  def get_id(self): return self.__id
  def get_descricao(self): return self.__descricao
  def get_valor(self): return self.__valor
  def get_duracao(self): return self.__duracao
  def set_id(self, id): self.__id = id
  def set_descricao(self, descricao): self.__descricao = descricao
  def set_valor(self, valor): self.__valor = valor
  def set_duracao(self, duracao): self.__duracao = duracao
  def __str__(self):
    return f"{self.__id} - {self.__descricao} - {self.__valor} - {self.__duracao}"


class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
 


class NServico:
  __servicos = []         # lista de serviços inicia vazia
  @classmethod
  def inserir(cls, obj):
    NServico.abrir()
    id = 0 # encontrar o maior id já usado
    for servico in cls.__servicos:
      if servico.get_id() > id: id = servico.get_id()
    obj.set_id(id + 1)
    cls.__servicos.append(obj)  # insere um serviço (obj) na lista
    NServico.salvar()
  @classmethod
  def listar(cls):
    NServico.abrir()    
    return cls.__servicos      # retorna a lista de serviços
  @classmethod
  def listar_id(cls, id):
    NServico.abrir()
    for servico in cls.__servicos:
      if servico.get_id() == id: return servico
    return None
  @classmethod
  def atualizar(cls, obj):
    NServico.abrir()
    servico = cls.listar_id(obj.get_id())
    if servico != None:
      servico.set_descricao(obj.get_descricao())
      servico.set_valor(obj.get_valor())
      servico.set_duracao(obj.get_duracao())
      NServico.salvar()
  @classmethod
  def excluir(cls, obj):
    NServico.abrir()
    servico = cls.listar_id(obj.get_id())
    cls.__servicos.remove(servico)    
    NServico.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__servicos = []
      with open("servicos.json", "r") as f:
        servicos__json = json.load(f)
      for obj in servicos__json:
        c = Servico(obj["_Servico__id"], obj["_Servico__descricao"], obj["_Servico__valor"], obj["_Servico__duracao"])
        cls.__servicos.append(c)
    except FileNotFoundError:
      #print: nenhum arquivo encontrado
      pass
  @classmethod
  def salvar(cls):
    with open("servicos.json", "w") as f:
      json.dump(cls.__servicos, f, default=vars)

class NCliente:
  __clientes = []         # lista de clientes inicia vazia
  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0 # encontrar o maior id já usado
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)  # insere um cliente (obj) na lista
    NCliente.salvar()
  @classmethod
  def listar(cls):
    NCliente.abrir()    
    return cls.__clientes       # retorna a lista de clientes
  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()
  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)    
    NCliente.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"],
                     cliente["_Cliente__email"], cliente["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as f:
      json.dump(cls.__clientes, f, default=vars)

class UI:
  @classmethod
  def Main(cls):
    op = 0
    while(op != 99):
      op = UI.Menu()
      if op == 1: UI.ClienteInserir()
      if op == 2: UI.ClienteListar()
      if op == 3: UI.ClienteAtualizar()
      if op == 4: UI.ClienteExcluir()
      if op == 5: UI.ServicoInserir()
      if op == 6: UI.ServicoListar()
      if op == 7: UI.ServicoAtualizar()
      if op == 8: UI.ServicoExcluir()
  @classmethod
  def Menu(cls):
    print("1-Inserir cliente, 2-Listar cliente, 3-Atualizar cliente, 4-Excluir cliente, 5-Inserir serviço, 6-Listar serviço, 7-Atualizar serviço, 8-Excluir serviço, 99-Sair")
    return int(input())
  @classmethod
  def ServicoInserir(cls):
    # id = int(input("Id: "))
    descricao = input("Descrição: ")
    valor = input("Valor: ")
    duracao = input("Duração: ")
    servico = Servico(0, descricao, valor, duracao)
    NServico.inserir(servico)
    
  @classmethod
  def ClienteInserir(cls):
    # id = int(input("Id: "))
    nome = input("Nome: ")
    email = input("E-mail: ")
    fone = input("fone: ")
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
    
  @classmethod
  def ServicoListar(cls):
    for servico in NServico.listar():
      print(servico)

  @classmethod
  def ClienteListar(cls):
    for cliente in NCliente.listar():
      print(cliente)
      
  @classmethod
  def ServicoAtualizar(cls):
    UI.ServicoListar()
    id = int(input("Id do serviço a ser atualizado: "))
    descricao = input("Nova descrição: ")
    valor = input("Novo valor: ")
    duracao = input("Nova duração: ")
    servico = Servico(id, descricao, valor, duracao)
    NServico.atualizar(servico)    

  @classmethod
  def ClienteAtualizar(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser atualizado: "))
    nome = input("Novo nome: ")
    email = input("Novo e-mail: ")
    fone = input("Novo fone: ")
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)    


  @classmethod
  def ServicoExcluir(cls):
    UI.ServicoListar()
    id = int(input("Id do serviço a ser excluído: "))
    servico = Servico(id, "", "", "")
    NServico.excluir(servico)

  @classmethod
  def ClienteExcluir(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser excluído: "))
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)


UI.Main()