""" HJ9 提取不重复的整数
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。

数据范围： 1 \le n \le 10^{8} \1≤n≤10 
8
  
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数 """
num=input()
num=num[::-1]
n=len(num)
str_=''
for i in range(n):
    if num[i] not in str_:
        str_+=num[i]
print(str_)
