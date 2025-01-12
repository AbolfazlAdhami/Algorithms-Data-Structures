const message = "Hello World!";
function findFirstChar(str) {
  const tbale = {};
  for (let char of str) {
    if (tbale[char]) return char;
    tbale[char] = 1;
  }
}

function findFirstCharOld(str) {
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j < str.length; j++) {
      if (str[i] === str[j]) return str[i];
    }
  }
}

console.log(findFirstChar(message));
