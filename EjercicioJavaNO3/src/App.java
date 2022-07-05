import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Porfavor dijite un numero entero : ");
        int numero = sc.nextInt();
        System.out.println("El doble del numero "+ numero + " es = " + doblenumero(numero));
        System.out.println("el triple del numero "+ numero + " es = " + triplenumero(numero)); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Porfavor dijite el numero del cual quiere saber la mitad: ");
        int numerom = scanner.nextInt();
        System.out.println("La mitad del numero "+ numerom + " es = " + (numerom));
    }//end main
    public static int doblenumero(int numero) {
        return numero * 2;
    }
    public static int triplenumero(int numero){
        return numero * 3;
    }
    public static int mitadnumero(int numerom) {
        return numerom / 2;
    }
}

