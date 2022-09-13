
import codecs
from base64 import encode
import sys

if __name__ == "__main__" :
    if len(sys.argv) <3 : exit()
    extracted_times = []
    file_to_be_replaced = sys.argv[1]
    file_to_be_loaded_to_first_file = sys.argv[2] 
    
    #extract all time stamps of titles from the first file
    with open(str(file_to_be_replaced), "r", encoding='utf-8') as file:
        for line in file:
            #print(line.strip())
            if line.strip().find("-->") > -1:
                # print(line.strip())
                extracted_times.append(line.strip())
    
    #create the new file with append mode
    new_file = open("new_title_file.srt", encoding='utf-8', mode="a")

    #write the desired titles from the second file with original times to @new_file
    counter = 0
    with open(str(file_to_be_loaded_to_first_file), "r", encoding='utf-8') as file:
        for line in file:
            if line.strip().find("-->") > -1:
                if counter >= len(extracted_times):
                    print("Creating of new titles: "+ '\033[93m' +" [ OK ]")
                    print("Creating of file has been stopped, the original file is shorter then the title-source file", file=sys.stderr,)
                    exit()
                new_file.write(extracted_times[counter]+"\n")
                counter = counter + 1
            else:
                new_file.write(line.strip() + "\n")

    new_file.close()
    print("Creating of new titles: "+ '\033[92m' +" [ OK ]")
