const outer = (name) => {
  const inner = (greeting) => `${greeting} ${name}, how are you?`;
  return inner;
};

const aubGreeter = outer("Auberon");
console.log(aubGreeter("Hello"));
console.log(aubGreeter("Hey there"));
