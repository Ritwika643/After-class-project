var a = 'Hello, World!';
var b = 42;
var c = [500, 6, 71, 82];
var d = ['red', 'yellow', 'blue'];

console.log(c[1]); 
console.log(d[2]);

console.log(a);

 var e = c.join(' - ');
console.log(e);

d.push('black');
console.log(d)

function sum(a,b,c){
    return a + b + c;
}

function average(a,b,c){
    return (a + b + c) / 3;
} 

var result = average(100, 200, 30);
console.log(result);