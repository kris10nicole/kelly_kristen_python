N=[0,1,2,3,4,5]

def brackets(number):
    if number==1:
        print('[] OK')
        print('[[ Not OK')
        print('][ OK')
        print(']] Not OK')
    elif number==2:
        print('[[]] OK')
        print('[]]] Not OK')
        print('][]] Not OK')
        print('[[[] Not OK')
        print('[[[[ Not OK')
        print('[][] OK')
        print(']]]] Not OK')
        print('][][ Not OK')
        print('][[] Not OK')
    else:
        print('[[[]]] OK')
        print('[[]]]] Not OK')
        print('[[[[]] Not OK')
        print('[][[[[ Not OK')
        print(']][[[[ Not OK')
        print(']]][[[ OK')
        print('[][][] OK')
        print('][[[[[ Not OK')
        print('][[[[] Not OK')
        print('][][][ OK')


print(brackets(int(input('Enter a number between 1 and 3: '))))
