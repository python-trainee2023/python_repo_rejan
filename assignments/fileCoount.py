try:
    count = 0
    with open('student.txt', 'r') as source:
        for line in source:
            word_list = line.strip().split(' ')
            for word in word_list:
                if(word.endswith('e')):
                    count = count + 1

    print(f"Total words ending with e: {count}")
except Exception as e:
    print(f"Exception {str(e)}")

