""" HJ8 合并表记录

描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
然后输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

示例1
输入：
4
0 1
0 2
1 2
3 4
复制
输出：
0 3
1 2
3 4
复制
示例2
输入：
3
0 1
0 2
8 9
复制
输出：
0 3
8 9 """
n= int(input())
d = {}
for i in range(n):
    ab = input().split(" ")
    a,b = int(ab[0]), int(ab[-1])
    if a not in d:
        d[a] = b
    elif a in d:
        d[a] = d[a] + b
for i in sorted(d.keys()):
    print(i,d[i])
