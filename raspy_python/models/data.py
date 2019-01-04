from extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, String, Table, text, Integer, Boolean, Float, REAL
from sqlalchemy.orm import relationship
from flask_login import UserMixin

Base = db.Model
metadata = Base.metadata


class User(UserMixin, Base):
    __tablename__ = 'data_user'
    table_args = {"useexisting": True}
    id = Column(Integer(), primary_key=True)
    username = Column(String(255))
    password = Column(String(255))

    def __repr__(self):
        # formats what is shown in the shell when print is
        # called on it
        return '<User {}>'.format(self.username)
    
    def get_id(self):
        return self.id


class Wendu(Base):
    __tablename__ = 'data_wendu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String(100))
    save_time = Column(DateTime)
    time_style = Column(String(100))
    user_data_id = Column(ForeignKey('data_user.id'), nullable=True, index=True)

    user = relationship('User', backref='data_wendus')


class Shidu(Base):
    __tablename__ = 'data_shidu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String(100))
    save_time = Column(DateTime)
    time_style = Column(String(100))
    user_data_id = Column(ForeignKey('data_user.id'), nullable=True, index=True)

    user = relationship('User', backref='data_shidus')


class AddParametersGroup(Base):
    __tablename__ = 'add_parameters_group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    unit = Column(String(20))
    description = Column(String(100))


class AddParametersData(Base):
    __tablename__ = 'add_parameters_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    value = Column(REAL)
    save_time = Column(DateTime)
    group_id = Column(ForeignKey('add_parameters_group.id'), nullable=True, index=True)
    my_group = relationship('AddParametersGroup', backref='my_datas')
