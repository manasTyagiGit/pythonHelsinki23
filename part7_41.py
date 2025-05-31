import json

def print_persons (filename: str) :
    with open (filename) as file_head :
        data = file_head.read()

    data_list = json.loads(data)

    for dict in data_list :
        print (f"{dict["name"]} {dict["age"]} years (", end = "")        
        
        hobb = ", ".join(dict["hobbies"])
        print (hobb, end = "")

        print (")")   
        

if __name__ == "__main__" :
    print_persons("part7_41.json")