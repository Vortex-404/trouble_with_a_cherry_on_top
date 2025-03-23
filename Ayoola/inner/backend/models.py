from config import db

class Contact(db.Model):  # Renamed to follow PascalCase convention
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)  # Fixed typo in db.String
    last_name = db.Column(db.String(80), unique=False, nullable=False)  # Fixed typo in db.String
    email = db.Column(db.String(180), unique=True, nullable=False)  # Fixed typo in db.String
    password = db.Column(db.String(100), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "email": self.email,
            "password": self.password,
        }