def sortStrings(array):
    dic = {}
    for i in range(len(array)):
        size = len(array[i])
        if size not in dic.keys():
            dic[size] = []
            dic[size].append(array[i])
        else:
            dic[len(array[i])].append(array[i])
    keys = dic.keys()
    keys_ord = sorted(keys)
    array_ord = []
    for key in keys_ord:
        for string in dic[key]:
            array_ord.append(string)
    return array_ord

n = int(raw_input())
strings = []
for i in range(n):
    string = raw_input()
    strings.append(string)
strings_ord = sortStrings(strings)
boolean = True
for i in xrange(len(strings_ord)-1):
    if strings_ord[i] not in strings_ord[i+1]:
        boolean = False
        break
if boolean:
    print "YES"
    for value in strings_ord:
        print value
else:
    print "NO"
