from flask import render_template, request
def apllyRout(app):

    @app.route("/")
    def indice():
        return "<p>pagina principal</p>"
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':
            name = request.form.get('nome')
            username = request.form.get('usuario')
            password = request.form.get('senha')
            rpassword = request.form.get('c_senha')
           
        else:
            return render_template('cadastro.html')

    return app