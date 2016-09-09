class word:
    """simple class for a word"""

    def __init__(self, word, length):
        # type: (object, object) -> object
        self.word = word
        self.length = length

# max line
max_line_width = 40
# holds all words
word_list = []


def main():
    # in and out files
    infile = open("input.txt", 'r')
    outfile = open("output.txt", 'w')

    for l in infile:
        # if there is a paragraph make a special paragraph word object
        if l =="\n" :
            word_list.append(word("\n", 0))
        # for each word make a word object
        for w in l.split():
            word_list.append(word(w, len(w)))

    # characters in the current line
    current_line = 0
    # characters in the current line
    line = ""
    for item in word_list:
        # special case for paragraphs
        if item.word is "\n":
            outfile.write(line.strip() + "\n\n")
            line = ""
            current_line = len(line)
            continue

        # add item to line
        if item.length + current_line <= max_line_width :
            line += item.word + " "
            current_line += item.length + 1

        # when the line is too large append to outfile
        else:
            line = line.strip() + "\n"
            outfile.write(line)
            line = ""
            line += item.word + " "
            current_line = len(line)
    # if there is still items in buffer write them
    if(line != ""):
        line.strip()
        outfile.write(line)

    # close outfile
    outfile.close()



if __name__ == '__main__':
    main()
