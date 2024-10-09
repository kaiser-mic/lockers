class Locker:  # Armário
    def __init__(self, locker_id):
        self.__locker_id = locker_id
        self.__is_ocupado = False
        self.__usuario_id = None

    def associar_usuario(self, usuario_id):
        if not self.__is_ocupado:
            self.__is_ocupado = True
            self.__usuario_id = usuario_id
            return True
        return False

    def liberar_usuario(self):
        if self.__is_ocupado:
            self.__is_ocupado = False
            self.__usuario_id = None
            return True
        return False

    def get_status(self):
        return self.__is_ocupado, self.__usuario_id

    # def get_locker_id(self):
    #     return self.__locker_id

class Usuario:
    def __init__(self, usuario_id, nome):
        self.__usuario_id = usuario_id
        self.__nome = nome

    # def get_usuario_id(self):
    #     return self.__usuario_id

    def get_nome(self):
        return self.__nome



class SistemaLocker: #LockerSystem:
    def __init__(self, locker_arq='lockers.txt'):
        self.__lockers = {}
        self.__usuarios = {}
        self.__locker_arq = locker_arq
        self.carregar_lockers()

    def adicionar_locker(self, locker_id):
        if locker_id not in self.__lockers:
            self.__lockers[locker_id] = Locker(locker_id)
            self.salvar_locker(locker_id)
            return True
        return False

    def adicionar_usuario(self, usuario_id, nome):
        if usuario_id not in self.__usuarios:
            self.__usuarios[usuario_id] = Usuario(usuario_id, nome)
            return True
        return False

    def associar_locker_ao_usuario(self, locker_id, usuario_id):
        if locker_id in self.__lockers and usuario_id in self.__usuarios:
            return self.__lockers[locker_id].associar_usuario(usuario_id)#  .assign_user(usuario_id)
        return False

    def libera_locker(self, locker_id):
        if locker_id in self.__lockers:
            return self.__lockers[locker_id].liberar_usuario()
        return False

    def get_locker_status(self, locker_id):
        if locker_id in self.__lockers:
            return self.__lockers[locker_id].get_status()
        return None

    def salvar_locker(self, locker_id):
        with open(self.__locker_arq, 'a') as arquivo:
            arquivo.write(f'{locker_id}\n')

    def carregar_lockers(self):
        try:
            with open(self.__locker_arq, 'r') as arquivo:
                for linha in arquivo:
                    locker_id = linha.strip()
                    self.__lockers[locker_id] = Locker(locker_id)
        except FileNotFoundError:
            pass

    def salvar_dado(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for locker_id, locker in self.__lockers.items():
                is_ocupado, usuario_id = locker.get_status()
                arquivo.write(f'{locker_id},{is_ocupado},{usuario_id}\n')

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    locker_id, is_ocupado, usuario_id = linha.strip().split(',')
                    self.adicionar_locker(locker_id)
                    if is_ocupado == 'True':
                        self.associar_locker_ao_usuario(locker_id, usuario_id)
        except FileNotFoundError:
            pass

def menu():
    system = SistemaLocker()
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Locker")
        print("2. Adicionar Usuário")
        print("3. Atribuir Locker a Usuário")
        print("4. Liberar Locker")
        print("5. Verificar Status do Locker")
        print("6. Salvar Dados")
        print("7. Carregar Dados")
        print("8. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            locker_id = input("Digite o ID do Locker: ")
            if system.adicionar_locker(locker_id):
                print("Locker adicionado com sucesso.")
            else:
                print("Locker já existe.")
        elif escolha == '2':
            usuario_id = input("Digite o ID do Usuário: ")
            nome = input("Digite o Nome do Usuário: ")
            if system.adicionar_usuario(usuario_id, nome):
                print("Usuário adicionado com sucesso.")
            else:
                print("Usuário já existe.")
        elif escolha == '3':
            locker_id = input("Digite o ID do Locker: ")
            usuario_id = input("Digite o ID do Usuário: ")
            if system.associar_locker_ao_usuario(locker_id, usuario_id):
                print("Locker atribuído com sucesso.")
            else:
                print("Erro ao atribuir locker.")
        elif escolha == '4':
            locker_id = input("Digite o ID do Locker: ")
            if system.libera_locker(locker_id):
                print("Locker liberado com sucesso.")
            else:
                print("Erro ao liberar locker.")
        elif escolha == '5':
            locker_id = input("Digite o ID do Locker: ")
            status = system.get_locker_status(locker_id)
            if status:
                is_ocupado, usuario_id = status
                print(f"Locker {locker_id} - Ocupado: {is_ocupado}, Usuário: {usuario_id}")
            else:
                print("Locker não encontrado.")
        elif escolha == '6':
            nome_arquivo = input("Digite o nome do arquivo para salvar os dados: ")
            system.salvar_dado(nome_arquivo)
            print("Dados salvos com sucesso.")
        elif escolha == '7':
            nome_arquivo = input("Digite o nome do arquivo para carregar os dados: ")
            system.carregar_dados(nome_arquivo)
            print("Dados carregados com sucesso.")
        elif escolha == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()