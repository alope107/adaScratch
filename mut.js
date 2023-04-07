const entries = [
  { id: 0, liked: true, author: {
    name: "something",
    school: {
      schoolName: "Ada",
      
    }
  } },
  { id: 77, liked: false },
];

const newEntries = [];

for (const entry of entries) {
  const newEntry = { ...entry };
  if (newEntry.id === 0) {
    newEntry.liked = !newEntry.liked;
  }
  newEntries.push(newEntry);
}

console.log(newEntries[0].liked);
console.log(entries[0].liked);
