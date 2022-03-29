import os;
import yaml;

# # # List的基本属性:可变有序可重复列表
# # st=['py','java','js']
# # l=len(st)
# # for i in range(l):
# #     print(st[i],end='\t')


# # # 在list的末尾添加一个元素
# # st.append(123)
# # print(st)
# # # 删除list末尾的一个元素
# # st.pop()
# # print(st)
# # # 在指定位置插入一个元素
# # st.insert(1, 'object')
# # print(st)
# # st.insert(2, 'object')
# # print(st)
# # # list切片: object[start_index:end_index:step]step 为正，从左到右切片；step为负，从右到左切片
# # print(st[0:])
# # # 删除某一个元素
# # print(st)
# # st.remove('object')
# # print(st)
# # # 清除list的全部元素
# # st.clear()
# # print(st)
# '''
# 元组：一旦创建不可改变的列表，引用不可改变，内容可改变
# 形式为s=(1,2,3)
# '''
# x = {3, 4, 5}
# s = {4, 5, 6, 6}
# print(s ^ x)
# print(x)


# '''
# 字典
# dict={'name':'tom','age':18}
# '''


# dict={'name':'tom','age':18}
# print(dict['age'])
# print(dict.get('name'))
# print(dict)
# '''
# 集合：
# 无序不可重复的数据集合，可进行数学集合操作，如：交集&、并集|、差集^
# 可使用函数set()初始化
# x={3,4,5}
# s={4,5,6,6}
# print(s^x)
# print(x)
# '''

# '''
# 函数
# 定义：
# def 函数名 (参数列表):
#         函数体

# 参数类型：必须参数、关键字参数、默认参数、不定长参数
# '''
# def max (a,b):
#     if a>b:
#         return a
#     else:
#         return b

# a,b=5,6
# print(max(a, b))


path = os.getcwd()
file=open(path+"/src/data/page_data.yaml", 'r', encoding="utf-8")
data = yaml.load(file,Loader=yaml.FullLoader)
print(data)
print(os.getcwd()+"/src/data/page_data.yaml")