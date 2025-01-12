import { LinkedList } from "./linked-list.js";

class Queue {
  constructor() {
    this.list = new LinkedList();
  }
  enQueue(value) {
    this.list.append(value);
  }
  deQueue() {
    return this.list.deleteHead();
  }
  toArray() {
    return this.list.toArray();
  }
}

const queue = new Queue();

queue.enQueue(1);
queue.enQueue(2);
queue.enQueue(3);
console.log(queue.toArray());
console.log(queue.deQueue());
console.log(queue.deQueue());
console.log(queue.toArray());
