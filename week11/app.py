import os
from todosapp import create_app, db


app = create_app()

# Run Server
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    PORT = int(os.environ.get("PORT", 8080))
    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=False
    ) #Production