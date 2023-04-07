Object.prototype.protoKey = "foo";

const thing = {
  ownKey: "bar",
};

const doSomething = console.log;

const foo = thing;

for (key in foo) {
  if (Object.hasOwn(foo, key)) {
    doSomething(key);
  }
}

// console.log(thing.balls);

// for (const key in thing) {
//   console.log(`For in: ${key}`);
// }
// console.log();
// for (const key of Object.keys(thing)) {
//   console.log(`For of: ${key}`);
// }
