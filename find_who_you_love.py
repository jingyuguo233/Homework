import wordninja
import enchant
from os.path import exists, join
import pickle
from os import makedirs


lovewords = []
def get_love_words():
    d = enchant.Dict("en_US")
    #f = open("preprocess_csdn.txt", "r")  # 设置文件对象
    f = open("preprocess_yahoo.txt", "r")  # 设置文件对象
    line = f.readline()   #读取所有的txt文件数据
    line = line[:-1]
    while line:        # 直到读取完文件   一行一行的对数据进行处理
        str_love = ""
        #print(line)
        pwd = line.split(':')[1] #获取密码部分
        #pwd = line
        #print(pwd)
        all_words = wordninja.split(pwd)  #先分词
        #print(all_words)
        for i,word in enumerate(all_words):  #出现love之后再合词
            if(word.lower() == 'love'):
                ###如果出现了love，那么对所有的love后面的单词进行拼接 拼接完成之后直接读取下一行
                print("love is here!")
                for k in range(i+1,len(all_words)):
                    str_love += all_words[k]
                print(str_love)
                break
        if(len(str_love)>0):
            lovewords.append(str_love)
        line = f.readline()  # 读取一行文件，包括换行符
    f.close()  # 关闭文件
    print(lovewords)

def save_data():
#创建文件存储路径
    path = 'data/'
    if not exists(path):
        makedirs(path)
    print('Starting pickle to file...')
    #filename = 'test_text.txt'
    with open(join(path, 'all_love_words_yahoo.pkl'), 'wb') as f:
        pickle.dump(lovewords, f)  # 将x的index写入文件中
    print('Pickle finished')

#从pkl中恢复文件
def load_data():
    source_data = 'data/all_love_words_yahoo.pkl'
    with open(source_data, 'rb') as f:
        data_x = pickle.load(f)
        print(data_x)
    return data_x




get_love_words()
save_data()
load_data()
