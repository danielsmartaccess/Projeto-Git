from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        form_data = {
            'email': request.form.get('email'),
            'visao_vida': request.form.get('visao_vida'),
            'sabatico': request.form.get('sabatico'),
            'sucesso': request.form.get('sucesso'),
            'superpoder': request.form.get('superpoder'),
            'investimento': request.form.get('investimento'),
            'prioridades': {
                'Realização Profissional': request.form.get('prio_realizacao'),
                'Família e Relacionamentos': request.form.get('prio_familia'),
                'Liberdade e Independência': request.form.get('prio_liberdade'),
                'Contribuição Social': request.form.get('prio_contribuicao'),
                'Conhecimento e Crescimento': request.form.get('prio_conhecimento')
            }
        }
        
        # Validate all fields are filled
        if not all(form_data.values()):
            raise ValueError("Todos os campos são obrigatórios")
        
        # Generate report
        report = f"""# Resultado da Descoberta de Valores

**Email:** {form_data['email']}

## Suas Escolhas

1. **Visão de Vida:** {form_data['visao_vida']}
2. **Ano Sabático:** {form_data['sabatico']}
3. **Visão de Sucesso:** {form_data['sucesso']}
4. **Superpoder:** {form_data['superpoder']}
5. **Investimento:** {form_data['investimento']}

## Suas Prioridades

1. Realização Profissional: {form_data['prioridades']['Realização Profissional']}
2. Família e Relacionamentos: {form_data['prioridades']['Família e Relacionamentos']}
3. Liberdade e Independência: {form_data['prioridades']['Liberdade e Independência']}
4. Contribuição Social: {form_data['prioridades']['Contribuição Social']}
5. Conhecimento e Crescimento: {form_data['prioridades']['Conhecimento e Crescimento']}

---

Relatório gerado automaticamente pelo sistema de Descoberta de Valores.
"""
        return render_template('report.html', report=report)
        
    except Exception as e:
        flash(str(e))
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
