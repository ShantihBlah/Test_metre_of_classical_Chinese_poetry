
#对输入的诗歌文件进行处理，使之成为能够处理的格式——分开每个字并将其组成列表
def do_file(file):
    def openfile(filename):
        fh = open(filename)
        wds = []
        for line in fh:
            line = line.rstrip()
            lst = line.split()
            for word in lst:
                if word not in wds:
                    wds.append(word)
        return wds
    poem = openfile(file)
    n = 0
    line_numbers = len(poem)
    poem_word = []
    while n < line_numbers:
        for word in poem[n]:
            if word not in ['，', '。']: #除掉“，”和“。”
                poem_word.append(word)
        n += 1
    return poem_word
    #print(poem_word,line_numbers)
