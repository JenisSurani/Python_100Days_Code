l1=[1,22,19,"Jenis",-57,18.23]
l2=[1,22,25,2,9,16,255,22]

# # sort method:
# # .sort() modifies the list in place instead of returning a new list.
# # It returns None because its purpose is to change the original list, not to create a new one.
# # print(l2.sort()) # returns None

# l2.sort
# print(l2) # means it changing actual l2 not creating new list

# # if you want to l2 remains unchanged and wants new list
# print(sorted(l2)) # use sorted method (public method) instead of sort that is in list class

# l2.sort(reverse=True)
# print(l2)

# # reverse method:

# l1.reverse() # same for reverse method also
# print(l1)

print(l2.index(22)) # returns 1st index of 22

# count method:
print(l2.count(22)) # returns total no of occureence

#  copy method:
# if you don't want to change your l2 list just copy it in l3 and apply operations
l3=l2.copy()
print(l3)

            # if you do this:
# l3=l2
# l3[0]=11
# it actually changes l2 because l3=l2 means now l3 is pointing to l2 object
#  so avoid doing this instead of just use copy function

# append method:

# print(l3.append(1000)) --> None
l3.append(1000)
print(l3) 

# insert at specific index:

l3.insert(2,23)
print(l3) # modifying the l3 not creating new one


# extend method:

l3.extend(l1) # means open l1 and add l1 to end of l3
print(l3)  #can use concenate if you dont want to change l3
# print(l3+l1) # can do this also


# list j extend kari sakiye tevu nai,tuples,dict,set kai pan l3 ni pachhal extend kari skay
# also if you dont want l3 to be changed copy it to l4

# concatenating two list:
print(l1+l2)


# so all the methods in list don't return new list expect copy it just changes existing list because list are mutuable


# If you need a general-purpose dynamic array, list is fine. If you need a performance-optimized numerical array, use NumPy. For fast insertions/deletions, use deque.

            
# Author: Jenis Surani
# Topic: List_Methods
# Date: 06/02/2025

