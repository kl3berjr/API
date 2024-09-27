# - localhost/livros (GET) recebe
# - localhost/livros (POST) criar
# - localhost/livros/id (GET) recebe
# - localhost/livros/id (PUT) editar
# - localhost/livros (DELETE) exclui

from flask import Flask, jsonify, request

app = Flask(__name__)

# criação de um dicionario dentra de uma lista
livros = [
    {
        'id': 1,
        'titulo': 'Homem aranha',
        'autor': 'Kleber'
    },
    {
        'id': 2,
        'titulo': 'Homem aranha 2',
        'autor': 'kleber'
    },
]

# realização de consulta de todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# realizar consulta por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    
    return("Livro não encontrado!")

# editar um livro por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_edit = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livro[indice].update(livro_edit)
            return jsonify(livros[indice])

# Criar um novo livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    new_livro=request.get_json()
    livros.append(new_livro)
    return jsonify(livros)

#excluir um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, id  in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)