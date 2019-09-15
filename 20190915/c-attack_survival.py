# def
class attack_survival():
    def __init__(self, num_of_member, num_of_question, points):
        self.num_of_member = num_of_member
        self.num_of_question = num_of_question
        self.points = points

    def count_correct(self, correct_list):

        rv = [0] * (self.num_of_member + 1)
        for i in correct_list:
            rv[i] += 1

        self.count_list = rv

    def check_result(self):
        for i in range(1, self.num_of_member+1):
            if (self.points + self.count_list[i] - self.num_of_question) > 0:
                print('Yes')
            else:
                print('No')

        return True
# input
N,K,Q = list(map(int, input().split()))
input_list = []
for i in range(1, Q):
    input_list.append(int(input()))

# test input
#N,K,Q = list(map(int, [6, 3, 4]))
#input_list = [3,1,3,2]

# main

game = attack_survival(N,Q,K)
game.count_correct(input_list)
game.check_result()
