import logging
import os
from collections import namedtuple
import argparse
from time import sleep

class Catalog_separe:

    logging.basicConfig(filename='log-catalog.log',
                        filemode='w',
                        encoding='utf-8',
                        format='{levelname} >>> - {msg} >>> : {asctime} ',
                        style='{',
                        level=logging.INFO)

    logger = logging.getLogger(__name__)

    def __init__(self, dir='C:\_python\LEETCODE'):
        self.directory = dir

    def separate(self):
        data_list = [(dirs, folders, files) for dirs, folders, files in
                     os.walk(self.directory)]
        clas_list = []

        Data = namedtuple('Data',
                          ['file_name', 'file_exten', 'dir_flag', 'parent_dir'])
        for i in range(0, len(data_list)):
            parent_dir = data_list[i][0]
            dir_list = data_list[i][1]
            file_list = data_list[i][2]

            for el in dir_list:
                dir_flag = 'Yes'
                file_name = el
                file_exten = ''
                d = Data(file_name, file_exten, dir_flag, parent_dir)
                clas_list.append(d)
                self.logger.info(f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

            for item in file_list:
                dir_flag = 'No'
                try:
                    file_name, file_exten = item.split('.')
                except Exception:
                    *file_name, file_exten = item.split('.')

                d = Data(file_name, file_exten, dir_flag, parent_dir)
                clas_list.append(d)
                self.logger.info(
                    f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')
                return print(*clas_list, sep="\n")

Catalog_separe().separate()
sleep(1)
os.system('cls')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parsing')
    parser.add_argument('-a', metavar='dir_sep', type=str, help='entre directory', default='C:\_python\LEETCODE\OOP')
    args = parser.parse_args()
    print(Catalog_separe(args.a).separate())
    # sleep(1)
    # print(Catalog_separe("C:\_python\LEETCODE\OOP\06_logging").separate())

    # python \home_06_catalog.py -a="C:\_python\LEETCODE\OOP\06_logging"  #запуск через терминал
    # или в конфигурации прописать -a="C:\_python\LEETCODE\OOP\06_logging"

