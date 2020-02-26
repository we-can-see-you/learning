# !/usr/bin/python3
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser()
# 调用add_argument添加参数
parser.add_argument("--square", help="display a square of a given number", type=int)
parser.add_argument("--cubic", help="display a cubic of a given number", type=int)

# 使用parse_args解析命令行输入的参数
args = parser.parse_args()

if args.square:
    print(args.square**2)

if args.cubic:
    print(args.cubic**3)
