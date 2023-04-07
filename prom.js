const prom = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("foo");
  }, 300);
});

console.log(prom);

prom
  .then((value) => console.log(value))
  .catch((value) => console.log("Crashed with", value));

console.log("Doing something else");
