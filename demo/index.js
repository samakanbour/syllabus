// JS object organizes data in key-value pairs, like a Python dictionary
// Unlike Lists, key-value pairs in Objects are unordered
var movie = {
  name: "Star Wars",
  year: 1977,
  sequels: [1, 2, 3]
};

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

// Prints both keys and values
console.log(movie);

// Prints keys only
console.log(Object.keys(movie));

// Prints values only
console.log(Object.values(movie));

// Prints key-value pairs as array, like a Python zip
console.log(Object.entries(movie));