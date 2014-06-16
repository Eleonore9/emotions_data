from database import Base, session
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import datetime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

#-------------------User Class----------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(80), nullable=False)
    password = Column(String(10), nullable=False)
    username = Column(String(20), nullable=True)

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    #-------class methods
    @classmethod
    def authenticate(cls, email, password):
        auth = session.query(User).filter_by(email=email, password=password).first()
        return auth

    @classmethod
    def new(cls, email, password, username):
        user = User(email, password, username)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get(cls, id):
        user = session.query(User).get(id)
        return user
    
#-------------------Element Class----------------------------------
class Element(Base):
    __tablename__ = "elements"

    id = Column(Integer, primary_key = True)
    title = Column(String(150), nullable=True)
    url = Column(String(150), nullable=True)
    element_type = Column(String(80), nullable=False)
    emotion = Column(String(80), nullable=True)
    weather = Column(String(80), nullable=True)
    posted_at = Column(DateTime())
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User",
    backref=backref("elements", order_by=id))

    def __init__(self, title, url, element_type, emotion, weather, posted_at, user_id):
        self.title = title
        self.url = url
        self.element_type = element_type
        self.emotion = emotion
        self.weather = weather
        self.posted_at = posted_at
        self.user_id = user_id
    
    #-------class methods
    @classmethod
    def new(cls, title, url, element_type, emotion, weather, user_id):
        now = datetime.datetime.now()
        element = Element(title, url, element_type, emotion, weather, now, user_id)
        session.add(element)
        session.commit()
        return element

    @classmethod
    def get(cls, id):
        """get an element using its id """
        element = session.query(Element).get(id)
        return element
    
    @classmethod
    def get_all(cls):
        """gets all the elements"""
        elements = session.query(Element).all()
        return elements
    
    @classmethod
    def get_all_type(cls, element_type):
        """get all elements of a certain type"""
        elements_of_type = []
        all_types = session.query(Element).filter_by(element_type=element_type).all()
        for e in all_types:
            elements_of_type.append(e)
        return elements_of_type
    
    @classmethod
    def get_all_emotion(cls, emotion):
        """get all elements linked to a certain emotion"""
        elements_of_emotion = []
        all_emotions = session.query(Element).filter_by(emotion=emotion).all()
        for a in all_emotions:
            elements_of_emotion.append(a)
        return elements_of_emotion


if __name__ == "__main__":
    pass
