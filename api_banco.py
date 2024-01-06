from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def homepage():
    return "API BANCO"

# Consultar os Dados

@app.route("/produtos", methods=['GET'])
def obter_produtos():

    conn = sqlite3.connect('banco_loja.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos_banco = cursor.fetchall()

    produtos = [{'id': produto[0], 'nome': produto[1], 'preco': produto[2]} for produto in produtos_banco]

    return jsonify(produtos)

# Consultar os Dados por ID

@app.route("/produtos/<int:id>", methods=['GET'])
def obter_produtos_id(id):

    conn = sqlite3.connect('banco_loja.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos_banco = cursor.fetchall()

    produtos = [{'id': produto[0], 'nome': produto[1], 'preco': produto[2]} for produto in produtos_banco]
    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)

# Adicionar os Dados

@app.route("/produtos", methods=['POST'])
def cadastrar_produtos():
    produto = request.get_json()

    conn = sqlite3.connect('banco_loja.db')
    cursor = conn.cursor()
    sql = "INSERT INTO produtos (nome, preco) VALUES (?, ?)"
    cursor.execute(sql, (produto['nome'], produto['preco']))
    conn.commit()

    return jsonify(produto)

# Editar os Dados

@app.route("/produtos/<int:id>", methods=['PUT'])
def editar_produtos(id):
    conn = sqlite3.connect('banco_loja.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
    produtos_banco = cursor.fetchall()
        
    produtos = [{'id': produto[0], 'nome': produto[1], 'preco': produto[2]} for produto in produtos_banco]
    produto_alterado = request.get_json()
    print(produto_alterado)
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            sql = "UPDATE produtos SET nome = ?, preco = ? WHERE id = ?"
            cursor.execute(sql, (produto_alterado['nome'], produto_alterado['preco'], id))
            conn.commit()
            return jsonify(produtos[indice])

# Deletar os Dados

@app.route("/produtos/<int:id>", methods=['DELETE'])
def excluir_produtos(id):
    conn = sqlite3.connect('banco_loja.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
    produtos_banco = cursor.fetchall()
    
    produtos = [{'id': produto[0], 'nome': produto[1], 'preco': produto[2]} for produto in produtos_banco]
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            sql = "DELETE from produtos WHERE id = ?"
            cursor.execute(sql, (id,))
            conn.commit()
            return jsonify(produtos[indice])

app.run(host='localhost', port=5000, debug=True)