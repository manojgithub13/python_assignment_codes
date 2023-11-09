count=0
Easy=0
print('welcome to quiz')
nxt=input('To start press enter')

print('----------------------------------------------')
print('what is the capital of india?(level:Easy)')
print('a.delhi')
print('b.bangalore')
print('c.agra')
print('d.chennai')
answer=input('answer:').lower()
if answer == 'a':
    count=count+10
    Easy+=1
else:
    print('wrong answer')
    
print('----------------------------------------------')

print('what is the capital of karnataka?(level:Easy)')
print('a.delhi')
print('b.bangalore')
print('c.agra')
print('d.chennai')
answer=input('answer:').lower()
if answer == 'b':
    count=count+10
    Easy+=1
else:
    print('wrong answer')
    
print('----------------------------------------------')
print('Where is rapid tech. located?(level:Easy)')
print('a.delhi')
print('b.bangalore')
print('c.agra')
print('d.chennai')
answer=input('answer:').lower()
if answer == 'b':
    count=count+10
    Easy+=1
else:
    print('wrong answer')
    
print('----------------------------------------------')
print('which of the city below has seaport?(level:Easy)')
print('a.delhi')
print('b.bangalore')
print('c.agra')
print('d.chennai')
answer=input('answer:').lower()
if answer == 'd':
    count=count+10
    Easy+=1
else:
    print('wrong answer')


Medium=0    
print('----------------------------------------------')
print('who is the 1st president of india?(level:Medium)')
print('a.Dr. Zakir Husain')
print('b. V. V. Giri')
print('c.Dr. Rajendra Prasad')
print('d.Dr. Sarvepalli Radhakrishnan')
answer=input('answer:').lower()
if answer == 'c':
    count=count+20
    Medium+=1
else:
    print('wrong answer')
    
print('----------------------------------------------')
print('who is 1st Muslim president of india?(level:Medium)')
print('a.Dr. Zakir Husain')
print('b. V. V. Giri')
print('c.Dr. Rajendra Prasad')
print('d.Dr. Sarvepalli Radhakrishnan')
answer=input('answer:').lower()
if answer == 'a':
    count=count+20
    Medium+=1
else:
    print('wrong answer')
    
print('----------------------------------------------')
print('who is 1st independent candidate to be elected as president?(level:Medium)')
print('a.Dr. Zakir Husain')
print('b. V. V. Giri')
print('c.Dr. Rajendra Prasad')
print('d.Dr. Sarvepalli Radhakrishnan')
answer=input('answer:').lower()
if answer == 'b':
    count=count+20
    Medium+=1
else:
    print('wrong answer')
    
print('----------------------------------------------')
print("whose birthday is celebrated as teacher's day?(level:Medium)")
print('a.Dr. Zakir Husain')
print('b. V. V. Giri')
print('c.Dr. Rajendra Prasad')
print('d.Dr. Sarvepalli Radhakrishnan')
answer=input('answer:').lower()
if answer == 'd':
    count=count+20
    Medium+=1
else:
    print('wrong answer')


Hard=0    
print('----------------------------------------------')
print("Who is the first Indian woman to win an Asian Games gold in 400m run?(level:Hard)")
print('a.M.L. Valsamma')
print('b.P.T. Usha ')
print('c.Kamaljit Sandhu')
print('d.K.Malleshwari')
answer=input('answer:').lower()
if answer == 'b':
    count=count+30
    Hard+=1
else:
    print('wrong answer')    

print('----------------------------------------------')
print("The National Game of Japan is?(level:Hard)")
print('a.Tennis')
print('b.Karate')
print('c.Ice Hockey')
print('d.Sumo wrestling')
answer=input('answer:').lower()
if answer == 'd':
    count=count+30
    Hard+=1
else:
    print('wrong answer')
    
print('----------------------------------------------')
print("Which of the following is the first South Asian country to call match-fixing a crime?(level:Hard)")
print('a.Nepal')
print('b.Sri Lanka')
print('c.India')
print('d.Pakistan')
answer=input('answer:').lower()
if answer == 'b':
    count=count+30
    Hard+=1
else:
    print('wrong answer')    

print('----------------------------------------------')
print("Which country hosted the 13th South Asian Games?(level:Hard)")
print('a.Nepal')
print('b.Sri Lanka')
print('c.India')
print('d.Pakistan')
answer=input('answer:').lower()
if answer == 'a':
    count=count+30
    Hard+=1
else:
    print('wrong answer')    
    
print('----------------------------------------------')
print(f'total source:')
print(f'%s'%(count))
print(f'level Easy crct answers:{Easy}')
print(f'level Medium crct answers:{Medium}')
print(f'level Hard crct answers:{Hard}')

if count >= 160:
    print('good')
elif count == 240:
    print('wow!answered all questions')
else:
    print('need to improve')
      
