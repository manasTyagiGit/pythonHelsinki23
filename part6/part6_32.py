def filter_incorrect () :
    correct = open ("correct_numbers.csv", 'w')

    with open ("lottery_number.csv", 'r') as lottery :
        for line in lottery :
            parts = line.split (',')

            if len (parts) != 8 :
                break

            part1 = parts[0].split (' ')

            if not part1[1].isdigit() :
                break

            for num in parts[1:] :
                if not num.isdigit() :
                    break

                elif int(num) < 1 or int(num) > 39 :
                    break

            correct.write (line)
         

if __name__ == "__main__" :
    filter_incorrect ()
    
