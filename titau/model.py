from titau import db

def num(s, t):
    if t == 'INTEGER':
        return int(s)
    else:
        return float(s)

class Residencia(db.Model):
    __tablename__ = 'residencias'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String())
    host_id = db.Column('host_id', db.Integer)
    host_name = db.Column('host_name', db.String())
    neighbourhood = db.Column('neighbourhood', db.String())
    latitude = db.Column('latitude', db.Float)
    longitude = db.Column('longitude', db.Float)
    room_type = db.Column('room_type', db.String()) 
    price = db.Column('price', db.Integer) 
    minimum_nights = db.Column('minimum_nights', db.Integer) 
    number_of_reviews = db.Column('number_of_reviews', db.Integer) 
    last_review = db.Column('last_review', db.String()) 
    reviews_per_month = db.Column('reviews_per_month', db.Float) 
    calculated_host_listings_count = db.Column('calculated_host_listings_count', db.Integer) 
    availability_365 = db.Column('availability_365', db.Integer) 
    neighbourhood_group = db.Column('neighbourhood_group', db.String())

    def dict(self):
        d = {}
        for column in self.__table__.columns:
            if str(column.type) in ['INTEGER','FLOAT']:
                d[column.name] = num(getattr(self, column.name), str(column.type))
            else:
                d[column.name] = str(getattr(self, column.name))

        return d
 

class Media(db.Model):
    __tablename__ = 'medias'
    id = db.Column('id', db.Integer, primary_key=True)
    neighbourhood_group = db.Column('neighbourhood_group', db.String())
    room_type = db.Column('room_type', db.String()) 
    price = db.Column('price', db.Integer) 
    def dict(self):
        d = {}
        for column in self.__table__.columns:
            if str(column.type) in ['INTEGER','FLOAT']:
                d[column.name] = num(getattr(self, column.name), str(column.type))
            else:
                d[column.name] = str(getattr(self, column.name))

        return d

    
class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column('id', db.Integer, primary_key=True)
    residencia_id = db.Column('id', db.Integer, primary_key=True)
    like = db.Column(db.Boolean)
