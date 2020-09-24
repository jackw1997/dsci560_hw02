# This is a python script that transfer output of the first script by 'y=3x+6'

with open('hw02_1a.txt', 'r') as f1:
    with open('hw02_1b.txt', 'w') as f2:
        for i in range(1000):
            line_num = float(f1.readline())
            f2.write('{}\n'.format(line_num * 3 + 6))