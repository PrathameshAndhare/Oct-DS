# format()

str1="today is {}, tomorrow is {} .".format("saturday","sunday")
print(str1)

str1="today is {1}, ans today's date is {0} .".format("saturday",7)
print(str1)

# indexing --->
#. 0123456789.     16
q="Today is Saturday"
print(q)

print(q[4],q[8],q[13])
print(q[2])
w=q[2]

e=w
print(w,e)
print(id(w),id(e))
e="z"
print(id(w),id(e))
print(w)
# print(q[19])


#.       0123456
value = "rainbow"
#.       -7   -1

print(value)
print(value[3])

print(value[0],value[-7])
print(value[6],value[-1])

print(value[1],value[-3])
# print(value[10])
# print(value[-8])


# multiple values --> string[start:end]. start<=end , end index is not included 
#.       0123456
value = "rainbow"
#
print(value[0:5])
print(value[0:7])
print(value[3:6])
print(value[6:7])
print(value[3:])
print(value[:6])
print(value[:])
#.                -7.   -1
#.       value = "rainbow"
# -1 w
# -2 o
# -3 b
# -4 n
# -5 i
# -6 a
# -7 r
print(value[-7:-1])
print(value[-3:-1])
print(value[-7:])
print(value[:-2])
print(value[:])

print(value[-1:-4]) # start < end












