# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------lab1--------------------------------------------------------------------
# word = input("Enter your word : ")
#
# def remove_vowels(word):
#     ans = word
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     for i in word.lower():
#         if i in vowels:
#             ans = ans.replace(i,"")
#     return ans
# ans = remove_vowels(word)

#
# vowels = ('a', 'e', 'i', 'o', 'u')
#
# for i in word.lower():
#     if i in vowels:
#         ans = ans.replace(i, "")
#
# print('word : ', ans)
#-------------------------

# -------------------------------------------------
# num = int(input("Enter your num : "))
# # i=num;
# for i in range(num+1):
#     print(" "*(num-i),"*"*i);
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------lab2--------------------------------------------------------------------
# import math
# def Triangle_area():
#     shape = input("Enter your shape : ")
#     area=0
#     if(shape=="t"):
#         base =int(input("Enter your base : "))
#         height =int(input("Enter your height : "))
#         area=0.5*base*height
#     elif(shape=="r"):
#         width =int(input("Enter your width : "))
#         height =int(input("Enter your height : "))
#         area=width*height
#     elif(shape=="s"):
#         width = int(input("Enter your width : "))
#         area=width*width
#     elif(shape=="c"):
#         radius = int(input("Enter your radius : "))
#         area = math.pi*radius*radius
#     return area
# print("let`s calculate the area of your shapes")
# area=Triangle_area()
# print("your shape area : ", area)
#-------------------------------------------
# st= input("Enter your string : ")
# ans=[]
# for i in range(len(st)):
#     if (st[i]=="i"):
#         ans.append(i)
# print(ans);
#----------------------------------------------
# num= int(input("Enter your num : "))
# l=[]
# ls=[]
# for i in range(1,num+1):
#     l=[]
#     j=i
#     for j in range(1,i*i+1):
#         if(j%i==0):
#             l.append(j)
#     ls.append(l)
# print(ls)
# --------------------------------------------------
ls=input("Enter your elements_num : ")
num= int(input("Enter your elements_num : "))
ls=[]
print("Enter your elements : ")
for i in range(num):
    ls.append(input())
# print(ls)
ans={}
for i in range(len(ls)):
    d={ls[i][0]:ls[i]}
    ans.update(d)
print(ans)
# -----------------------------------------------------------------------------------------------------------------------
