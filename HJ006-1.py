""" 
HJ6 质数因子
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）


数据范围： 1 \le n \le 2 \times 10^{9} + 14 \1≤n≤2×10 
9
 +14 
输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入：
180
复制
输出：
2 2 3 3 5 
"""



#输入一个正整数，并转为整形 # i = 2 num = 50 int(num**0.5)+1 = 8  i --> 2,8  49 % 7 == 0 print(7,end ' ' )  -> 7 空格 num = 8   
while True:
    try:
        num = int(input())
        for i in range(2,int(num**0.5)):
            while num%i==0:
                print(i,end=' ')
                num = int(num/i)
        if num>2:
            print(num)
        print('\n')
    except:
        break

