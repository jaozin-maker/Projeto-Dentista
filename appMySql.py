from flask import Flask,render_template, request, jsonify
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'clientes'
 
mysql = MySQL(app)
 
@app.route('/cadastro', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('cadastro.html')

     
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data_nascimento = request.form['data_nascimento']
        sexo = request.form['sexo']
        cursor = mysql.connection.cursor()
        
        cursor.execute(''' INSERT INTO nome VALUES(%s,%s,%s,%s)''',(nome,cpf,data_nascimento,sexo))
        mysql.connection.commit()
        cursor.close()
        return render_template('form.html')

@app.route('/test', methods = ['GET'])
def get_data_by_id():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nome;")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/login', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

    if usuario == "joaozinho@gmail.com" and senha == "89054210":
        return render_template ('cadastro.html')

    else:
        return render_template ('login.html')

app.run(host='localhost', port=5000)
