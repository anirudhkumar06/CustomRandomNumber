import time
class GenerateRandomNumber:
    # set range in constructor #
    def __init__(self, start=0, stop=0):
        self.start = start
        self.stop = stop
        self.seed = start
    # gernerate random number function definition #
    def nextNumber(self):
        start = self.start
        stop = self.stop
        while True:
            time.sleep(0.001)
            self.seed = int(time.time() * self.seed % stop)
            if (self.seed < start):
                self.seed += start
            if (self.seed >= stop):
                continue
            break
        return self.seed


if __name__ == '__main__':
    # get current time in ms #
    current_time = time.time()
    min_list = list()
    max_list = list()
    # set range of random number #
    randomNumber = GenerateRandomNumber(start=1, stop=10)
    while (True):
        # called for random number #
        number = randomNumber.nextNumber()
        if (number > 5):
            if (len(max_list) != 73):
                max_list.append(number)
        else:
            if (len(min_list) != 27):
                min_list.append(number)
        # check for biased value #
        if (len(max_list) == 73 and len(min_list) == 27):
            break
    print(len(max_list), ":", max_list)
    print(len(min_list), ":", min_list)
    print("Total time:", time.time() - current_time, "ms")
