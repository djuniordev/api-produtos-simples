import sqlite3

# Conectar ao banco de dados (criará um novo se não existir)
conn = sqlite3.connect('banco_loja.db')

# Criar uma tabela de exemplo
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome VARCHAR(20) NOT NULL DEFAULT '',
        preco DOUBLE NOT NULL DEFAULT 0
    )
''')

# Commitar as alterações e fechar a conexão
conn.commit()
conn.close()
