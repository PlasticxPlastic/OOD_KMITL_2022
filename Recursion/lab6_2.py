def Max(list):
    if len(list) == 1:
        return list[0]
    m = Max(list[1:])
    if m > list[0]:
        return m
    else:
        return list[0]


def sort(list, slist=[]):
    if len(list) == 0:
        return slist
    slist.append(int(Max(list)))
    list.remove(int(Max(list)))
    return sort(list, slist)


ip = input("Enter your List : ").split(',')
for i in range(len(ip)):
    ip[i] = int(ip[i])
slist = sort(ip)
print("List after Sorted : ",end="")
print(slist)