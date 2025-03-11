import array as arr
a=arr.array("i",[1,2,2,3,2,2,2,2,2,2,2,2,2,3,4,4,4,5,5,4,5,7,8,754,3,8,765,4])
print(str(a))
print("number of occurances for the number 2:",str(a.count(2)))

a.reverse()
print(str(a))