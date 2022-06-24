#HJ40 统计字符
""" 描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000 

输入描述：
输入一行字符串，可以有空格

输出描述：
统计其中 英文字符，空格字符，数字字符，其他字符的个数 """
#考察类型的判断
#isalpha()
#isspace()
#isdigit()
#isalnum()

str = input()
a,b,c,d = 0,0,0,0
for i in str:
    if i.isalpha():
        a +=1
    elif i.isspace():
        b +=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
print(a,b,c,d,sep='\n')
