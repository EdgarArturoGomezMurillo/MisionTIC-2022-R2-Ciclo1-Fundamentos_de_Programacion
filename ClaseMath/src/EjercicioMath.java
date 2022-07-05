import java.util.Scanner;

public class EjercicioMath {
    public static void main(String[] args) throws Exception {
        System.out.println("Numero PI: " + Math.PI);
        System.out.println("Numero Euler: " + Math.E);
        Scanner sc = new Scanner(System.in);
        System.out.println("dijite 1 numero");
        int numero1 = sc.nextInt();
        System.out.println("dijite 2 numero");
        int numero2 = sc.nextInt();
        System.out.println("la potencia es: " + Math.pow(numero1, numero2));
        System.out.println("Redondeo de pi: " + Math.round(Math.PI));
        double euler1 = Math.E;
        double eulerRedondeado = Math.round(euler1 * 100.0) / 100.0;
        System.out.println("Redonde o de euler: " + Math.round(euler1));
        System.out.println("renondeo de euler 2 decimales: " + eulerRedondeado);
        System.out.println("redondear al entero menor: " + Math.floor(euler1));
        System.out.println("redondear al entero mayor: " + Math.ceil(euler1));

    }
}
