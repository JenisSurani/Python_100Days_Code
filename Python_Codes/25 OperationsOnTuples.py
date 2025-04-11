# We know that Tuples are immutable.

# But we can perform opretations by following approch:
# 1) Typecast (Convert) it to list then apply list method then Typecast(Convert) it back to Tuple
# 2) Using Concatrnate method of tuple

#1)

countries=("Spain","USA","India","China","Japan","Sri-lanka")
print(countries)
temp1=list(countries)

#  now we can apply list method on temp1 list
temp1.append("Ireland")
temp1.pop(5)
temp1[1]="SouthAfrica"

#  now convert it back to the tuple

countries=tuple(temp1)

# now your tuple has changed
print(countries)


#2)

t=(1,2,3)
print(t)
t1=t[:1]+(5,)+t[2:] # we are not doing anything new here , just slicing the tuple(that returns new tuple) and then using Concatrnate that also return new tuple means our old tuple in memory is still there
# we are forming new one and give it the ref of t
print(t1)
print(t)


#  As tuples are immutable it have limited built in methods

ttt=(11,22,33,44,11,44,66,33,22,99)
print(ttt.count(11))
print(ttt.index(22)) # can raise ValueError if element is not found in tuple
print(ttt.index(22,2,9)) # index(element,start,end)

# Author: Jenis Surani
# Topic: Tuples Operations
# Date: 06/02/2025