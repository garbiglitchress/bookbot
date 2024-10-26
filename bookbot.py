class Bookbot():
    def __init__(self,file):
        self.file=file
    def get_book_contents(self):
        with open(self.file) as f:
            file_contents=f.read()
        return file_contents#returns string of file data
    def word_count(self):
        file_contents=self.get_book_contents()
        print(len(file_contents.split()))
    def character_count(self):
        book_string=self.get_book_contents()
        book_string=book_string.strip()
        book_string=book_string.lower()
        char_dict={}
        for i in book_string:
            if i in char_dict.keys():
                char_dict[i]+=1
            else:
                char_dict[i]=1
        return char_dict
    def report(self):#takes a filename string
        print(f"--- Begin report of {self.file} ---")
        print('\n')
        char_data = self.character_count()
        nested_dict={}
        for i in char_data.items():
            nested_dict[i[0]]=i[1]
        sorted_by=dict(sorted(char_data.items(), key=lambda item: item[1], reverse=True))
        for i in sorted_by.items():
            if i[0].isalpha():
                print(f"The '{i[0]}' character was found {i[1]} times")
        print('--- End report ---')

    