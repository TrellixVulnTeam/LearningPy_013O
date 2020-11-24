# import random
# b=set()
# for num in range(10):
#     a=random.randint(0,1000)
# # 将生成的随机数放入一个集合
#     b.add(a)
# print(len(b))
# # 遍历集合元素
# list=[]
# for item in b:
#     print(item,end=' ')
# # 将集合元素添加至list
#     list.append(item)
# #排序
# for i in range(len(list)-1):
#     for j in range(len(list)-i-1):
#         if (list[i]>list[i+1]):
#             list[i+1],list[i]=list[i],list[i+1]
# print(list)

# input_int=int(input("请输入一个整数："))
# while input_int>0:
#     if input_int>10:
#         print("输入的数字过大，请重新输入！")
#         break
#     else:
#         input_int-=1
#         print("输入的数字正常")

# for letter in 'Python':
#     if letter == 'h':
#         continue
#     print('当前字母:'+letter)

for x in range(1,10):
    for y in range(10):
        for z in range(10):
                sum=x**3+y**3+z**3
                if sum==100*x+10*y+z:
                    print(sum)

