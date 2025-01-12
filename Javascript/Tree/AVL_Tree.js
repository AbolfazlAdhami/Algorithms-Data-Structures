class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
  get leftDepth() {
    if (!this.left) {
      return 0;
    }
    return this.left.depth + 1;
  }
  get righthDepth() {
    if (!this.right) {
      return 0;
    }
    return this.right.depth + 1;
  }
  get depth() {
    return Math.max(this.leftDepth, this.righthDepth);
  }
  get balancedFactor() {
    return this.leftDepth - this.righthDepth;
  }
  add(value) {
    if (this.value == null) {
      this.value = value;
      return;
    }
    if (this.value < value) {
      if (this.right) {
        this.right.add(value);
        return;
      }
      const newNode = new Node(value);
      this.right = newNode;
      return;
    }
    if (this.value > value) {
      if (this.left) {
        this.left.add(value);
        return;
      }
      const newNode = new Node(value);
      this.left = newNode;
      return;
    }
  }
  find(value) {
    if (this.value === value) {
      return this.value;
    }
    if (this.value < value && this.right) {
      return this.right.find(value);
    }
    if (this.value > value && this.left) {
      return this.left.find(value);
    }
  }
}

class Tree {
  constructor() {
    this.root = new Node(null);
  }

  add(value) {
    this.root.add(value);
  }
  find(value) {
    return this.root.find(value);
  }
}

const tree = new Tree();

tree.add(1);
tree.add(2);
tree.add(3);

console.log(tree);
