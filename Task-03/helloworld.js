const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter the limit: ", (limit) => {
  for (let i = 2; i <= limit; i++) {
    let c = 1;
    for (let j = 2; j < i; j++) {
      if (i % j === 0) {
        c = 0;
        break;
      }
    }
    if (c === 1) {
      process.stdout.write(`${i} `);
    }
  }
  rl.close();
});
