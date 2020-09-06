import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = 'postgresql://andrey:fylhtq32741553@localhost:5432/les6DB'
engine = create_engine(db)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(80), nullable=False)


class Book(Base):
    __tablename__ = 'book'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(80), nullable=False)
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey('publisher.id'))


class Stock(Base):
    __tablename__ = 'stock'
    id = sa.Column(sa.Integer, primary_key=True)
    id_book = sa.Column(sa.Integer, sa.ForeignKey('book.id'))
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'))
    count = sa.Column(sa.Integer, nullable=False)


class Shop(Base):
    __tablename__ = 'shop'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(80), nullable=False)


class Sale(Base):
    __tablename__ = 'sale'
    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Numeric(7, 2), nullable=False)
    date_sale = sa.Column(sa.Date, nullable=False)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey('stock.id'))
    count = sa.Column(sa.Integer, nullable=False)

Base.metadata.create_all(engine)