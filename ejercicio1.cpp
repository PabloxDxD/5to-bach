#include <iostream>
#include <string>
#include <Cmath>
using namespace std;

int main(void){
    int res, num1, num2;
    int suma, resta, multi;
    float division, potencia, raiz;
    double a, b, c;

    string menu = "\t\tMENU\n\t1. SUMA\n\t2. RESTA\n\t3. MULTIPLICACION\n\t4. DIVISION\n\t5. POTENCIACION\n\t6. RAIZ CUADRADA\n";
    cout << "Ingrese el primer numero: ";
    cin >> num1;
    cout << "Ingrese el segundo numero: ";
    cin >> num2;
    cout << menu;
    cin >> res;

    switch (res){
    case 1:
            if(suma = num1 + num2 ){
            cout << "La suma de sus numeros son: " << endl;
        }
        break;
    case 2:
        if(resta = num1 - num2){
            cout << "La respuesta de su resta es: " << resta << endl;
        }
        break;
    case 3:
           if(multi = num1 * num2){
            cout << "La respuesta de su multiplicacion es: " << multi << endl;
        }
        break;
    case 4:
            if(num2!=0){
                        cout << num1 / num2 << endl;
                    }else{
                        cout << "No se puede dividir entre 0" << endl;
                    }
        break;
    case 5:
            cout << "Ingrese un numero: " << endl;
            cin >> a;
            cout << "Ingrese el exponente a elevar: " << endl;
            cin >> b;
            c=pow(a,b);
            cout <<"El numero "<<a << endl <<"elevado a la potencia "<<b<< endl<<"es :  "<<c<< endl;
            break;
        break;
    case 6:
            double a;
            cout << "Ingresa un numero para sacarle la raiz cuadrada: " << endl;
            cin >> a;
            float raiz = sqrt(a);
            cout << "La raiz cuadrada de  " << a << " es  " << raiz;
        break;
    }
}