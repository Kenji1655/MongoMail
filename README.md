# Mini Projeto - Implementação de Chat Criptografado (Python/Java)

## Descrição do Projeto

Este projeto tem como objetivo desenvolver uma aplicação de chat com interface de linha de comando (CLI), utilizando Python ou Java, com foco na segurança das mensagens trocadas entre dois usuários, Alice e Bob. A segurança será garantida por meio da utilização de criptografia simétrica, assegurando que as mensagens estejam protegidas durante o armazenamento e a troca. O projeto explora a implementação de criptografia, armazenamento seguro e boas práticas para garantir a confidencialidade das comunicações.

## Funcionalidades Principais

### 1. Estabelecimento da Chave Simétrica
- **Chave Secreta Compartilhada**: Alice e Bob concordam em utilizar uma chave secreta baseada no padrão *PBE-PKCS* (Password-Based Encryption).
- **Segurança da Chave**: A chave **não será armazenada** em nenhum local, garantindo que a segurança dependa exclusivamente da confidencialidade da chave compartilhada.

### 2. Criptografia das Mensagens
- **Função Cifrar (cypher)**: Responsável por criptografar as mensagens antes de serem enviadas ou armazenadas no banco de dados.
- **Função Decifrar (decrypt)**: Descriptografa as mensagens quando são recuperadas do banco de dados, tornando-as legíveis apenas para os destinatários.
- **Armazenamento Seguro**: As mensagens são armazenadas de forma criptografada em um banco de dados MongoDB, utilizando a biblioteca *PyMongo*.

### 3. Armazenamento e Recuperação de Mensagens
- **Inserção de Mensagens**: As mensagens criptografadas são armazenadas no banco de dados com os campos “de” (remetente) e “para” (destinatário).
- **Recuperação de Mensagens**: Ao recuperar uma mensagem, ela é descriptografada para ser visualizada, garantindo a confidencialidade dos dados até o momento da leitura.

### 4. Filtragem e Segurança
- **Boas Práticas de Segurança**: Além da criptografia, serão aplicadas medidas de segurança para prevenir vulnerabilidades, como o armazenamento inadequado de chaves e o acesso não autorizado às mensagens.

## Ferramentas e Tecnologias
- **Python/Java**: Linguagens de programação utilizadas para o desenvolvimento da aplicação.
- **MongoDB**: Banco de dados utilizado para o armazenamento das mensagens.
- **PyMongo**: Biblioteca para interação com o MongoDB (no caso da implementação em Python).
- **PBE-PKCS**: Padrão de criptografia utilizado para gerar e manejar a chave simétrica.

## Como Usar

1. **Clone o Repositório**: 
   ```bash
   git clone https://github.com/Kenji1655/MongoMail.git
   ```

2. **Instale as Dependências (Python)**:
   ```bash
   pip install pymongo
   ```

3. **Execute a Aplicação**:
   - Certifique-se de que o MongoDB esteja rodando e execute a aplicação por meio da linha de comando.

4. **Envie e Receba Mensagens**: Utilize os comandos disponíveis para Alice e Bob trocarem mensagens de forma segura.

## Licença
Este projeto é distribuído sob a licença MIT.

---
