# os creates paths to access files across your operating system
# csv reads/writes CSV files
import os, csv


### 1

# takes directory location, folder name, file name
csvpath = os.path.join('..', 'Demo', 'data.csv')

# takes file path, 'r' for read, and ROW delimiter, saves file as variable
with open(csvpath, 'r', newline='') as csvfile:

    # takes file and COLUMN delimiter, returns content
    csvreader = csv.reader(csvfile, delimiter=',')

    # reads each row as list of strings
    for row in csvreader:
        print(row)

### 2
        
# takes file path, 'w' for OVERwrite, 'a' for write, and ROW delimiter, saves file as variable
with open(csvpath, 'a', newline='') as csvfile:

    # takes file and COLUMN delimiter
    csvwriter = csv.writer(csvfile, delimiter=',')

    # writes row
    csvwriter.writerow(['(500) Days of Sama', 'Comedy', '2019'])


### 3

movie_title = ['Tangled', 'Midnight in Paris']
movie_genre = ['Animation', 'Romance']
movie_year = ['2010', '2011']

# zips 4 lists into tuples
zipdata = zip(movie_title, movie_genre, movie_year)

# setups file path
csvpath = os.path.join('data_new.csv')

# writes data
with open(csvpath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Genre', 'Year'])
    writer.writerows(zipdata)

