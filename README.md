# Mini Projeto - Implementação de Chat Criptografado (Python)

## Descrição do Projeto

Este projeto tem como objetivo desenvolver uma aplicação de chat com interface de linha de comando (CLI), utilizando Python, com foco na segurança das mensagens trocadas entre dois usuários. A segurança será garantida por meio da utilização de criptografia simétrica, assegurando que as mensagens estejam protegidas durante o armazenamento e a troca. O projeto explora a implementação de criptografia, armazenamento seguro e boas práticas para garantir a confidencialidade das comunicações.

## Funcionalidades Principais

### 1. Estabelecimento da Chave Simétrica
- **Chave Secreta Compartilhada**: Usuarios concordam em utilizar uma chave secreta baseada no padrão *PBE-PKCS* (Password-Based Encryption).
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
- **Python**: Linguagens de programação utilizadas para o desenvolvimento da aplicação.
- **MongoDB**: Banco de dados utilizado para o armazenamento das mensagens.
- **PyMongo**: Biblioteca para interação com o MongoDB (no caso da implementação em Python).
- **PBE-PKCS**: Padrão de criptografia utilizado para gerar e manejar a chave simétrica.

# Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Kenji1655/MongoMail.git
    cd MongoMail
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:
    
        ```bash
        .\venv\Scripts\activate
        ```

    - No Unix ou MacOS:
    
        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

Certifique-se de que o MongoDB está rodando e configurado corretamente no seu sistema.

## Estrutura do Projeto

O projeto é organizado nos seguintes diretórios e arquivos principais:

- `main.py`: O ponto de entrada principal do aplicativo.
- `database/`: Contém os arquivos relacionados ao banco de dados MongoDB.
    - `entities.py`: Define as entidades do banco de dados.
    - `mongohandler.py`: Manipula as operações com o MongoDB.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
---
