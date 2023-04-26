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
print("Welcome...You're about to work for a Miral Project")
print("Quick Tip :- \n🔴 Miral Asset Management LLC name has been changed to MIRAL LLC \n🔴 FARAH Experiences LLC name has been changed to MIRAL Experiences LLC \n🔴 Experiences Hub LLC name has been changed to MIRAL Destinations LLC")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("You Can Assign upto 3 Directories at a same time")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("Now Enter Directory 1 👇")
# Directory and search phrase user Input 
dir_path = input("Enter a Directory (1):")
search_phrase = input("Enter a Search_Word (1): ")

#Function call 
findtext(dir_path, search_phrase)

print("----------------------")
print("Now Enter Directory 2 👇")
dir_path_1= input("Enter a Directory (2):")
search_phrase_1= input("Enter a Search_Word (2): ")
#Function call
findtext(dir_path_1, search_phrase_1)

print("----------------------")
print("Now Enter Directory 3 👇")
dir_path_2= input("Enter a Directory (3):")
search_phrase_2= input("Enter a Search_Word (3): ")
#Function call
findtext(dir_path_2, search_phrase_2)

#by user_1409 😊