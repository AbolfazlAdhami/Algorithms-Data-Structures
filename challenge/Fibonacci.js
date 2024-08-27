function generateFibonacci(count) {
  let fibonacciSequence = [];

  // Helper function to calculate Fibonacci numbers
  function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
  }

  // Generating Fibonacci sequence
  for (let i = 1; i <= count; i++) {
    fibonacciSequence.push(fibonacci(i));
  }
  console.log(fibonacciSequence, "by Callback");
}

// Example usage of generateFibonacci with a callback function
generateFibonacci(5);

function fib(n) {
  //build
  let fibonacci = [1, 1];

  for (let i = 2; i < n; i++) {
    fibonacci.push(fibonacci[i - 2] + fibonacci[i - 1]);
  }
  //retunr
  return fibonacci;
}

console.log(fib(5), "Build fibonacci by for loop");
