var a  = [ 86,56,29,90,33,0,6,7,69,143]

console.log(a)

// ascending order

a.sort((x, y) => x - y)

console.log(a)

// descending order

a.sort((x, y) => y - x)

console.log(a)

var b = a.map(x => x * 2)

console.log(b)