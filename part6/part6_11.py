def largest() -> int :
    max = -1
    with open ("numbers.txt") as file :
        for line in file :
            line = line.replace ("\n", "")
            if int(line) > max :
                max = int(line)

    return max


if __name__ == "__main__" :
    print (largest())