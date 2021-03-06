# 使用 print 进行内容的输出，可以输出不定长度不定类型的值
print(1, '1', 1.1, [1, ], (1, ))

# 在使用 print 进行输出的时候，通过参数可以指定一些格式
print(1, 2, 3, 4, 5, 6, sep='*', end='这里是结尾')

# 格式化输出，使用 % 进行格式化输出，字符串语法支持
print('%5.2f + %d = %d' % (1, 2, 1+2))

# 格式化输出，使用字符串的内置方法 format，字符串内置方法
print('{0:.3f}, {1:10d}, {0:.3f}'.format(1, 2))

# 格式化输出，使用 f'' 字符串进行输出，语法支持
print(f'{1:.2f} + {2} = {1+2}')
