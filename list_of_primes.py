def crazy_list (list):
    list_back=list[-1::-1]
    for i in range (0, len(list)):
        if list[i]==list_back[i]:
          return True
        else:
            return False
crazy_list([5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] )
