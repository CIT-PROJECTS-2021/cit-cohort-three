from fruits import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=3000, debug=True)