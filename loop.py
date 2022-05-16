'''
1) Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
2) Using a while loop and input , do the following :
Ask the the user : "what is the product of 7 * 24 ?"
check if the answer is right then exit the loop and print "You answered this Question correctly"
if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again
'''



i = 45
while i < 210:
    i += 1
    if i == 100:
        
        continue
    elif i == 205:
        
        break
    print( i )
         
b= int(input("what is the product of 7 * 24 ?") )
c=168

while c != b:
    print("try again")
    b= int(input("what is the product of 7 * 24 ?") )
    continue
    if c == b:
        
        
        break
print("your ansewr is correct")
    
    


