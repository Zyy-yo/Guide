import pandas as pd
import jieba
'''
结巴分词：
    精确模式，试图将句子最精确地切开，适合文本分析；
    全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
    搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
'''
'''
jieba.cut()方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
jieba.cut_for_search()方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词。
    以上两种方法返回的结构都是一个可迭代的generator，可以使用for循环来获得分词后得到的每一个词语(unicode)，
    或者用jieba.lcut 以及jieba.lcut_for_search 直接返回 list
jieba.Tokenizer(dictionary=DEFAULT_DICT) ：新建自定义分词器，可用于同时使用不同词典。jieba.dt为默认分词器，所有全局分词相关函数都是该分词器的映射。
'''
a = jieba.cut('北京清华大学出版社')
print('精确模式:'+'/'.join(a))          # 精确模式:北京/清华大学出版社
b = jieba.cut('北京清华大学出版社', cut_all=True)
print('全模式:'+'/'.join(b))            # 全模式:北京/清华/清华大学/清华大学出版社/华大/大学/出版/出版社
c = jieba.cut_for_search('北京清华大学出版社')
print('搜索引擎模式:'+'/'.join(c))         # 搜索引擎模式:北京/清华/华大/大学/出版/出版社/清华大学出版社 

'''
词性标注：
    jieba.posseg模块,jieba.posseg.cut()
    名词：n 名词; nr 人名; nr1 汉语姓氏; nr2 汉语名字; nrj 日语名字; nrf 音译名字;
         ns 地名; nsf 音译地名; nt 机构团体名; nz 其他专名; nl 名词性惯用语; ng 名词性语素
    动词：v 动词; vd 副动词; vn 名动词; vshi 动词‘是’; vyou 动词‘有’; vf 趋向动词; 
         vx 形式动词; vi 不及物动词; vl 动词性惯用语; vg 动词性语素
    代词：r 代词; rr 人称代词; rz 指示代词; rzt 时间指示代词; rzs 处所指示代词; ry 疑问代词;
         rzv 谓词性指示代词; ryt 时间疑问代词; rys 处所疑问代词; ryv 谓词性疑问代词; rg 代词性语素
    助词：u 助词; uzhe 着; ule 了 喽; uguo 过; ude1 的 底; ude2 地; ude3 得; usuo 所;
         udeng 等 等等 云云; uyy 一样 一般 似的 般; udh 的话; uls 来讲 来说 而言 说来; uzhi 之; ulian 连
    时间词：t 时间词; tg 时间词性语素
    处所词：s 
    方位词：f
    形容词：a 形容词; ad 副形词; an 名形词; ag 形容词性语素; al 形容词性惯用词
    状态词：z
    数次：m 数次; mq 数量词
    量词：q 量词; qv 动量词; qt 时量词
    副词：d
    介词：p 介词; pba ‘把’; pbei ‘被'
    连词：c 连词; cc 并列连词
    叹词：e
    语气词：y
    拟声词：o
    前缀：h
    后缀：k
    字符串：x 字符串; xx 非语素字; xu 网址url
    标点：w 标点符号; wkz 左括号; wky 右括号; wyz 左引号; wyy 右引号; wj 句号; ww 问号; wt 叹号;
         wd 逗号; wf 分号; wn 顿号; wm 冒号; ws 省略号; wp 破折号; wb 百分号千分号; wh 单位符号
'''
import jieba.posseg as pseg
words = pseg.cut('可爱漂亮美丽大方。')
for word, flag in words:
    print('%s %s'%(word,flag))
# '''
# 可爱 v
# 漂亮 a
# 美丽大方 nr
# 。 x
# '''
# 👆词性分的不是很准确

# '''
# 关键词提取：
#     jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
#     sentence ：为待提取的文本
#     topK： 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
#     withWeight ： 为是否一并返回关键词权重值，默认值为 False
#     allowPOS ： 仅包括指定词性的词，默认值为空，即不筛选
# '''
import jieba.analyse
sen = '我想多少跟妹妹的情況有關吧。禰豆子好好一個女孩被迫變成了鬼，那其他鬼又是怎樣呢？會不會在變成鬼之前也只是個想平凡過生活的普通人……肯定很痛苦吧……'
keywords = jieba.analyse.extract_tags(sen, withWeight=True, allowPOS=(['n','a']))
print(keywords)
# 👆呃，不知道是基于什么来提取的，里面出现了3次的'鬼'就是不提取

d = pseg.lcut('鬼')		
print(d)				# [pair('鬼', 'n')]
