class vegetable {
    constructor(name,color,taste,price){
        this.name = name;
        this.color = color;
        this.taste = taste;
        this.price = price;
    }
    
}
class veggies {
    constructor(name,color,size,taste,price,vitamins,quantity){
        super(name,color,size,taste,price);
        this.vitamins = vitamins;
        this.quantity = quantity;
    }
        
}
 const a = new vegetable("carrot","orange","mid sweet","1.5")
 console.log(a.taste)

 const b = new veggies("spinach","green","medium","leafy",0.5,"A",10)
 console.log(b.vitamins)
