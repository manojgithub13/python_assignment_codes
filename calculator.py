def add (x,y):
    return x+y

def sub (x,y):
    return x-y

def mul (x,y):
    return x*y

def div (x,y):
    if y==0:
       return'cant be divided'
    return(x/y)

while True:
    print('options:add, sub, mul, div')
    print('enter exit to quit')

    user_input = input(':').lower()

    if user_input == 'exit':
         break
        
    if user_input in ('add','sub','mul','div'):
         num1=float(input('enter the first number:'))
         num2=float(input('enter the second number:'))
         if user_input=='add':
             print(f'{add(num1,num2)}')
         elif user_input=='sub':
             print(f'{sub(num1,num2)}')
         elif user_input=='mul':
             print (f'{mul(num1,num2)}')
         elif user_input == 'div':
             result = div(num1, num2)
             if result == "Can't divide by zero":
                 print(result)
             else:
                 print(f'Result: {result}')

    else:
       print('invalid number')
              
    
