import java.util.Scanner;

public class Array {
    public static void main(String[] args) throws Exception {
        //declarar array --- unidimensional--- array
        //tipo de datos [] nombreVector = new tipo de datos [dimension]
        Scanner sc = new Scanner(System.in);
        System.out.print("porfavor digite la cantidad de elementos que va a tener el vector : ");
        int dimension = sc.nextInt();
        int [] vector = new int[dimension];
        int contar = 0;
        int numero;
        for (int i = 0; i < vector.length; i++) {
            System.out.print("Digite el numero " + (++contar + ":"));
            numero = sc.nextInt();
            vector[i] = numero;
        }
        //mostrar vector
        for (int i = 0; i < vector.length; i++) {
            System.out.print(vector[i]+"  ");
        }
        System.out.println(" ");
        System.out.println("El indice y el valor");
        for (int i = 0; i < vector.length; i++) {
            System.out.println("En el indice "+i+" esta el valor: "+vector[i]);
        }
    }//end main
}
