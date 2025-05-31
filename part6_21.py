def filter_solutions() :
    
    correct_file_name = "correct.csv"
    incorrect_file_name = "incorrect.csv"

    open(correct_file_name, "w").close()            # wiping
    open(incorrect_file_name, "w").close()          # wiping

    correct   = open(correct_file_name, "w")
    incorrect = open(incorrect_file_name, "w")

    with open ("solutions.csv") as solutions :

        for line in solutions :            
            parts = line.split(";")           
            
            if eval(parts[1]) == int(parts[2]) :
                correct.write (line)
            else :
                incorrect.write (line)



if __name__ == "__main__" :
    filter_solutions()

    filter_solutions()
    filter_solutions()