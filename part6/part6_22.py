def find_words (search : str) -> list :

    ret_list = []
    with open ("words.txt") as words :
        for line in words :
            word = line.strip()

            if search.startswith("*") :
                if word.endswith(search[1:]) :
                    ret_list.append(word)

            elif search.endswith ("*") :                
                if word.startswith (search[:-1]) :          #upper_bounds are not inclusive in python
                    ret_list.append(word)

            else :

                if len(word) == len(search) :                    
                    match = True

                    size = len(search)

                    for i in range(0, size) :
                        if(search[i] != '.') :
                            if (search[i] != word[i]) :
                                match = False
                                break
                    
                    if match :
                        ret_list.append(word)
    
    return ret_list

if __name__ == "__main__" :

    print(find_words("ca*"))


