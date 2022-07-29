from config.config_db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    participation = db.Column(db.Integer)

    
    def __init__(self, first_name, last_name, participation):
        self.first_name = first_name
        self.last_name = last_name
        self.participation = participation

    def json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'participation': self.participation
        }
