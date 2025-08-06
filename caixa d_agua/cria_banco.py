import sqlite3

# Conecta/Cria o banco de dados
conn = sqlite3.connect("nivel_agua.db")
cursor = conn.cursor()

# Cria a tabela dos níveis
cursor.execute("""
CREATE TABLE IF NOT EXISTS niveis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Cria a tabela dos comandos ligar/desligar
cursor.execute("""
CREATE TABLE IF NOT EXISTS comando (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    acao TEXT NOT NULL CHECK (acao IN ('ligar', 'desligar')),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()
print("Banco de dados criado com sucesso.")
