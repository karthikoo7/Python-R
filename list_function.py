# l1 = [1,2,3,4,5]

def display_list(l):
    print(l)
    #for i in l:
    #    print(i)


def reverse_list(l):
    print('reverse',l[::-1])

def isOdd(i):
    if i%2 != 0:
        return True
    else:
        return False


def alternate_list(l):
    l2 = []
    for i in range(len(l)):
        if isOdd(i):
            l2.append(l[i])
    print('alternate',l2)

def displayUpper(l):
    l2 = []
    for i in l:
       l2.append(str(i).upper())
    print('upper',l2)

def displayLower(l):
    l2 = []
    for i in l:
        l2.append(str(i).lower())
    print('lower',l2)


def unique(l):
    l2 =[]
    for i in l:
        if i not in l2:
            l2.append(i)

    print('unique',l2)

def displayDuplicate(l):
    l3 = []
    for i in l:
        if l.count(i)>1:
           l3.append(i)

    print('duplicate',l3)


