# def
def detect_q2(step_list):
    for k,s in enumerate(step_list):

        if k % 2 == 0:
            if s == 'L':
                return False
        else:
            if s == 'R':
                return False

    return True

# input
step = str(input())
step_list = list(step)

# main
if detect_q2(step_list):
    print('Yes')
else:
    print('No')
