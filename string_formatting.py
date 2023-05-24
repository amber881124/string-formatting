fruit = 'apple'
num = 20
price = 10

# 舊型
print('一個 apple %d 元' % price)
print('一個 %s %d 元' % (fruit, price))

# 新型
print('一個 {} {} 元'.format(fruit, price))

# python 3.6+ (最新型)
print(f'一個 {fruit} {price} 元')

# 上面全都輸出 : 一個 apple 10 元

# 向左or右對齊
print((f'一個 {fruit:>10} {price} 元'))
print((f'一個 {fruit:<10} {price} 元'))

# 一個      apple 10 元
# 一個 apple      10 元


