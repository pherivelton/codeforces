dic = {"purple": "Power", "green": "Time", "blue": "Space", "orange": "Soul",
       "red": "Reality", "yellow": "Mind"}
colors = ["red", "purple", "green", "blue", "orange", "yellow"]
n = int(raw_input())
output = str(6-n)+"\n"
for i in xrange(n):
    color = raw_input()
    colors.remove(color)
for color in colors:
    output += dic[color] + "\n"
print output
