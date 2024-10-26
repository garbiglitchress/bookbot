from bookbot import *
import os.path
def main():
    file_name=input('Enter filepath containing text you want analyzed.')
    if os.path.isfile(file_name):
        books=Bookbot(file_name)
    else:
        raise FileNotFoundError
    books.report()

        

if __name__=="__main__":
    main()
