def do_twice(f, spam):
    f(spam)
    f(spam)

def print_spam(spam):
    print(spam)

do_twice(print_spam, 'spam')

def do_four(f, spam):
    i = 0
    while i < 4:
        f(spam)
        i+=1

do_four(print_spam, 'spam')