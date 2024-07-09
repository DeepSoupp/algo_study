T = int(input())

for _ in range(T):
    floor = int(input())
    rooms = int(input())


    numbers = [x for x in range(1, rooms+1)]

    for _ in range(floor):
        for i in range(1,rooms):
            numbers[i] += numbers[i-1]

    print(numbers[-1])