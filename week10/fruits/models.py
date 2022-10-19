from fruits import db
from datetime import datetime


class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# fruits model
class Fruit(db.Model, ExtraMixin):
    __tablename__ = 'fruits'
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()