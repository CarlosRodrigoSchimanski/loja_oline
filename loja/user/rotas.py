from flask import Blueprint, render_template, request

usuario_bluprint = Blueprint('usuarios', __name__, template_folder='templates')

@usuario_bluprint.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        name = request.form.get('nome')
        username = request.form.get('usuario')
        password = request.form.get('senha')
        rpassword = request.form.get('c_senha')
        
    else:
        return render_template('cadastro.html')