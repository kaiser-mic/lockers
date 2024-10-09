from locker.py import Locker
'''Classe-> SistemaLocker: Gerencia os lockers e os usuários.
Atributos: __lockers, __usuarios, __locker_arq.
Métodos: adicionar_locker(locker_id), adicionar_usuario(usuario_id, nome), 
associar_locker_ao_usuario(locker_id, usuario_id), liberar_locker(locker_id), 
get_locker_status(locker_id), salvar_locker(locker_id), carregar_lockers(), 
salvar_dado(nome_arquivo), carregar_dados(nome_arquivo).'''

class Sistemausuario:
    def __init__(self, locker_arq='lockers.txt') -> None:
        self.__lockers = {}
        self.__usarios = {}
        self.__locker_arq = locker_arq
    def adicionar_locker(self, locker_id):
        if locker_id not in self.__lockers:
            self.__locker[locker_id] = Locker(locker_id)
            self.salvar_locker(locker_id)
            return True
            #if locker_id not in self.__lockers: checa se o id seleciona ja nao existe, se nao exisitir ele segue para criar um novo locker, a primeira
            #funcao adiciona o locker_id ate a classe Locker, que esta em outro arquivo, junto com o locker_id, que ira para a instancia do objeto locker
            #self.salvar salva o locker dentro do arquivo de texto
        else:
            return False
    def adicionar_usario(self, usuario_id, nome):
        if usuario_id not in self.__usarios:
            self.__usarios=[usuario_id] = Usuario(usuario_id, nome)
            return True
            #if usuario_id not in self.__usarios: checa se o id do usuario ja nao existe no arquivo de texto, se nao existir ele segue no bloco de codigos
            #self.__usarios=[usuario_id] = Usuario(usuario_id, nome) atribui o id do usario para o usario, tambem atribuindo o nome ate a classe Usuario que esta em outro arquivo
        else:
            return False
    def associar_locker_ao_usuario(self, locker_id, usuario_id):
        if locker_id in self.__lockers and usuario_id in self__usarios:
            return self.__locker[locker_id].associar_usario(usuario_id)
        #if locker_id in self.__lockers and usuario_id in self__usarios: checa se o id do locker e do usario existem no diretorio, se sim ele executa o bloco de codigos
        #ele atualiza o locker com o id que foi elecionado e chama o metodo associar_usuario do arquivo locker.py, passando pela linha de codigo
        #if not self.__is_ocupado: checa se o locker esta ocupado ou nao, se nao estiver ocupado ele segue para este bloco de codigo e troca o
        #status para True e adiciona o id do usario para o locker que foi criado, e retorna True para confirmar que a acao deu certo
        #assim atualizando o locker a atribuindo a uma pessoa com o id
        return False
    def liberar_locker(self, locker_id):
        if locker_id in self.__lockers:
            return self.__lockers[locker_id].liberar_usuario()
        #if locker_id in self.__lockers: checa se o id do locker existe no arquivo de texto, se existir ele executa o bloco de codigos abaixo
        #Ele retorna o id do locker que devera ser liberado, assim chamando a função liberar_usario de outro arquivo que faz o seguinte:
        #Faz basicamente a mesma coisa so que ao contrario, se estiver ocupado ele esvia todas informações e reseta para o padrao, e retorna True para confirmar que a acao funcionou
        #assim liberando o locker retornnando ao estado desocupado
    def get_locker_status(self, locker_id):
        if locker_id in self.__lockers:
            return self.__lockers[locker_id].get_status()
        #retorna o status do locker especifico pedindo o locker_id para selecionar o mesmo com a função get_status que faz o seguinte:
        #Retorna o status de ocupação do locker, chamando (instancia).get_status
        return None
    def salvar_locker(self, locker_id):
        with open(self.__locker_arq, 'a') as arquivo:
            arquivo.write(f'{locker_id}\n')
        #open abre o arquivo, puxando de self.__locker_arq, como um arquivo, write escreve no arquivo os id's de lockers criados ate agora
    def carregar_lockers(self):
        try:
            with open(self.__locker_arq, 'r') as arquivo:
                for linha in arquivo:
                    locker_id=linha.strip()
                    self.__lockers[locker_id] = Locker(locker_id)
        except FileNotFoundError:
            pass
    def salvar_dado(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for locker_id, locker in self.__lockers.items():
                is_ocupado, usuario_id = locker.get_status()
                arquivo.write(f'{locker_id},{is_ocupado},{usuario_id}\n')
    def carregar_dados(self,nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    locker_id, is_ocupado, usuario_id = linha.strip().split(',')
                    self.adicionar_locker(locker_id)
                    if is_ocupado == 'True':
                        self.associar_locker_ao_usuario(locker_id, usuario_id)
        except FileNotFoundError:
            pass