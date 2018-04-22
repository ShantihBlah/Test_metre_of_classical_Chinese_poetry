#把平仄文件打开并分类输出
def outpingze():

    #读取文件函数
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


    #输出平声的标题
    def print_title_1(wds):
        title = wds[0]
        shangping = wds[2].split('、')
        xiaping = wds[4].split('、')
        print('\n','\n',15 * '*','\n',' ——',title,'——','\n',15 * '*','\n')
        return shangping,xiaping


    #输出仄声的标题
    def print_title_2(wds):
        title = wds[0]
        zesheng = wds[1].split('、')
        print('\n','\n',15 * '*','\n',' ——',title,'——','\n',15 * '*','\n')
        return zesheng


    #输出每个韵部及框架
    def print_element(shengyun_list,fenlei = 0):
        if fenlei != 0 :
            print(fenlei,':\n')
        print(' ================')
        for element in shengyun_list:
            if len(element) < 3:
                print(' ||   ', element, '   ||')
            elif len(element) == 3:
                print(' ||  ', element, '  ||')
            else:
                print(' || ', element, ' ||')
        print(' ================\n')


    #输出平声
    wds_ping = openfile('sound/pingshengyilan.txt')
    [shangping,xiaping] = print_title_1(wds_ping)
    print_element(shangping,wds_ping[1])
    print_element(xiaping,wds_ping[3])

    #输出上声
    wds_shang = openfile('sound/shangshengyilan.txt')
    print_element(print_title_2(wds_shang))

    #输出去声
    wds_qu = openfile('sound/qushengyilan.txt')
    print_element(print_title_2(wds_qu))

    #输出入声
    wds_ru = openfile('sound/rushengyilan.txt')
    print_element(print_title_2(wds_ru))
