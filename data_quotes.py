from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import constant

engine = create_engine(f'sqlite:///{constant.DBQUOTES}', connect_args={'check_same_thread': False}, echo=False)

Session = sessionmaker(bind=engine)
Base = declarative_base()


# Define the Motivational Quote class
class MotivationalQuote(Base):
    __tablename__ = 'motivational_quotes'
    id = Column(Integer, primary_key=True)
    quote = Column(String)
    author = Column(String)


# Create the database table
Base.metadata.create_all(engine)

# Create a list of motivational quotes to add to the database
quotes = [
    {'quote': 'Believe you can and you\'re halfway there.', 'author': 'Theodore Roosevelt'},
    {'quote': 'Strive not to be a success, but rather to be of value.', 'author': 'Albert Einstein'},
    {'quote': 'The only way to do great work is to love what you do.', 'author': 'Steve Jobs'},
    {'quote': 'Don\'t let yesterday take up too much of today.', 'author': 'Will Rogers'},
]

# Add the quotes to the database
session = Session()
for quote in quotes:
    new_quote = MotivationalQuote(quote=quote['quote'], author=quote['author'])
    session.add(new_quote)
session.commit()


def get_quote():
    random_quote = session.query(MotivationalQuote).order_by(func.random()).first()

    # Print the quote and author
    return f'\"{random_quote.quote}\" \n by {random_quote.author}'


# Close the session
session.close()
