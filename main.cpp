#include <iostream>

using namespace std;

int main()
{
    /*unsigned int num_max = 0, input;
    do {
        cout << "Ingresa un numero: ";
        cin >> input;
        if (input > num_max) num_max = input;
    } while (input != 0);
    cout << num_max << endl; */

    /*bool is_square_perfect = false;
    unsigned int input = 0;

    cout << "Ingresa un numero: ";
    cin >> input;

    for (unsigned int i = 0; i*i <= input; i++){
        if (i*i == input) is_square_perfect = true;
    }
    if (is_square_perfect) {
        cout << "Cuadrado perfecto" << endl;
    } else {
        cout << "No es Cuadrado perfecto" << endl;
    } */

    /*int numero1, numero2, temp;
    bool found = false;

    cout << "Ingresa el numero 1: ";
    cin >> numero1;
    cout << "Ingresa el numero 2: ";
    cin >> numero2;

    for (int i = 1; !found; i++){
        if ((numero1 * i) % numero2 == 0) {
            found = true;
        }
        temp = numero1 * i;
    }
    if (found) {
        cout << "El MCP entre " << numero1 << " y " << numero2 << " es: " << temp << endl;
    } */

    /*int num, digit, pot = 1, total = 0;

    cout << "Ingresa un numero: ";
    cin >> num;

    if (num > 0){
        while (num != 0){
            digit = num % 10;
        for (int i = 0; i < digit; i++){
                pot *= digit;
            }
            num /= 10;
            total += pot;
            pot = 1;
        }
        cout << "La suma es: " <<total << endl;
    } else cout << "El numero debe ser mayor que 0" << endl; */

    /*int numero;
    float perimetro = 0, area = 0;

    cout << "Ingresa el radio: ";
    cin >> numero;

    perimetro = 2*3.1416*numero;
    area = 3.1416*(numero*numero);

    cout << "Perimetro: " << perimetro << endl;
    cout << "Area: " << area << endl;*/

    /*int numero;
    cout << "Ingresa un numero: ";
    cin >> numero;
    cout << "Los multiplos de " << numero << " menores que 100" << endl;
    for (int i = 1; i*numero < 100; i++) if (i*numero % numero == 0) cout << i*numero << endl; */

    /*int numero;
    cout << "Ingresa un numero: ";
    cin >> numero;

    for (int i = 1; i <= 10; i++) cout << i << "x" << numero << " = " << numero*i << endl; */

    /*int numero, pot = 1;
    cout << "Ingresa un numero: ";
    cin >> numero;
    for (int i = 1; i <= 5; i++){
        pot *= numero;
        cout << numero << "^" << i << " = " << pot << endl;
    } */

    /*int numero;
    cout << "Ingresa un numero: ";
    cin >> numero;
    cout << "Los divesores de " << numero << " son:" << endl;
    for (int i = 1; i <= numero; i++) if (numero % i == 0) cout << i << endl; */

    /*int i = 1;
    do {
        cout << i << "  " << 50 - (i - 1) << endl;
        i++;
    } while (i <= 50);*/

    /*unsigned int suma = 0, input;
    do {
        cout << "Ingresa un numero: ";
        cin >> input;
        suma += input;
    } while (input != 0);
    cout << "El resultado de la sumatoria es: " << suma << endl;*/

    unsigned int prom = 0, suma = 0, input, contador = 0;
    do {
        cout << "Ingresa un numero: ";
        cin >> input;
        suma += input;
        contador++;
    } while (input != 0);
    prom = suma / (contador - 1);
    cout << "El resultado de la sumatoria es: " << prom << endl;
}
