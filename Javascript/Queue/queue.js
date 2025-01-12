class Queue {
  constructor() {
    this.items = [];
  }
  enQueue(value) {
    this.items.unshift(value);
  }
  deQueue() {
    return this.items.pop();
  }
  toArray() {
    return this.items;
  }
}

const queue = new Queue();
queue.enQueue("item 1");
queue.enQueue("item 2");
queue.enQueue("item 3");
console.log(queue.toArray());
queue.deQueue();
console.log(queue.toArray());
queue.deQueue();
console.log(queue.toArray());
