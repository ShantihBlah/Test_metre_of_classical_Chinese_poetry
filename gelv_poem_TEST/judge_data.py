
import get_rules as gr             #导入平仄规则表——tule_table

#==============================================================
#==========================判断类型=============================
#==============================================================

#根据字数判断目标诗歌类型：五绝——20，七绝——28，五律——40，七律——56
def poemtype(poem):
    standard = len(poem)
    if standard == 20:
        type = '五绝'
    elif standard == 28:
        type = '七绝'
    elif standard == 40:
        type = '五律'
    elif standard == 56:
        type = '七律'
    else:
        type = 'ERROR'
    return type


#==============================================================
#========================韵部检测单元===========================
#==============================================================

def yunbu_test(poem, type, type_of_gelv,
               pingyun, zeyun):
    '''
    功能: 判断韵脚所在韵部
    结果: 结果以列表形式导出
    '''
    if type in ['五绝','七绝']:
        if type == '五绝':
            add_of_yun = [4, 9, 19]
        else:
            add_of_yun = [6, 13, 27]
        if type_of_gelv in ['首句入韵', 'Y']:
            pingyun_list = list(pingyun.keys())
            zeyun_list = list(zeyun.keys())
            yun0 = [poem[add_of_yun[0]]]
            yun1 = [poem[add_of_yun[1]]]
            yun2 = [poem[add_of_yun[2]]]
            yun = []

            #检测韵部
            for yun_key in pingyun_list:
                if poem[add_of_yun[0]] in pingyun[yun_key]:
                    yun0.append(yun_key)
                if poem[add_of_yun[1]] in pingyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in pingyun[yun_key]:
                    yun2.append(yun_key)
            for yun_key in zeyun_list:
                if poem[add_of_yun[0]] in zeyun[yun_key]:
                    yun0.append(yun_key)
                if poem[add_of_yun[1]] in zeyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in zeyun[yun_key]:
                    yun2.append(yun_key)
            if len(yun0) == 1:
                yun0.append('未入韵')
            if len(yun1) == 1:
                yun1.append('未入韵')
            if len(yun2) == 1:
                yun2.append('未入韵')
            yun = [yun0, yun1, yun2]
        else:
            pingyun_list = list(pingyun.keys())
            zeyun_list = list(zeyun.keys())
            yun1 = [poem[add_of_yun[1]]]
            yun2 = [poem[add_of_yun[2]]]
            yun = []

            #检测韵部
            for yun_key in pingyun_list:
                if poem[add_of_yun[1]] in pingyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in pingyun[yun_key]:
                    yun2.append(yun_key)
            for yun_key in zeyun_list:
                if poem[add_of_yun[1]] in zeyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in zeyun[yun_key]:
                    yun2.append(yun_key)
            if len(yun1) == 1:
                yun1.append('未入韵')
            if len(yun2) == 1:
                yun2.append('未入韵')
            yun = [yun1, yun2]
    elif type in ['五律','七律']:
        if type == '五律':
            add_of_yun = [4, 9, 19, 29, 39]
        else:
            add_of_yun = [6, 13, 27, 41, 55]
        if type_of_gelv in ['首句入韵', 'Y']:
            pingyun_list = list(pingyun.keys())
            zeyun_list = list(zeyun.keys())
            yun0 = [poem[add_of_yun[0]]]
            yun1 = [poem[add_of_yun[1]]]
            yun2 = [poem[add_of_yun[2]]]
            yun3 = [poem[add_of_yun[3]]]
            yun4 = [poem[add_of_yun[4]]]
            yun = []

            #检测韵部
            for yun_key in pingyun_list:
                if poem[add_of_yun[0]] in pingyun[yun_key]:
                    yun0.append(yun_key)
                if poem[add_of_yun[1]] in pingyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in pingyun[yun_key]:
                    yun2.append(yun_key)
                if poem[add_of_yun[3]] in pingyun[yun_key]:
                    yun3.append(yun_key)
                if poem[add_of_yun[4]] in pingyun[yun_key]:
                    yun4.append(yun_key)
            for yun_key in zeyun_list:
                if poem[add_of_yun[0]] in zeyun[yun_key]:
                    yun0.append(yun_key)
                if poem[add_of_yun[1]] in zeyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in zeyun[yun_key]:
                    yun2.append(yun_key)
                if poem[add_of_yun[3]] in zeyun[yun_key]:
                    yun3.append(yun_key)
                if poem[add_of_yun[4]] in zeyun[yun_key]:
                    yun4.append(yun_key)
            if len(yun0) == 1:
                yun0.append('未入韵')
            if len(yun1) == 1:
                yun1.append('未入韵')
            if len(yun2) == 1:
                yun2.append('未入韵')
            if len(yun3) == 1:
                yun3.append('未入韵')
            if len(yun4) == 1:
                yun4.append('未入韵')
            yun = [yun0, yun1, yun2, yun3, yun4]
        else:
            pingyun_list = list(pingyun.keys())
            zeyun_list = list(zeyun.keys())
            yun1 = [poem[add_of_yun[1]]]
            yun2 = [poem[add_of_yun[2]]]
            yun3 = [poem[add_of_yun[3]]]
            yun4 = [poem[add_of_yun[4]]]
            yun = []

            #检测韵部
            for yun_key in pingyun_list:
                if poem[add_of_yun[1]] in pingyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in pingyun[yun_key]:
                    yun2.append(yun_key)
                if poem[add_of_yun[3]] in pingyun[yun_key]:
                    yun3.append(yun_key)
                if poem[add_of_yun[4]] in pingyun[yun_key]:
                    yun4.append(yun_key)
            for yun_key in zeyun_list:
                if poem[add_of_yun[1]] in zeyun[yun_key]:
                    yun1.append(yun_key)
                if poem[add_of_yun[2]] in zeyun[yun_key]:
                    yun2.append(yun_key)
                if poem[add_of_yun[3]] in zeyun[yun_key]:
                    yun3.append(yun_key)
                if poem[add_of_yun[4]] in zeyun[yun_key]:
                    yun4.append(yun_key)
            if len(yun1) == 1:
                yun1.append('未入韵')
            if len(yun2) == 1:
                yun2.append('未入韵')
            if len(yun3) == 1:
                yun3.append('未入韵')
            if len(yun4) == 1:
                yun4.append('未入韵')
            yun = [yun1, yun2, yun3, yun4]
    return yun

#==============================================================
#==========================输出单元=============================
#==============================================================

def output_result(words, type,
                  type_of_gelv, yun=0):
    '''
    功能：输出原诗及检测后的诗，可选择是否输出韵部。
        words: 将诗的列表（只有字）输入进来；
        type: 诗歌类型，判断输出格式；
        type_of_gelv: 格律类型，判断输出格式；
        yun: 将之前提取到的韵脚输进来，有即输出，
             没有就默认为零，用于只输出原诗。
    '''
    result = ''
    for word in words:
        result += word
    #print('\n平仄检测:')
    if type in ['五绝', '七绝']:
        if type == '五绝':
            print('\n{0}，\n{1}。\n{2}，\n{3}。\n'.\
                format(result[0:5], result[5:10],
                       result[10:15], result[15:20]))
        else:   #输出七绝
            print('\n{0}，\n{1}。\n{2}，\n{3}。\n'.\
                format(result[0:7], result[7:14],
                       result[14:21], result[21:28]))
        if yun != 0:
            if type_of_gelv in ['首句入韵', 'Y']:
                print('\n{0}: {1}\n{2}: {3}\n{4}: {5}\n'.\
                    format(yun[0][0], yun[0][1:],
                           yun[1][0], yun[1][1:],
                           yun[2][0], yun[2][1:]))
            else:
                print('\n{0}: {1}\n{2}: {3}\n'.\
                    format(yun[0][0], yun[0][1:],
                           yun[1][0], yun[1][1:]))

    else:
        if type == '五律':
            print('\n{0}，{1}。\n{2}，{3}。\n{4}，{5}。\n{6}，{7}。\n'.\
                format(result[0:5], result[5:10],
                       result[10:15], result[15:20],
                       result[20:25], result[25:30],
                       result[30:35], result[35:40]))
        else:   #输出七律
            print('\n{0}，{1}。\n{2}，{3}。\n{4}，{5}。\n{6}，{7}。\n'.\
                format(result[0:7], result[7:14],
                       result[14:21], result[21:28],
                       result[28:35], result[35:42],
                       result[42:49], result[49:56]))
        if yun != 0:
            if type_of_gelv in ['首句入韵', 'Y']:
                print('\n{0}: {1}\n{2}: {3}\n{4}: {5}\n{6}: {7}\n{8}: {9}\n'.\
                    format(yun[0][0], yun[0][1:],
                           yun[1][0], yun[1][1:],
                           yun[2][0], yun[2][1:],
                           yun[3][0], yun[3][1:],
                           yun[4][0], yun[4][1:]))
            else:
                print('\n{0}: {1}\n{2}: {3}\n{4}: {5}\n{6}: {7}\n'.\
                    format(yun[0][0], yun[0][1:],
                           yun[1][0], yun[1][1:],
                           yun[2][0], yun[2][1:],
                           yun[3][0], yun[3][1:]))


#==============================================================
#========================平仄判断单元===========================
#==============================================================

def get_test_of_pingze(poem, type_of_poem, type_of_pingze,
                       type_of_gelv, pingsheng, zesheng):
    '''
    功能: 判断每个字的平仄，符合要求原样保存，不符合改为☺
    注意: 在命令行窗口里，☺显示为大方框
    结果：结果以列表形式导出
    '''
    WUJUEZEQI_0 = gr.rule_table[0]                 #接受get_rules.py的值
    WUJUEZEQI_1 = gr.rule_table[1]
    WUJUEPINGQI_0 = gr.rule_table[2]
    WUJUEPINGQI_1 = gr.rule_table[3]
    QIJUEZEQI_0 = gr.rule_table[4]
    QIJUEZEQI_1 = gr.rule_table[5]
    QIJUEPINGQI_0 = gr.rule_table[6]
    QIJUEPINGQI_1 = gr.rule_table[7]
    WULVZEQI_0 = gr.rule_table[8]
    WULVZEQI_1 = gr.rule_table[9]
    WULVPINGQI_0 = gr.rule_table[10]
    WULVPINGQI_1 = gr.rule_table[11]
    QILVZEQI_0 = gr.rule_table[12]
    QILVZEQI_1 = gr.rule_table[13]
    QILVPINGQI_0 = gr.rule_table[14]
    QILVPINGQI_1 = gr.rule_table[15]
    if type_of_poem == '五绝':
        len_of_poem = 20
        if type_of_pingze in ['仄起', '1']:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = WUJUEZEQI_1
            else:
                add_of_zesheng = WUJUEZEQI_0
        else:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = WUJUEPINGQI_1
            else:
                add_of_zesheng = WUJUEPINGQI_0
    elif type_of_poem == '七绝':
        len_of_poem = 28
        if type_of_pingze in ['仄起', '1']:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = QIJUEZEQI_1
            else:
                add_of_zesheng = QIJUEZEQI_0
        else:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = QIJUEPINGQI_1
            else:
                add_of_zesheng = QIJUEPINGQI_0
    elif type_of_poem == '五律':
        len_of_poem = 40
        if type_of_pingze in ['仄起', '1']:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = WULVZEQI_1
            else:
                add_of_zesheng = WULVZEQI_0
        else:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = WULVPINGQI_1
            else:
                add_of_zesheng = WULVPINGQI_0
    elif type_of_poem == '七律':
        len_of_poem = 56
        if type_of_pingze in ['仄起', '1']:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = QILVZEQI_1
            else:
                add_of_zesheng = QILVZEQI_0
        else:
            if type_of_gelv in ['首句入韵', 'Y']:
                add_of_zesheng = QILVPINGQI_1
            else:
                add_of_zesheng = QILVPINGQI_0
    m = 0
    while m < len_of_poem:
        if m in add_of_zesheng:
            if poem[m] in zesheng:
                poem[m] = poem[m]    #应符合且符合仄声则输出原字
            else:
                poem[m] = '☺'        #应符合而不符合仄声的输出奇怪字符（cmd上显示方框）
        else:
            if poem[m] in pingsheng:
                poem[m] = poem[m]    #应符合且符合平声则输出原字
            else:
                poem[m] = '☺'        #应符合而不符合平声的输出奇怪字符（cmd上显示方框）
        m += 1
    return poem
