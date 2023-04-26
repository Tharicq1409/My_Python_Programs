import csv

# open the two CSV files
with open('C:/Users/3iintr00203/Desktop/integrations list/completed.csv') as file1, open('C:/Users/3iintr00203/Desktop/integrations list/all.csv') as file2:
    # read the contents of each file into a list
    file1_list = [row for row in csv.reader(file1)]
    file2_list = [row for row in csv.reader(file2)]
    
    # find the unique strings in each file
    file1_set = set([item for sublist in file1_list for item in sublist])
    file2_set = set([item for sublist in file2_list for item in sublist])
    
    # print the unique strings in each file
    print("Unique strings in file 1:", file1_set - file2_set)
    print("Unique strings in file 2:", file2_set - file1_set)

'''
import csv

# open the two CSV files
with open('C:/Users/3iintr00203/Desktop/integrations list/completed.csv') as file1, open('C:/Users/3iintr00203/Desktop/integrations list/all.csv') as file2, open('C:/Users/3iintr00203/Desktop/integrations list/output.csv', 'w', newline='') as output_file:
    # read the contents of each file into a list
    file1_list = [row for row in csv.reader(file1)]
    file2_list = [row for row in csv.reader(file2)]
    
    # find the unique strings in each file
    file1_set = set([item for sublist in file1_list for item in sublist])
    file2_set = set([item for sublist in file2_list for item in sublist])
    
    # write the unique strings to the output file
    writer = csv.writer(output_file)
    writer.writerow(['Unique strings in file 1'])
    writer.writerow(list(file1_set - file2_set))
    writer.writerow(['Unique strings in file 2'])
    writer.writerow(list(file2_set - file1_set))
'''

#by user_1409 😊