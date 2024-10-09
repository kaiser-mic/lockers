'''Classe-> Usuario: Representa um usuário do sistema.
Atributos: __usuario_id, __nome.
Métodos: get_usuario_id(), get_nome().
'''


class Usuario:
    def __init__(self, id_usario, nome_usario) -> None:
        self.__usario_id = id_usario
        self.__nome = nome_usario
    def get_id_usario(self):
        return __usuario_id
        #retorna o id do usario ao chamar (instancia).get_id_usario
    def get_nome(self):
        return __nome
        #retorna o nome do usario ao chamar (instancia).get_nome