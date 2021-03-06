console.log(s);//undefined
var s = 'hello';
// 分两步：变量声明(definition)，变量初始化(initialization)
// var s;
// s = 'hello';
// js预解析环节会把所有的变量声明提升
// 因为还没初始化，所以打印结果为undefined

function func(){
    if(false){
        var web = 'hhl';

    }
    console.log(web);//undefined
}
func();

// Uncaught ReferenceError: Cannot access 'c' before initialization
// 使用let声明变量，仍然有变量声明提升，
// 但是定义了死区，变量只能在初始化之后使用。
// console.log(b);
// let b = 'hello';

// const也有类似效果，
// 强烈建议使用let const

// var c = 'he'
// function func1(){
//     console.log(c);
//     let c = 'hello';
// }
// func1();


// p10 作用域
// p11 全局污染

// p12 优先：避免变量污染
// let 具有块作用域
// aaa
{
    var web2 = 'aaa';
}
console.log(web2);

// Uncaught ReferenceError: web1 is not defined
// {
//     let web1 = 'aaa';
// }
// console.log(web1);

// p14
// var 会污染window对象，let不会

// var screenLeft = 99;
let screenLeft = 99
console.log(window.screenLeft);

// 用let避免重复声明
// let web3 = 11;
// let web3 = 11;
// Uncaught SyntaxError: Identifier 'web3' has already been declared

//p15
const HOST = {
    url: "www.baidu.com",
    port: "30"
}

// 冻结，无法修改
Object.freeze(HOST);

HOST.port = '89';
console.log(HOST.port);
// 30

//p16
