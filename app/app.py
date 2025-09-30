"""Aplicação Flask conectando ao MySQL dentro de um container Docker"""

import os
import mysql.connector
from mysql.connector import Error
from flask import Flask

# Inicializa a aplicação Flask
app = Flask(__name__)

@app.route("/")
def home():
    """Rota inicial"""
    return "Aplicação Flask rodando dentro de um container Docker! 🚀"

@app.route("/db")
def db_test():
    """Testa a conexão com o banco MySQL"""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "app_user"),
            password=os.getenv("DB_PASSWORD", "senha_app"),
            database=os.getenv("DB_NAME", "meuappdb"),
        )

        cursor = conn.cursor()
        cursor.execute("SELECT 'Conexão bem-sucedida com o banco!'")
        result = cursor.fetchone()

        # Fecha recursos
        cursor.close()
        conn.close()

        return result[0]

    except Error as err:
        return f"Erro do MySQL: {str(err)}"
    # Se quiser capturar qualquer outro erro inesperado, mantenha assim:
    # except Exception as e:  # pylint: disable=broad-exception-caught
    #     return f"Erro inesperado: {str(e)}"

if __name__ == "__main__":
    # Executa a aplicação Flask
    app.run(host="0.0.0.0", port=3000, debug=True)
