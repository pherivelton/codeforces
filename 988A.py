n, k = map(int, raw_input().split())
numbers = map(int, raw_input().split())
indexes = []
verified = []
aux = 0
boolean = False
for i in xrange(len(numbers)):
    if numbers[i] not in verified:
        verified.append(numbers[i])
        indexes.append(i+1)
        aux += 1
    if aux == k:
        boolean = True
        break
if boolean:
    print "YES"
    print ''.join(str(e) + " " for e in indexes)
else:
    print "NO"
