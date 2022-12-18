from settings import db, app

class Sentiment_Analysis_Model(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    technique = db.Column(db.String(100))
    description = db.Column(db.String(500))

    def __inti__(self, technique, description):
        self.technique = technique
        self.description = description