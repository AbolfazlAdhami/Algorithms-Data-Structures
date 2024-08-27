import { LinkedList } from "./linked-list.js";

class Stack {
  constructor() {
    this.items = new LinkedList();
  }
  push(value) {
    this.items.prepend(value);
  }
  pop() {
    return this.items.deleteHead();
  }
  toArray() {
    return this.items.toArray();
  }
}

const stack = new Stack();
stack.push("1");
stack.push("a");
stack.push(2);
console.log(stack.toArray());

// console.log("Frist POP Items", stack.pop());
stack.push("new Items");

console.log(stack.toArray());

console.log("Second POP Items", stack.pop());
console.log(stack.toArray());
