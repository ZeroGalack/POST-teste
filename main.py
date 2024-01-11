from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "TESTE POST"

@app.route('/receber_post', methods=['POST'])
def receber_post():
    # Verifica se o pedido é um POST
    if request.method == 'POST':
        # Obtém os dados do corpo do pedido
        dados_do_post = request.json  # Supondo que os dados são enviados como JSON

        # Faça algo com os dados, por exemplo, imprimir no console
        print("Dados recebidos:", dados_do_post)

        # Retorne uma resposta
        return "Pedido POST recebido com sucesso!"

if __name__ == '__main__':
    # Inicia o servidor Flask
    app.run(debug=True)
