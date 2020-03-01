// js解析环节变量提升
console.log(s);
var s = 'hello';

function func(){
    if(false){
        var web = 'hhl';

    }
    console.log(web);

}
func();

var a = 10;

