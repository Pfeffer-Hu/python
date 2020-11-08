# 虽然说python里面一切是对象，但是还能很难理解一个函数是如何能用isinstance 这么个东西

def enumerate(value):
    list1 = []
    index = 0
     for i in value:
         t1 = (index,i)
         list1.append(t1)

         index += 1

         print(list1)