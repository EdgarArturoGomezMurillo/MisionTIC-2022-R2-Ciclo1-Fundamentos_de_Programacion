import java.io.IOException;
import java.util.Scanner;

public class operacionesMatematicas {
    public int [] leer() throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.println("digite el numero 1");
        int numero1 = sc.nextInt();
        System.out.println("digite el numero 2");
        int numero2 = sc.nextInt();
        int valores[] = new int[2];
        valores [0] = numero1;
        valores [1] = numero2;
        return valores;
    }
    
}
