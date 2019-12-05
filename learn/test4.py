# i = 0
# while i < 9:
#     i += 1
#     print(i)

# def cfkj():
#     i = 0
#     while i < 9:
#         i+=1
#         j=0
#         while j < i:
#             j+=1
#             print(str(j)+"*"+str(i)+"="+str(i*j), end="\t")
#
#         print("")
# cfkj()

# class Math:
#     def cfkj(self):
#         i = 0
#         while i < 9:
#             i += 1
#             j = 0
#             while j < i:
#                 j += 1
#                 print(str(j) + "*" + str(i) + "=" +str(i * j), end="\t")
#             print("")
#
# math = Math()
# math.cfkj()

#
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i >= j:
#             print("%s*%s=%s"%(j, i, i*j), end="\t")
#     print()


# a = [-4,-5,-9,0,1,2,3]
# z = []
# f = []
# for b in a:
#     if b > 0:
#         z.append(b)
#     elif b < 0:
#         f.append(b)
#     else:
#         print(str(b) + "不是正数或负数")
#
# print(len(z))
# print(len(z))


# number = list(range(-11, 5, 2))
# print(number)
#
# a = []
# b = []
# for i in number:
#     if i > 0:
#         a.append(i)
#     elif i < 0:
#         b.append(i)
#     else:
#         print("不为正数或负数")
#
# print(len(a))
# print(len(b))


guest = ['Alice', 'Bob', 'Candy']
print(guest)
print(guest[0] + "无法参加聚会。")
guest[0] = 'Dave'
print(guest)

for a in guest:
    print("邀请"+ a +"参加聚会。")

print("我找到一个更大的餐桌。")
guest.insert(0, 'Joe')
guest.insert(2, 'Eric')
guest.append('Flank')
print(guest)
for b in guest:
    print("邀请"+ b +"参加聚会。")

for n in range(0, 4):
    number = 0
    leave = guest.pop(number)
    print(leave + "无法参加聚会。")

