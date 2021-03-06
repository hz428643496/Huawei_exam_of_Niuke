'''HJ12 字符串反转
描述
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

输入描述：
输入一行，为一个只包含小写字母的字符串。

输出描述：
输出该字符串反转后的字符串。

示例1
输入：
abcd

输出：
dcba
'''
#切片的用法 strip()去除尾部空格或者换行
#Python中的[::-1] 
# b = a[i:j] 表示复制a[i]到a[j-1]，以生成新的list对象
# 当i缺省时，默认为0，即 a[:3]相当于 a[0:3]
# 当j缺省时，默认为len(alist), 即a[1:]相当于a[1:10]
# 当i,j都缺省时，a[:]就相当于完整复制一份a了
# b = a[i:j:s]这种格式呢，i,j与上面的一样，但s表示步进，缺省为1.
# 所以a[i:j:1]相当于a[i:j]
# 当s<0时：i缺省时，默认为-1； j缺省时，默认为-len(a)-1
# 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。
print(input().strip().lower()[::-1])




