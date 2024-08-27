class HashTable {
  constructor() {
    this.size = 1000;
    this.product = Array(1000).fill(null);
  }
  hash(key) {
    let hash = 0;
    for (const char of key) {
      hash += char.charCodeAt(0);
    }
    return hash % this.size;
  }

  set(key, value) {
    const keyHash = this.hash(key);

    this.product[keyHash] = value;
  }
  get(key) {
    const keyHash = this.hash(key);

    return this.product[keyHash];
  }
}

const message = "HElow Owrld";

const tbale = new HashTable();
function findFirstChar(str) {
  for (let char of str) {
    if (tbale.get(char)) return char;

    tbale.set(char, 1);
  }
}

console.log(findFirstChar(message));
