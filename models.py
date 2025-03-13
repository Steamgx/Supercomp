from sqlalchemy import Column, String, Integer, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///Super.db')
Session = sessionmaker(bind=engine)
session = Session()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    address = Column(String)

    orders = relationship('Order', back_populates='client')

    def __repr__(self):
        return f'Client(name={self.name}, age={self.age}, address={self.address})'

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    orders = relationship('Order', back_populates='product')

    def __repr__(self):
        return f'Product(name={self.name}, price={self.price})'

class Order(Base):
    __tablename__ = 'orders' 
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)

    client = relationship('Client', back_populates='orders')
    product = relationship('Product', back_populates='orders')

    def __repr__(self):
        return f'Order(id={self.id}, client_id={self.client_id}, product_id={self.product_id}, quantity={self.quantity}, total={self.total})'

Base.metadata.create_all(engine)

def create_client(name, age, address):
    client = Client(name=name, age=age, address=address)
    session.add(client)
    session.commit()
    print(f'Client {name} has been created')
    return client

def create_product(name, price):
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    print(f'Product {name} has been created')
    return product

def create_order(client_id, product_id, quantity, total):
    order = Order(client_id=client_id, product_id=product_id, quantity=quantity, total=total)
    session.add(order)
    session.commit()
    print(f'Order {order.id} has been created')
    return order

def get_clients():
    return session.query(Client).all()

def get_products():
    return session.query(Product).all()

def get_orders():
    return session.query(Order).all()

def get_client_orders(client_id):
    return session.query(Order).filter(Order.client_id == client_id).all()
