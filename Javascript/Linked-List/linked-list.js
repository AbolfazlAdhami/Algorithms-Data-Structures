export class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }
  //
  append(value) {
    const newElement = { value, next: null };

    if (this.tail) this.tail.next = newElement;

    this.tail = newElement;

    if (!this.head) this.head = newElement;
  }

  prepend(valeu) {
    const newElement = { valeu, next: this.head };
    this.head = newElement;

    if (!this.tail) this.tail = newElement;
  }

  delete(value) {
    if (!this.head) return null;
    while (this.head && this.head.value == value) {
      this.head = this.head.next;
    }

    let curElement = this.head;

    while (curElement) {
      if (curElement?.next?.value == value) {
        curElement.next = curElement.next.next;
      } else {
        curElement = curElement.next;
      }
    }
    if (this.tail.value == value) {
      this.tail = curElement;
    }
  }
  inserAfter(value, afterValue) {
    const existingValue = this.find(afterValue);
    if (existingValue) {
      const newElement = { value, next: existingValue.next };
      existingValue.next = newElement;
    }
  }

  find(value) {
    if (!this.head) return;
    let curElement = this.head;
    while (curElement) {
      if (curElement.value == value) {
        return curElement;
      }
      curElement = curElement.next;
    }
    return null;
  }
  deleteHead() {
    if (!this.head) return null;
    const deletedItem = this.head;
    if (this.head.next) {
      this.head = this.head.next;
    } else {
      this.head = null;
      this.tail = null;
    }

    return deletedItem;
  }
  toArray() {
    const elements = [];

    let curElement = this.head;

    while (curElement) {
      elements.push(curElement);
      curElement = curElement.next;
    }
    return elements;
  }
}

const linkedList = new LinkedList();
