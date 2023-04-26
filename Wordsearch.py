import os

def findtext(dir, phrase):    
    for file in os.listdir(dir):
        path = os.path.join(dir.replace('/', '\\'), file) #path grabbing and converting the path into windows readable format
        file_name = os.path.basename(file) # Getting Filename
        if os.path.isdir(path):
            findtext(path, phrase)
        else:
            try:
                with open(path, 'r') as f:
                    file_contents = f.read().lower()
                    if phrase.lower() in file_contents:                                                                                                                                      
                        #print(path)
                        print(f"'{phrase}' found in '{file_name}' ||-->\t File Path :'{path}'\n")                       
            except Exception as e:
                print(f"Error reading file '{path}': {e}")
    
# Directory and search phrase user Input 
dir_path = input("Enter Directory:")
search_phrase = input("Enter search phrase: ")

#Function call
findtext(dir_path, search_phrase)




#by user_1409 😊