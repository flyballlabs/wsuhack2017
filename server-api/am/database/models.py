from datetime import datetime

from am.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    mobile = db.Column(db.String(80))
    grade_level = db.Column(db.Integer)
    user_type = db.Column(db.Integer)
    school_id  = db.Column(db.Integer)

    #category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    #category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, username,password,name,email,mobile,grade_level,user_type,school_id):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.mobile = mobile
        self.grade_level = grade_level
        self.user_type = user_type
        self.school_id = school_id
              
        #if mobile is None:
        #    mobile = datetime.utcnow()

    def __repr__(self):
        return '<Username %r>' % self.username

