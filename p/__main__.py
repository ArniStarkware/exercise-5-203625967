import p as p
import sys

if __name__ == '__main__':
    if len (sys.argv) <= 1:
        print('usage')
    elif len(sys.argv) > 2:
        print('usage')
    else:
        classToMake = sys.argv[1]
        if classToMake == 'a':
            instance = p.A()
        elif classToMake == 'b':
            instance = p.B()
        elif classToMake == 'c':
            instance = p.C()
        elif classToMake == 'd':
            instance = p.D()
        else:
            print('usage')
        print (f'created {instance}')

