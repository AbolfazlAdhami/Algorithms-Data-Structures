class Stack {
  constructor() {
    this.itmes = [];
  }
  push(value) {
    this.itmes.push(value);
  }
  pop() {
    return this.itmes.pop();
  }
}

const newStack = new Stack();
