def function1 (first_value:int ,second_value:int):
    
     for number in range(first_value, second_value+1):
       if number > 1:
            for i in range(2,number):
               if(number % i == 0):
                 break
            else:
                print(number)

function1(5,66)