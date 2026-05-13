from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def curriculo():
    
    data = {
        "nome": "João Silva",
        "telefone": "+55 11 99999-9999",
        "email": "joao.silva@email.com",
        "educacao": [
            {"instituicao": "Universidade Federal de Tecnologia", "curso": "Engenharia de Software", "ano": "2018 - 2022"},
            {"instituicao": "Escola Técnica Estadual", "curso": "Técnico em Informática", "ano": "2015 - 2017"}
        ],
        "experiencia": [
            {"empresa": "Tech Solutions", "cargo": "Desenvolvedor Backend", "periodo": "Jan 2023 - Presente", "detalhes": "Desenvolvimento de APIs com Flask, otimização de banco de dados."},
            {"empresa": "Web Innovators", "cargo": "Estagiário", "periodo": "Jul 2021 - Dez 2022", "detalhes": "Manutenção de sites e automação de testes."}
        ],
        "cursos": ["Python para Dados - Udemy", "Flask Web Development - Coursera"],
        "idiomas": [
            {"lingua": "Inglês", "nivel": "Avançado (C1)"},
            {"lingua": "Espanhol", "nivel": "Intermediário (B2)"}
        ]
    }
    return render_template('index.html', cv=data)

if __name__ == '__main__':
    app.run(debug=True)
