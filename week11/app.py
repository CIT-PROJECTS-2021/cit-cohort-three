from todosapp import create_app, db


app = create_app()

# Run Server
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)