const SALESTAX = 0.12;

class Zine {
  constructor(title, contributor, price = 9) {
    this.title = title;
    this.contributor = contributor;
    this.price = price;
  }

  totalPrice() {
    return this.price * (1 + SALESTAX);
  }
}

const chefZine = new Zine("Croissants 101", "Julia Child");
const zineObject = {
  title: "Croissants 101",
  contributor: "Julia Child",
  price: 9,
  totalPrice: function () {
    return this.price * (1 + SALESTAX);
  },
};
console.log(zineObject.totalPrice());
console.log(zineObject.contributor);
// > 4.48
