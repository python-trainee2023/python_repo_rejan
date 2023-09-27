# class CustomFileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# # Create a student file
# with CustomFileManager("student.txt", "w") as file:
#     file.write("\n supersonic sonicLabs")
#     file.write("\n supertest testinc labs")
#
#
# # Read file
# with CustomFileManager("student.txt", "r") as file:
#     for student in file.readlines():
#         # Clone file
#         with CustomFileManager("studentCopy.txt", "a") as innerFile:
#             innerFile.write(f'\n {student.upper()}')

#
# authors = [
#     ("William Shakespear", ["Hamlet", "Julius Caesar", "Romeo and Juliet"]),
#     ("JK Rowling", ["Harry Potter series", "Fantastic Beasts series"],)]

#
# authors = [{
#     "William Shakespear": {
#         "books": ["Hamlet", "Julius Caesar", "Romeo and Juliet"]
#     },
#     "JK Rowling": {
#         "books": ["Harry Potter series", "Fantastic Beasts series"]
#     }
# }]
#
# with open("books.txt", "w") as source_file:
#     for author in authors:
#         for key,value, in author.items():
#             temp = f"Author: {key} Books: "
#             for book in value.values():
#                 temp+=f"{book}"
#             temp+="\n"
#             source_file.write(temp)


def author_search(name):
    try:
        book_list = []
        with open("books.txt", "r") as source:
            for record in source:
                author, book = record.strip().split(',')
                if name == author:
                    book_list.append(book)

        if(len(book_list) > 0):
            print(f"authr: {name}")
            for book in book_list:
                print(f"title: {book}")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(str(e))




author_name = input("Enter the author to find ?")
author_search(author_name.lower())

