import pymongo
from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding
from pymongo import MongoClient
from database.mongohandler import MongoHandler
import shutil

client = MongoClient()
db = client.test_database


def print_centered(text):
    columns = shutil.get_terminal_size().columns
    print(text.center(columns))


def input_centered(prompt):
    columns = shutil.get_terminal_size().columns
    return input(prompt.center(columns))


def menu_mensagens(handler, email):
    """
    :param handler: A handler object that provides methods for user and message-related operations.
    :param email: The email address of the user interacting with the menu.
    :return: None
    """
    while True:
        print_centered(50 * "-")
        print_centered("Menu de Opções - Mensagens")
        print_centered("1. Enviar mensagem")
        print_centered("2. Ler mensagens")
        print_centered("3. Voltar ao menu principal")
        print_centered(50 * "-")

        opcao_mensagem = input_centered("Escolha uma opção (1/2/3): ")

        if opcao_mensagem == '1':
            print_centered(50 * "-")
            print_centered("Lista de usuários cadastrados:")
            usuarios = handler.get_all_users()
            for usuario in usuarios:
                print_centered(usuario['email'])
            print_centered(50 * "-")

            while True:
                destinatario = input_centered("Digite o email do destinatário: ")
                authMail = handler.auth_email(destinatario)
                if authMail:
                    break
                else:
                    print_centered("Email invalido, tente novamente.")

            chave = input_centered("Digite a chave secreta: ")
            mensagem = input_centered("Digite sua mensagem: ")

            criptografar = criptografia(chave, mensagem)
            mensagem_objeto = {
                "remetente": email,
                "destinatario": destinatario,
                "mensagem": criptografar
            }
            handler.send_message(mensagem_objeto)

        elif opcao_mensagem == '2':
            while True:
                print_centered(50 * "-")
                mensagens = handler.get_users_who_sent_messages(email)
                if not mensagens:
                    print_centered("Nenhuma mensagem recebida.")
                    break

                print_centered("Mensagens recebidas:")
                for idx, mensagem in enumerate(mensagens):
                    print_centered(f"{idx + 1}. De: {mensagem['remetente']}")
                print_centered(f"{len(mensagens) + 1}. Voltar ao menu anterior")

                try:
                    print_centered(50 * "-")
                    escolha = int(input_centered("Escolha a mensagem que deseja ler (número): "))
                    if 1 <= escolha <= len(mensagens):
                        mensagem_selecionada = mensagens[escolha - 1]
                        chave_decripto = input_centered("Digite a chave secreta: ")
                        texto_decriptado = criptografia(chave_decripto, mensagem_selecionada['mensagem'], decrypt=True)
                        print_centered(f"Mensagem: {texto_decriptado}")
                        print_centered(50 * "-")
                    elif escolha == len(mensagens) + 1:
                        break
                    else:
                        print_centered(50 * "-")
                        print_centered("Escolha inválida, tente novamente.")
                except ValueError:
                    print_centered(50 * "-")
                    print_centered("Entrada inválida, insira um número.")

        elif opcao_mensagem == '3':
            print_centered(50 * "-")
            print_centered("Voltando ao menu principal...")
            break
        else:
            print_centered(50 * "-")
            print_centered("Opção inválida. Tente novamente.")


def criptografia(chave, mensagem, decrypt=False):
    """
    :param chave: The encryption key used for AES encryption/decryption.
    :param mensagem: The plaintext message to be encrypted or the ciphertext message to be decrypted.
    :param decrypt: A boolean flag indicating whether to decrypt the message (True) or encrypt the message (False). Default is False.
    :return: The encrypted or decrypted message based on the value of the decrypt parameter.
    """
    iv_parameter = "0011223344556677"
    output_format = "b64"
    cipher = AESCBCPKCS5Padding(chave, output_format, iv_parameter)
    if decrypt:
        decrypted_message = cipher.decrypt(mensagem)
        return decrypted_message
    else:
        criptomessage = cipher.encrypt(mensagem)
        return criptomessage


if __name__ == '__main__':
    handler = MongoHandler()
    auth = handler.authenticate('mateus@gmail.com', '123456qwerty')

    while True:
        print_centered(50 * "-")
        print_centered("Menu de Opções")
        print_centered("1. Login")
        print_centered("2. Cadastro")
        print_centered("3. Sair")
        print_centered(50 * "-")

        opcao = input_centered("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            while True:
                print_centered(50 * "-")
                email = input_centered("Digite seu email: ")
                password = input_centered("Digite sua senha: ")
                auth = handler.authenticate(email, password)
                if auth:
                    menu_mensagens(handler, email)
                    break
                else:
                    print_centered(50 * "-")
                    print_centered("Email ou senha inválidos. Tente novamente.")

        elif opcao == '2':
            print_centered(50 * "-")
            name = input_centered("Digite seu nome: ")
            email = input_centered("Digite seu email: ")
            password = input_centered("Digite sua senha: ")
            register_result = handler.register_user(email, password, name)
        elif opcao == '3':
            print_centered("Saindo do programa...")
            break
        else:
            print_centered("Opção inválida. Tente novamente.")
