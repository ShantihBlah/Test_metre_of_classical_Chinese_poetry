import pingzeyilan
import get_data as gd
import get_aim_poem
import judge_data

print('\n#欢迎使用简易的诗词格律检测器，现在仅支持平水韵——格律诗\
       \n 其他功能正在开发中，敬请期待#\
       \n\n=======================格律检测======================\n\n')
#get_file = 'example/' + input('请输入包含欲检测诗歌的文件名：') #输入时不加引号
get_file = 'objective/' + input('请输入包含欲检测诗歌的文件名：')
poem = get_aim_poem.do_file(get_file)
type_of_poem = judge_data.poemtype(poem)

if type_of_poem in [
           '五绝', '七绝',
           '五律', '七律'
           ]:
    print('检测到旧体诗类型：{0}'.format(type_of_poem))
    type_of_pingze = input('选择{0}平仄类型[仄起[1]、平起[2]]:'.format(type_of_poem))
    type_of_gelv = input('选择{0}入韵类型[首句入韵[Y]、首句不入韵[N]]:'.\
                       format(type_of_poem))
    #得到韵的列表
    yun_word = judge_data.yunbu_test(poem, type_of_poem, type_of_gelv,
                                     gd.yunbu_ping, gd.yunbu_ze)
    #得到判断平仄后的诗歌
    result = judge_data.get_test_of_pingze(poem, type_of_poem,
                                           type_of_pingze, type_of_gelv,
                                           gd.all_pingsheng, gd.all_zesheng)
    #整体输出，可放后面
    poem1 =  get_aim_poem.do_file(get_file)
    print('\n__原诗:')
    judge_data.output_result(poem1, type_of_poem,
                             type_of_gelv)
    print('\n__检测后:')
    judge_data.output_result(result, type_of_poem, type_of_gelv, yun_word)

else:
    print(type_of_poem, ': 请检查文件后再输入')


#查看平仄一览
cho_look = input('是否要查看平仄一览（是（Y）或否（其他）：')
if cho_look in ['Y', 'y', '是']:
    pingzeyilan.outpingze()

while 1:
    ask_quit = input('是否退出程序: ')
    if ask_quit in ['是', '1', 'Y', 'y']:
        quit()
