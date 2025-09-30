

# 🚀 Configuração de Ambiente com Docker Compose

Este projeto foi desenvolvido como parte do **Desafio da Rocketseat**, com foco em consolidar os conhecimentos de **Dockerfile**, **Docker Compose**, **redes**, **volumes** e **variáveis de ambiente**.

---

## 📚 Tecnologias

- 🐍 **Python 3.11 (Alpine)**
- 🌐 **Flask** (Framework Web)
- 🗄️ **MySQL** (Banco de Dados)
- 🐳 **Docker & Docker Compose**

---

## 📂 Estrutura do Projeto

```

├── app/                  # Código da aplicação Flask
│   ├── **init**.py
│   └── main.py
├── Dockerfile            # Configuração da imagem da aplicação
├── docker-compose.yaml   # Orquestração dos containers
├── requirements.txt      # Dependências do Python
├── .env                  # Variáveis de ambiente (não versionar)
└── .gitignore            # Arquivos a serem ignorados

````

---

## ⚙️ Como Executar o Projeto

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/MorganaSouza/Configura-o-de-Ambiente-com-Docker-Compose.git
   cd Configura-o-de-Ambiente-com-Docker-Compose
````

2. **Criar o arquivo `.env`**

   ```env
   DB_HOST=db
   DB_USER=app_user
   DB_PASSWORD=senha_app
   DB_NAME=meuappdb
   ```

3. **Subir os containers**

   ```bash
   docker-compose up --build
   ```

4. **Acessar a aplicação**

   ```
   http://localhost:3000
   ```

---

## 🗄️ Banco de Dados

Acesse o MySQL dentro do container:

```bash
docker exec -it mysql_db mysql -u app_user -p
```

Senha: `senha_app`

---

## 🛠️ Recursos de Infraestrutura

* 📦 **Volumes**

  * `db_data` → garante a persistência dos dados do MySQL.

* 🌐 **Rede customizada**

  * `app_network` → isola e gerencia a comunicação entre os containers.

---

## ✅ Requisitos Atendidos

* [x] Criação do **Dockerfile**
* [x] Definição do **Docker Compose** com múltiplos serviços
* [x] Persistência de dados com **Volumes**
* [x] **Rede customizada** para os containers
* [x] Uso de **Variáveis de Ambiente**
* [x] Usuário **não-root** para conexão ao banco
* [x] **Documentação (README)**

---

## 🔒 Boas Práticas

* Não versionar o arquivo `.env` → crie um `.env.example` para referência.
* Usar `.gitignore` para ignorar:

  ```
  __pycache__/
  *.pyc
  .env
  *.log
  ```



## 👩‍💻 Autora

Projeto desenvolvido por Morgana Souza, como parte do Desafio Docker Compose - Rocketseat.


