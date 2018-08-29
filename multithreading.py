import threading
import time

start = time.time()

def squares(numbers):
    print("calculating square of numbers... ")
    for n in numbers:
        time.sleep(.5)
        print("square: ", n**2)

def cubes(numbers):
    print("calculating cubes of numbers... ")
    for n in numbers:
        time.sleep(.5)
        print("cube: ", n**3)

num_list = [3,5,7,9]

# squares(num_list)
# cubes(num_list)

t1 = threading.Thread(target=squares, args= (num_list,))
t2 = threading.Thread(target=cubes, args= (num_list,))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()


print ("finished in...", end-start)

print ("program is done running!!!")


