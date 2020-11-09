import wordninja
import enchant
from os.path import exists, join
import pickle
from os import makedirs
#step1：提取出密码序列中所有的英文单词并重新存储到一pkl个文件中
    ##1.采用wordninja来对密码序列进行划分，可以对密码序列划分为字母、拼音、数字等序列
        ##需要注意的是但wordninja无法提取特殊符号
    ##2.挑选出序列中所有正确的英文单词，排除掉与字母表中重复的部分，
        ##将其存入all_english_words的文件中
    ##注意！！运行前请先修改读取的文件数据名以及保存的文件名

all_enwords = []
pinyin = []
all_words_without_pinyin = []

def get_all_pinyin():
    for line in open("data/pinyin.txt", "r"):  # 设置文件对象并读取每一行文件
        pinyin.append(line[:-1])

def get_english_words():
    d = enchant.Dict("en_US")
    f = open("preprocess_yahoo.txt", "r")  # 设置文件对象
    #f = open("data.txt","r")
    #f = open("preprocess_yahoo.txt", "r")  # 设置文件对象
    line = f.readline()   #读取所有的txt文件数据
    line = line[:-1]
    print("Reading text...")
    while line:        # 直到读取完文件   一行一行的对数据进行处理
        pwd = line.split(':')[1]
        #pwd = line.split('#')[1]
        #pwd = line
        all_words = wordninja.split(pwd)
        for word in all_words:
            if(( word.lower() not in pinyin) and d.check(word) and word.isalpha() and len(word)>2):
                all_enwords.append(word.lower())
                print(word.lower())
        line = f.readline()  # 读取一行文件，包括换行符
    f.close()  # 关闭文件
    print("Reading Finished!")

def save_data():
#创建文件存储路径
    path = 'data/'
    if not exists(path):
        makedirs(path)
    print('Starting pickle to file...')

    filename = 'test_text.txt'
    #with open(join(path, 'all_english_yahoo.pkl'), 'wb') as f:
    with open(join(path, 'all_english_tosmall_yahoo.pkl'), 'wb') as f:
        pickle.dump(all_enwords, f)  # 将x的index写入文件中
    print('Pickle finished')

#从pkl中恢复文件
def load_data():
    #source_data = 'data/all_english_yahoo.pkl'
    source_data = 'data/all_english_tosmall_yanhoo.pkl'
    with open(source_data, 'rb') as f:
        data_x = pickle.load(f)
        #print(data_x)
    return data_x

get_all_pinyin()
get_english_words()
save_data()
load_data()
