/**
 * Created by antoha on 17.01.2016.
 */

var N = parseInt(prompt("Введите число N"));
var delitel = 1;
var answer="";

while(N>delitel){
    if((N % delitel) != 0){
        delitel++;
    }else {
        answer = answer + delitel;
    };
}

alert(answer);