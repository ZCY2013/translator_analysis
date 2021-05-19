# coding: utf-8
import re

my_file_path = "resources/haryy_potter.txt"
save_file_path = "resources/haryy_potter_pure.txt"

if __name__ == '__main__':

    # 打开文件
    my_file = open(my_file_path, 'r')
    # 只保留中英文、数字和.的正则表达式
    cop = re.compile("[^a-z^A-Z^\n^ ]")

    save_file = open(save_file_path, 'w+')
    i = 0
    line = my_file.readline()
    while line != '':
        print(line)
        m_string = cop.sub('', line)
        save_file.write(m_string)
        save_file.flush()
        line = my_file.readline()
    save_file.close()
    my_file.close()

