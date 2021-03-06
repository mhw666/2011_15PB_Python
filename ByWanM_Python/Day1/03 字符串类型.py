# 字符串的表现形式: '' \ "" \ ''' \ """
print('单引号', '\'\'', '""')
print('双引号', "''", "\"\"")

# 三个引号和两个引号的区别：保留格式
# python 中的三引号通常用于文档注释
print('第一行\
      第二行')
print('''第一行
      第二行''')

# python 没有字符类型，可以把字符看作一个元素的 str
print('str', "str")