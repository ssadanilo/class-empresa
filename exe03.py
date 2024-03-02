# Crie uma classe Empresa que permita gerenciar funcionários. Os funcionários devem ter informações
# como nome, cargo e salário. A empresa deve ser capaz de adicionar, remover e listar funcionários.

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                return True
        return False
    
    def listar_funcionarios(self):
        if self.funcionarios:
            print('Funcionarios da empresa', self.nome + ':')
            for funcionario in self.funcionarios:
                print('Nome:', funcionario.nome, '- Cargo:', funcionario.cargo, '- Salário:', funcionario.salario)
        else:
            print('Não há funcionários registrados', self.nome)

# Uso das classes Funcionario e Empresa
empresa = Empresa('É de Fachada S/A')

funcionario1 = Funcionario('Jerônimo', 'Governador', 25000)
funcionario2 = Funcionario('Bruno Reis', 'Prefeito', 17000)
funcionario3 = Funcionario('Zé', 'Estagiário', 1000)

empresa.adicionar_funcionario(funcionario1)
empresa.adicionar_funcionario(funcionario2)
empresa.adicionar_funcionario(funcionario3)

empresa.listar_funcionarios()

empresa.remover_funcionario('Zé')

empresa.listar_funcionarios()
