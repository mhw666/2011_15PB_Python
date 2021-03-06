# 列表的基础知识: 内置的序列类型，可以看作是加强版本的数，通过中括号
# [] 进行定义，其中不要求元素的类型是一致的，并且长度是可变的
print([1, 2, 3, 4, 5], type([]))
print([1, 1.1, '1', [1]])

# 算数运算
print([1] + [2])        # 将参与运算的列表组合成新的列表
print([1, 2] * 3)       # 将列表的元素重复 3 次
print(3 in [0, 1, 2])   # 判断是否在列表中
print([1, 2, 3] == [3, 2, 1])   # 比较运算符

# 全局函数
print(len([1, 2, 3]))
print(min([1, 2, 3]))
print(max([1, 2, 3]))
print(list(reversed([1, 2, 3])))
print(list(sorted([1, 2, 3])))

# 内置方法
l = [1, 2, 3, 4, 5]
l.append(6)
print(l)        # 在结尾添加元素
l.insert(0, 0)
print(l)        # 在指定位置添加
l.remove(3)
print(l)        # 删除某元素(元素)
l.pop(0)
print(l)        # 删除某元素(索引)，返回删除的内容
l.extend([1,2,3,4])
print(l)        # 类似列表的加法运算符

# 切片操作(序列操作)  l[a:b:c]
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[:3], l[:4])         # [起始位置, 结束的索引(不包含)]
print(l[3:], l[4:])         # [起始的索引(包含), 结束位置]
print(l[::2], l[::3])       # [::间隔的个数(步长)]
print(l[:-1])               # [:负数] 倒数第n个的前一个
print(l[::-1])              # [::负数] 逆序开始计算步数
print(l[1:7:3])             # 从下标 1 开始，到下标 7 的前一个，每次遍历+3

# 元组类型: 可以看作不变的列表，操作方式类似列表，使用 , 定义
print((1,), type((1,)))

# 元组的打包和解包(打包)
t = 1, 2, 3, 4, 5
# 元组的打包和解包(解包): 解包的过程中前面的变量数量和元组的元素数量必须保持一致
a, b, c, d, e = t

# 元组打包解包的例子
a = 1
b = 2
# 将 b 和 a 的值，也就是 2 和 1 打包成一个临时的元组，
# 然后进行解包，将 2 和 1 分别赋值给对应位置的 a 和 b
a, b = b, a


# 打包可以让函数返回多个参数，解包可以接收多个参数
def return_more():
    return 1, 2, 3


# 通过解包接收到了多个返回值
value1, value2, value3 = return_more()







