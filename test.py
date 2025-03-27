def range_num():
    for x in range(3, -1, -1):
        print(x)

def task_2():
    gues_me = 5
    for number in range(10):
        if number < gues_me:
            print("to low")
        if number == gues_me:
            print("found it!")
            break

        
