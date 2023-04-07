// Top level functions
/*
def praise_dog(name):
  .....
*/
console.log(praiseDog("Sofia"));

function praiseDog(name) {
  return `${name} is a good doggo!`;
}

// Functions assigned some variable (non-arrow)
const praiseDogMore = function (name) {
  return `${name} is a very good doggo!`;
};

console.log(praiseDogMore("Maya"));

// Arrow functions
const praiseDogEvenMore = (name) => `${name} is an extremely good doggo!`;

console.log(praiseDogEvenMore("Sullyvan"));

// Anonymous function

const dogs = ["Sullyvan", "Sofia", "Maya"];
const praisedDogs = dogs.map((name) => `${name} is an extremely good doggo!`);

console.log(praisedDogs);

const nums = [1, 2, 3];
let doubledNums = nums.map((number) => number * 2);

console.log(doubledNums);

function timesTwo(number) {
  return number * 2;
}

doubledNums = nums.map(timesTwo);

console.log(doubledNums);

// Closures

function dogDescriber(name) {
  let specificDescriber = function (adjective) {
    return `${name} is very ${adjective}`;
  };
  return specificDescriber;
}

let dahliaDescriber = dogDescriber("Dahlia");
dahliaDescriber = dogDescriber("DAHLIA");
let banuDescriber = dogDescriber("Banu");
console.log(dahliaDescriber("messy"));
console.log(banuDescriber("sassy"));
console.log(dahliaDescriber("cute"));

// Reduce
const arr = [2, 4, 6, 8];

const total = arr.reduce((accumulated, current) => accumulated + current, 0);
/*
a    c
0    2
2    4
6    6
12   8

  20

acc = starting
for current in array:
   acc = func(acc, current)
return acc
*/

console.log(total);

const SALESTAX = 0.08;

class Zine {
  constructor(title, contributor, price) {
    this.title = title;
    this.contributor = contributor;
    this.price = price;
  }

  totalPrice() {
    return this.price * (1 + SALESTAX);
  }
}

const chefZine = new Zine("So you want to be a pastrychef", "Julia Child", 1.0);
console.log(chefZine.totalPrice());
// > 1.08
