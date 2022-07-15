import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite el precio del producto por unidad: ");
        double precio = sc.nextDouble();
        System.out.println("Digite el numero de productos vendidos: ");
        double vendidos = sc.nextDouble();
        System.out.println("El total de la venta es: "+ aplicariva(precio, vendidos));
    }//end main
    public static double aplicariva(double precio, double vendidos) {
        double totalproductos = precio * vendidos;
        double iva = totalproductos * 0.19;
        double total = totalproductos + iva;
        return total;
    }
}
