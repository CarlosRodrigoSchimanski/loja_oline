from projeto import create_app, db
from projeto.models import User

app = create_app()
'''with app.app_context():
    db.create_all()'''

if __name__ == "__main__":
    app.run(debug=True)