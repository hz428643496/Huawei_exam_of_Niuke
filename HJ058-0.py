'''HJ58 输入n个整数，输出其中最小的k个
描述
输入n个整数，找出其中最小的k个整数并按升序输出

本题有多组输入样例

数据范围：1 \le n \le 1000 \1≤n≤1000  ，输入的整数满足 1 \le val \le 10000 \1≤val≤10000 
输入描述：
第一行输入两个整数n和k
第二行输入一个整数数组

输出描述：
从小到大输出最小的k个整数，用空格分开。

示例1
输入：
5 2
1 3 5 7 2
复制
输出：
1 2

'''

while True:
    try:
        n, k = map(int, input().split())
        nums = sorted(list(map(int, input().split())))
        print(*nums[:k])
    except:
        break
# def f(x):
#  return x*x
# print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))