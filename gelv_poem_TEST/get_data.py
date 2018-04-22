
#读取文件
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

#将分块的字符串合成一个字符串，并将其拆成每一个字符后装入all列表中
def section2all(wds):
    n = 0
    transition = []
    yunbu = []
    all = []
    while n < len(wds):
        if n % 2 == 1:
            transition.append(wds[n])
        else:
            yunbu.append(wds[n])
        n += 1
    yunbu_yun = dict(zip(yunbu,transition)) #将各大韵部和对应的字装成字典dict
    ensemble = ''
    for section in transition:
        ensemble += section
    for word in ensemble:
        all.append(word)
    return all, yunbu_yun


wds_pingsheng = openfile('sound/pingsheng.txt')
wds_zesheng = openfile('sound/zesheng.txt')
[all_pingsheng,yunbu_ping] = section2all(wds_pingsheng)     #得到平韵
[all_zesheng,yunbu_ze] = section2all(wds_zesheng)           #得到仄韵
