from database import SessionLocal
from models import Book, User

db = SessionLocal()


def seed():
    book_titles = [
        '深層学習教科書 ディープラーニング G検定(ジェネラリスト) 公式テキスト',
        '詳解ディープラーニング',
        'PythonとKerasによるディープラーニング'
    ]
    books = [Book(title=title) for title in book_titles]

    user = User(username='yusugomori')
    user.books = books

    db.add(user)
    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()
