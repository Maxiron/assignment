def read_file_reverse(filename):
       with open(filename) as f:
              rev_output = f.readlines()
              # output = list(output)
       return rev_output[::-1]
def read_file_content(filename):
    with open(filename) as f:
       output = f.readlines()
       # output = list(output)
    return output
def count_words():
    text = read_file_content("new.txt")
    word_count = {}
    char_count = {}
    for line in text:
       for word in line.split():  
              word_count[word] = 1 + word_count.get(word, 0)
              for char in word:
                     char_count[char] = 1 + char_count.get(char, 0)

    return word_count,  char_count
print(count_words())
print(read_file_reverse("new.txt"))