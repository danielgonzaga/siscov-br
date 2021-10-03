from models import *


db.init_app(serv)


def main():
    db.create_all()


if __name__ == "__main__":
    main()
