global lvl

def Q1():
    print('----------------------------------------------')
    print('What is the capital of India? (level: Easy)')
    print('a. Delhi')
    print('b. Bangalore')
    print('c. Agra')
    print('d. Chennai')
    answer = input('answer:').lower()
    if answer == 'a':
        print('Correct answer')
        lvl = 'easy'
        score_cal(lvl)
    else:
        print('Wrong answer')

        
def Q2():
    print('----------------------------------------------')
    print('Who is the 1st Muslim president of India? (level: Medium)')
    print('a. Dr. Zakir Husain')
    print('b. V. V. Giri')
    print('c. Dr. Rajendra Prasad')
    print('d. Dr. Sarvepalli Radhakrishnan')
    answer = input('answer:').lower()
    if answer == 'a':
        print('Correct answer')
        lvl = 'medium'
        score_cal(lvl)
    else:
        print('Wrong answer')

def Q3():
    print('----------------------------------------------')
    print("Who is the first Indian woman to win an Asian Games gold in 400m run? (level: Hard)")
    print('a. M.L. Valsamma')
    print('b. P.T. Usha')
    print('c. Kamaljit Sandhu')
    print('d. K. Malleshwari')
    answer = input('answer:').lower()
    if answer == 'b':
        print('Correct answer')
        lvl = 'hard'
        score_cal(lvl)
    else:
        print('Wrong answer')

def score_cal(level):
    score = 0
    if level == 'easy':
        score += 10
        print(score)
    elif level == 'medium':
        score += 20
        print(score)
    elif level == 'hard':
        score += 30
        print(score)
    return score

Q1()
Q2()
final_score = Q3()

print('Total score:', final_score)

