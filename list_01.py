num=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)#列表[,]-有序

'''
可切片对象：列表、字符串、字典、元组
'''

print(num[1])#访问元素-索引从0开始-特殊切片
print(num[-1])#负数为倒序访问-最后一位为(-1)

print(num[1:12])#切片操作[起始:结束:步距]-前闭后开
print(num[:5:-1])#步距默认值为1。负数为倒切
print(num[:])#浅拷贝列表
print(num[::-1])#倒切列表




