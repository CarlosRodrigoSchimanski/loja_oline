
def apllyRout(app):

    @app.route("/")
    def main():
        return "<p>pagina principal</p>"

    return app