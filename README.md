**Link Codeforces's Profile:** http://codeforces.com/pherivelton

- [988 A](#988A)
- [988 B](#988B)
- [987 B](#987B)

## 988A

There are n students in a school class, the rating of the i-th student on Codehorses is ai. You have to form a team consisting of k students (1≤k≤n) such that the ratings of all team members are distinct.

If it is impossible to form a suitable team, print "NO" (without quotes). Otherwise print "YES", and then print k distinct numbers which should be the indices of students in the team you form. If there are multiple answers, print any of them.

**Input**
The first line contains two integers n and k (1≤k≤n≤100) — the number of students and the size of the team you have to form.

The second line contains n integers a1,a2,…,an (1≤ai≤100), where ai is the rating of i-th student.

**Output**
If it is impossible to form a suitable team, print "NO" (without quotes). Otherwise print "YES", and then print k distinct integers from 1 to n which should be the indices of students in the team you form. All the ratings of the students in the team should be distinct. You may print the indices in any order. If there are multiple answers, print any of them.

Assume that the students are numbered from 1 to n.

Examples
```
input
5 3
15 13 15 15 12
output
YES
1 2 5 

input
5 4
15 13 15 15 12
output
NO

input
4 4
20 10 40 30
output
YES
1 2 3 4 

```
### Note
All possible answers for the first example:

{1 2 5}
{2 3 5}
{2 4 5}
Note that the order does not matter.

## 988B
You are given n strings. Each string consists of lowercase English letters. Rearrange (reorder) the given strings in such a way that for every string, all strings that are placed before it are its substrings.

String a is a substring of string b if it is possible to choose several consecutive letters in b in such a way that they form a. For example, string "for" is contained as a substring in strings "codeforces", "for" and "therefore", but is not contained as a substring in strings "four", "fofo" and "rof".

Input
The first line contains an integer n (1≤n≤100) — the number of strings.

The next n lines contain the given strings. The number of letters in each string is from 1 to 100, inclusive. Each string consists of lowercase English letters.

Some strings might be equal.

Output
If it is impossible to reorder n given strings in required order, print "NO" (without quotes).

Otherwise print "YES" (without quotes) and n given strings in required order.

Examples
```
input
5
a
aba
abacaba
ba
aba
output
YES
a
ba
aba
aba
abacaba

input
5
a
abacaba
ba
aba
abab
output
NO

input
3
qwerty
qwerty
qwerty
output
YES
qwerty
qwerty
qwerty
```

### Note
In the second example you cannot reorder the strings because the string "abab" is not a substring of the string "abacaba".

## 987B

Year 2118. Androids are in mass production for decades now, and they do all the work for humans. But androids have to go to school to be able to solve creative tasks. Just like humans before.

It turns out that high school struggles are not gone. If someone is not like others, he is bullied. Vasya-8800 is an economy-class android which is produced by a little-known company. His design is not perfect, his characteristics also could be better. So he is bullied by other androids.

One of the popular pranks on Vasya is to force him to compare xy with yx. Other androids can do it in milliseconds while Vasya's memory is too small to store such big numbers.

Please help Vasya! Write a fast program to compare xy with yx for Vasya, maybe then other androids will respect him.

Input
On the only line of input there are two integers x and y (1≤x,y≤109).

Output
If xy<yx, then print '<' (without quotes). If xy>yx, then print '>' (without quotes). If xy=yx, then print '=' (without quotes).

Examples
```
input
5 8
output
>

input
10 3
output
<

input
6 6
output
=
```

### Note
In the first example **5^8 = 5.5.5.5.5.5.5.5 = 390625**, and **8^5= 8.8.8.8.8 = 32768.** So you should print '>'.

In the second example **10^3=1000 < 3^10=59049.**

In the third example **6^6 = 46656 = 6^6.**
