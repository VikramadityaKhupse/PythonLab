import time

def check_performance(approaches):
    time_taken = []
    test = {1: 2, 2: 2, 4: 5, 7: 6, 8: 7}

    for approach in approaches:
        start_time = time.time()
        for _ in range(100000):  
            approach(test)
        end_time = time.time()
        time_taken.append(end_time - start_time)

    return list(zip([approach.__name__ for approach in approaches], time_taken))


def approach1(test: dict):
    output = test.get(1) 


def approach2(test: dict):
    output = list(test.values())[1]  


print(check_performance([approach1, approach2]))
