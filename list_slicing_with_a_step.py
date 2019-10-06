my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[6:0:-2])
print(my_list[-1:-6:-2])

def _list_manipulation_sample1_(input_list, input_string):
    for i in range(1, 4):
        input_list[i] = input_string
    return input_list
