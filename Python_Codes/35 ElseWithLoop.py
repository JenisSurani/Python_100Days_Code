# https://chatgpt.com/share/67a85620-bed0-800f-87ca-404844d6f32a

#  for more info about string .format() method use this convo

# The else block in a for loop executes only if the loop completes all iterations naturally without hitting a break statement.

for i in range(10):
    print(i)
    if i==9:
        i=i+1 
        break
else:
    print("Else block is executed!!")
    
#  The else block in a for loop executes only if the loop completes all iterations naturally without hitting a break   statement.
# Since break is executed when i == 9, the loop does not complete naturally, and the else block is skipped.
# ✅ The else block of a for loop executes only if the loop is not terminated by break.
# ✅ i = i + 1 inside the loop does not affect the loop control variable in for i in range(10).
# because i = i + 1 modifies the local variable i,not loop ka i, but this has no effect on the loop control variable.
# remember intenal working of range loop 
# ✅ To execute the else block, either remove break or ensure it never executes.


# j = 5
# while j > 10:  # This condition is False from the start
    # print("Inside loop")
# else:
    # print("Else executed")
# ✅ Your understanding:
# 
# The loop does not run even once because j > 10 is False initially.
# Since no break occurs and the loop completes all (zero) iterations naturally, the else block executes.

#  break ka simple matlab hai loop ko break karo and execute next code after the loop.

# also explore the .format() method of string in this convo


# Author: Jenis Surani
# Topic: Else block with loop
# Date: 09/02/2025