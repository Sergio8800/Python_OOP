from date import user_date
import argparse
from datetime import datetime

# Edit configurations прописываем параменты через пробел, -cnt=3-я -wd=среда -m=ноября
parser = argparse.ArgumentParser(description="Принимаем строку с датой")
parser.add_argument('-cnt', type=str, default='1')
parser.add_argument('-wd', type=str, default=str(datetime.now().weekday()))
parser.add_argument('-m', type=str, default=str(datetime.now().month))
args = parser.parse_args()
print(args)
print(user_date(f'{args.cnt} {args.wd} {args.m}'))
