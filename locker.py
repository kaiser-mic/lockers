from usario.py import Usuario


"""Classe-> Locker: Representa um Armário individual.
Atributos: __locker_id, __is_ocupado, __usuario_id.
Métodos: associar_usuario(usuario_id), liberar_usuario(), get_status(), get_locker_id()"""


class Locker:
    def __init__(self, id_locker, status_locker, id_usario ) -> None:
        self.__locker_id = id_locker
        self.__is_ocupado = status_locker
        self.__usuario_id = id_usario
    def associar_usario(self, id_usario):
        if not self.__is_ocupado:
            self.__is_ocupado= True
            self.__usuario_id = id_usario
            return True
            #if not self.__is_ocupado: checa se o locker esta ocupado ou nao, se nao estiver ocupado ele segue para este bloco de codigo e troca o
            #status para True e adiciona o id do usario para o locker que foi criado, e retorna True para confirmar que a acao deu certo
        else:
            return False
            #Se estiver ocupado ele retornara false, assim informando que o armario ja esta ocupado
    def liberar_usario(self):
        if self.__is_ocupado:
            self.__is_ocupado = False
            self.__id_usario = None
            return True
            #Faz basicamente a mesma coisa so que ao contrario, se estiver ocupado ele esvia todas informações e reseta para o padrao, e retorna True para confirmar que a acao funcionou
        else:
            return False
    def get_status(self):
        return self.__is_ocupado
        #Retorna o status de ocupação do locker, chamando (instancia).get_status
    def get_locker_id(self):
        return self.__locker_id
        #retorna o id do locker, chamando 
    
    