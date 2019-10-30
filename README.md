
### Python ###
------

```python
# os creates paths to access files across your operating system
# csv reads/writes CSV files
import os, csv
```

### Python 1 ###
```python
# takes directory location, folder name, file name
csvpath = os.path.join('..', 'Demo', 'data.csv')

# takes file path, 'r' for read, and ROW delimiter, saves file as variable
with open(csvpath, 'r', newline='') as csvfile:

    # takes file and COLUMN delimiter, returns content
    csvreader = csv.reader(csvfile, delimiter=',')

    # reads each row as list of strings
    for row in csvreader:
        print(row)
```

### Python 2 ###
```python        
# takes file path, 'w' for OVERwrite, 'a' for write, and ROW delimiter, saves file as variable
with open(csvpath, 'a', newline='') as csvfile:

    # takes file and COLUMN delimiter
    csvwriter = csv.writer(csvfile, delimiter=',')

    # writes row
    csvwriter.writerow(['(500) Days of Sama', 'Comedy', '2019'])
```

### Python 3 ###
```python  
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
```

### JavaScript ###
------

### JavaScript 1 ###
```js
// JS object organizes data in key-value pairs, like a Python dictionary
// Unlike Lists, key-value pairs in Objects are unordered
var movie = {
  name: "Star Wars",
  year: 1977,
  sequels: [1, 2, 3]
};
```

### JavaScript 2 ###
```js
// Like Python, JS allows value lookup via dot or bracket notation
console.log(movie.name);
console.log(movie["year"]);
console.log(movie.sequels[0]);

// Adds a key-value pair
movie.rating = 8.5;
console.log(movie);

// Deletes a key-value pair
delete movie.sequels;
console.log(movie);

// Checks if key exists in an object
if ("rating" in movie) {
  console.log("YES!");
}
```

### JavaScript 3 ###
```js
// Prints both keys and values
console.log(movie);

// Prints keys only
console.log(Object.keys(movie));

// Prints values only
console.log(Object.values(movie));

// Prints key-value pairs as array, like a Python zip
console.log(Object.entries(movie));
```
