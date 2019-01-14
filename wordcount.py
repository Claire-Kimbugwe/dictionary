def count_words(filename):

    file = open(filename)
    word_dict = {}
    

    for line in file:
        line = line.rstrip()
        line = line.split()

        for word in line:
            word_dict[word] = word_dict.get(word, 0) + 1

    file.close()
    
    return word_dict

print(count_words("twain.txt"))# put your code here.
