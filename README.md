# Homework
## find_english_words.py
    本程序的目的是提取出口令中所包含的英文单词，即：
    输入：password123!
    输出：password
    
    输入：zhaoloveguo1314
    输出：love
### 实现思路及方法
##### def get_english_words():
    0.按行读取preprocess_csdn.txt/preprocess_yahoo.txt中的所有口令，口令存储的格式为：
    CSDN:用户名#口令#登录邮箱
    Yahoo：用户名:口令
    1.使用wordninja分词工具来对口令进行“分词”，即对口令的各个组成部分进行划分，效果如下：
    pwd = “password123!”
    words_of_pwd = ['password','123']
    2.接下来在word_of_pwd中收集所有的正确单词，在本步骤中采用的是enchant工具，该工具的使用效果     如下：
      d = enchant.Dict("en_US")
      >>d.check("password")
      True
      >>d.check("123")
      False
     因此使用该工具可以挑选出word_of_pwd中所有正确的英文单词，保存在all_enwords这个list中
     3.但经过实验发现，该工具在使用中会出现误将中文拼音识别成英文单词的情况，比如：
      d = enchant.Dict("en_US")
      >>d.check("jun")
      True
      >>d.check("ming")
      True
     因此，需要进一步对enchant提取出来的英文单词进行进一步的筛选，筛选的准则即为若该“单词”出现在拼音表中，则不将其视为英文单词进行挑选和存储，这样可减少大量的拼音被误认为英文单词的情况（特别是在CSDN数据集中）
#### def save_data():
    对数据进行存储，存储的格式为pkl文件，该文件无需将python对象转化成字符串即可进行存储，因此本程序保存的格式即为list对象all_enwords
#### def load_data():
    对数据进行加载，将返回所有口令英文单词的list对象
### 数据集及实验环境配置
#### 工具库
      1.wordninja：用于实现口令中不同元组组成的划分
      2.enchant：用于识别正确地英文单词
      3.pickle：用于生成、加载pkl文件
#### 数据集
      1.CSDN口令数据集，文件名为“preprocess_csdn.txt”
      2.Yahoo口令数据集，文件名为“preprocess_yahoo.txt”
      3.拼音表，文件名为“pinyin.txt”
#### 实验配置及结果
      本程序需要在程序源代码中修改相应的数据集文件及保存的数据文件名才能生成不同数据集不同类型的文件，具体说明如下：
      1.生成csdn的数据文件，需要修改的地方有三处：
          #设置读取的文件数据
          f = open("preprocess_yahoo.txt", "r")       （位于def get_english()）
          #设置保存的文件数据 存取口令集中所有的英文单词
          with open(join(path, 'all_english_tosmall_yahoo.pkl')(位于def savedata())
          source_data = 'all_english_tosmall_yanhoo.pkl'(位于def loaddata())
      2.同理，生成yahoo的数据文件同样需要修改这三条语句：
          f = open("preprocess_yahoo.txt", "r")       （位于def get_english()）
          with open(join(path, 'all_english_tosmall_yahoo.pkl')(位于def savedata())
          source_data = 'all_english_tosmall_yanhoo.pkl'(位于def loaddata())
      此外，本程序提取英文单词的目的是为了进行词频的top统计，由于英文字母的大小写不影响单词的语义，因此本程序统一将英文单词转化成小写进行处理。
        对本程序进行相应的修改后可得到以下几个文件：
        1.all_english_tosmall_yahoo.pkl：yahoo口令集里所有的英文单词
        2.all_english_tosmall_csdn.pkl：csdn口令集里所有的英文单词

      
