line=str

def reverse(line):
    return line[::-1]

def is_palindrome(line):
    return line==reverse(line)

f=open(input('Enter file name: '),'r')
for line in f:
    if is_palindrome(line):
        print(line, end='')
    else:
        print('Done')

