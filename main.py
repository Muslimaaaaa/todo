from models import User
from models import Todo

def main():
    web = input("""
        1. Login
        2. Register
            >>> """)

    if web == "1":
        return User()

    elif web == "2":
         return Todo()

    else:
        print("Xatolik iltimos qaytadan urining")
        return main()

if __name__ == "__main__":
    main()