if __name__ == '__main__':
    try:
        f = open('text.txt', 'r')
        read = f.read()
        replace = read.replace("a", "o")
        f1 = open('firstA.txt', 'w')
        f1.write(replace)
        f1.close()
        read_replace = read.replace("o", "a")
        f2 = open('firstB.txt', 'w')
        f2.write(read_replace)
        f2.close()
        f = open('text.txt', 'r')
        second = open('second.txt', 'w')
        third = open('third.txt', 'w')
        counter = 0
        for line in f:
            counter += 1
            if counter % 2 == 0:
                second.write(line)
            else:
                third.write(line)
        second.close()
        third.close()
        f.close()
    except FileExistsError as e:
        print(e)
    print("Program finished")
