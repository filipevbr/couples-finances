# 💰 Couples Finances (Finanças Casal)

Sistema web para gestão financeira compartilhada, focado em casais. Desenvolvido para praticar conceitos de desenvolvimento Fullstack com Python, arquitetura MVC e Bancos de Dados Relacionais.

> **Status do Projeto:** 🚧 Em Desenvolvimento (WIP)

## 🛠 Tecnologias Utilizadas

* **Backend:** Python 3, Flask
* **Banco de Dados:** SQLite, SQLAlchemy (ORM)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (CDN)
* **Controle de Versão:** Git & GitHub

## 📋 Funcionalidades (Roadmap)

Aqui está o progresso atual do desenvolvimento:

- [x] **Configuração Inicial:** Estrutura de pastas MVC e Ambiente Virtual (venv).
- [x] **Banco de Dados:** Modelagem das tabelas e criação automática do arquivo `.db`.
- [x] **Autenticação:**
    - [x] Formulário de Cadastro (Register) com validação de e-mail único.
    - [x] Sistema de Login com verificação de credenciais.
- [ ] **Gestão de Transações:**
    - [ ] Adicionar Receitas e Despesas.
    - [ ] Listar transações recentes.
- [ ] **Dashboard:** Visualização do saldo total.
- [ ] **Segurança:** Proteção de rotas (Login Required).

## 🚀 Como rodar o projeto localmente

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/filipevbr/couples-finances.git
    cd couples-finances
    ```

2.  **Crie e ative o ambiente virtual**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

4.  **Execute a aplicação**
    ```bash
    python app.py
    ```
    O servidor iniciará em `http://127.0.0.1:5000/`.

---
Desenvolvido por **Filipe Vaz** como projeto de portfólio.