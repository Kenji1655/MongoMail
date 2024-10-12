from database.entities import Message
from database.entities import User
from pymongo import MongoClient


class MongoHandler:
    def __init__(self):
        self.connection_string = "mongodb+srv://kenjigustavo7:Mongo67@mongomaildb.brshz.mongodb.net/?retryWrites=true&w=majority&appName=MongoMailDB"
        self.client = MongoClient(self.connection_string)

    def connect(self, database_name):
        return self.client[database_name]

    def authenticate(self, email, password) -> bool:
        db = self.connect("chat")
        user = db.users.find_one({"email": email, "password": password})
        if user:
            return True
        else:
            return False

    def register_user(self, email, password, nickname):
        db = self.connect("chat")
        existing_user = db.users.find_one({"email": email})
        if existing_user:
            print(50 * "-")
            print("Usuário já existe")
            return False  # Usuário já existe
        else:
            new_user = {"email": email, "password": password, "nickname": nickname}
            db.users.insert_one(new_user)
            print(50 * "-")
            print("Usuário cadastrado com sucesso")
            return True  # Usuário cadastrado com sucesso

    def get_all_users(self):
        db = self.connect("chat")
        users = list(db.users.find())
        return users

    def auth_email(self, email):
        db = self.connect("chat")
        user = db.users.find_one({"email": email})
        if user:
            return True
        else:
            return False

    def send_message(self, m):
        db = self.connect("chat")
        collection = db.messages
        print("Mensagem enviada com sucesso")
        return collection.insert_one(m).inserted_id

    # Assuming a functional my_chats method definition
    def my_chats(self, nickname_logado):
        db = self.connect("chat")
        messages = db.messages.find({"$or": [{"remetente": nickname_logado}, {"destinatario": nickname_logado}]})
        chat_data = []
        for message in messages:
            decrypted_message = criptografia(message['chave'], message['mensagem'])
            chat_data.append({
                "remetente": message["remetente"],
                "destinatario": message["destinatario"],
                "mensagem": decrypted_message
            })
        return chat_data

    def get_users_who_sent_messages(self, logged_in_user_email):
        db = self.connect("chat")
        # Find distinct senders who sent messages to the logged-in user
        distinct_senders = db.messages.distinct("remetente", {"destinatario": logged_in_user_email})

        sender_messages = []
        for sender in distinct_senders:
            encrypted_messages = db.messages.find({"destinatario": logged_in_user_email, "remetente": sender})
            for i, message in enumerate(encrypted_messages, start=1):
                sender_messages.append({
                    "indice": i,
                    "remetente": sender,
                    "mensagem": message['mensagem']  # Do not apply criptografia
                })
        return sender_messages

    def opcao_mensagem_handler(self, logged_in_user_email):
        if opcao_mensagem == 2:
            messages = self.get_users_who_sent_messages(logged_in_user_email)

            if not messages:
                print("Nenhuma mensagem recebida.")
                return

            print("Caixa de entrada:")
            for message in messages:
                print(f"[{message['indice']}] Remetente: {message['remetente']}")

            # Solicitando ao usuário que escolha qual mensagem deseja ler
            escolha = int(input("Digite o número da mensagem que deseja ler: "))

            # Verificando se a escolha é válida
            mensagem_escolhida = next((msg for msg in messages if msg['indice'] == escolha), None)

            if mensagem_escolhida:
                print(f"Mensagem de {mensagem_escolhida['remetente']}:")
                print(f"{mensagem_escolhida['mensagem']}")
            else:
                print("Escolha inválida.")