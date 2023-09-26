class CustomFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# Create a student file
with CustomFileManager("student.txt", "w") as file:
    file.write("\n supersonic sonicLabs")
    file.write("\n supertest testinc labs")


# Read file
with CustomFileManager("student.txt", "r") as file:
    for student in file.readlines():
        # Clone file
        with CustomFileManager("studentCopy.txt", "a") as innerFile:
            innerFile.write(f'\n {student.upper()}')


