import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("digite un numero entero: ");
        int numero = sc.nextInt();
        System.out.println("digite el numero de cifras que desea quitar al numero anterior: ");
        int m = sc.nextInt();
        System.out.println("el numero "+ numero+ " con"+ m + "cifras menos es = "+ quitarCifras(numero, m));

    }//end main
    public static String quitarCifras(int numero, int m) {
        String numeroS = String.valueOf(numero);
        String subCadena = numeroS.substring(0, numeroS.length() -m);
        return subCadena;
    }

}
