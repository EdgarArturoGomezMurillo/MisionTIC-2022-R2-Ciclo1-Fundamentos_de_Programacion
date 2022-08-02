import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        Suma suma = new Suma();
        System.out.println("Digite el numero 1: ");
        suma.setNumero1(sc.nextInt());
        System.out.println("Digite el numero 2: ");
        suma.setNumero2(sc.nextInt());
        System.out.println("el total de la suma es = "+(suma.sumar(suma.getNumero1(), suma.getNumero2())));
        Resta resta = new Resta();
        System.out.println("Digite el numero 1 para restar: ");
        resta.setNumero1(sc.nextInt());
        System.out.println("Digite el numero 2 para restar: ");
        resta.setNumero2(sc.nextInt());
        System.out.println("el total de la resta es = "+(resta.restar(resta.getNumero1(), resta.getNumero2())));
    }
}
