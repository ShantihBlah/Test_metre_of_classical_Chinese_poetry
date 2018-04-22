#平仄表进行处理
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
all_table = [
             'wujue_zeqi_0.txt', 'wujue_zeqi_1.txt',
             'wujue_pingqi_0.txt', 'wujue_pingqi_1.txt',
             'qijue_zeqi_0.txt', 'qijue_zeqi_1.txt',
             'qijue_pingqi_0.txt', 'qijue_pingqi_1.txt',
             'wulv_zeqi_0.txt', 'wulv_zeqi_1.txt',
             'wulv_pingqi_0.txt', 'wulv_pingqi_1.txt',
             'qilv_zeqi_0.txt', 'qilv_zeqi_1.txt',
             'qilv_pingqi_0.txt', 'qilv_pingqi_1.txt'
             ]                           #该列表一定要按顺序排列，可按需添加其他规则
poem = openfile('rule\gelv_poem/' + all_table[0])
rule_table = []
for table_of_pingze in all_table:
    poem = openfile('rule\gelv_poem/' + table_of_pingze)
    n = 0
    line_numbers = len(poem)
    poem_word = []
    while n < line_numbers:
        for word in poem[n]:
            if word not in [',','.',
                            '，', '。'
                            ]:               #除掉“,”、“.”、“，”和“。”，可按需添加
                poem_word.append(word)
        n += 1
    m = 0
    rule_list = []
    while m < len(poem_word):
        if poem_word[m] == '仄':
            rule_list.append(m)
        m += 1
    rule_table.append(rule_list)

#print(rule_table)
