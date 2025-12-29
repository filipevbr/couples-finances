from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuracao do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo (tabela do usuario)
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

# ----- ROTAS -----
# Rota da pagina inicial
@app.route('/')
def homepage():
    return render_template('index.html')

# Rota de cadastro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Pega os dados do HTML
        nome = request.form['nome_cadastro']
        email = request.form['email_cadastro']
        senha = request.form['senha_cadastro']

        # Verifica se o email já existe no banco (Query)
        usuario_existente = Usuario.query.filter_by(email=email).first()
        
        if usuario_existente:
            return '<h1>Erro: Este e-mail já está cadastrado!</h1>'

        # 3. Cria o novo usuário (Objeto)
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)

        # 4. Salva no Banco (INSERT)
        db.session.add(novo_usuario)
        db.session.commit()

        return '<h1>Conta criada com sucesso! <a href="/login">Faça Login</a></h1>'

    return render_template('register.html')

# Rota da pagina de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Pega os dados do HTML
        email = request.form['user_email']
        senha = request.form['user_password']

        # Busca o usuário no banco pelo email
        usuario = Usuario.query.filter_by(email=email).first()

        # Verifica se achou E se a senha bate
        if usuario and usuario.senha == senha:
            return f'<h1>Bem-vindo de volta, {usuario.nome}! Login Realizado. 🚀</h1>'
        else:
            return '<h1>Erro: Email não encontrado ou senha errada.</h1>'
    
    return render_template('login.html')

# ----- INICIALIZACAO -----
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Garante que as tabelas existem
    app.run(debug=True)