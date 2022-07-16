import java.lang.invoke.StringConcatFactory;
import java.util.Scanner;

public class Genericos {
    public static void main(String[] args) throws Exception {
        var integerBox = new Box<Integer>();
        Scanner sc = new Scanner(System.in);
        System.out.println("digite una variable entera: ");  
        integerBox.setT(sc.nextInt());
        System.out.println("el numero digitado es : "+ integerBox.getT());
        sc.nextLine();//limpiar buffer
        var StringBox = new Box<String>();
        System.out.println("digite una cadena de texto: ");
        StringBox.setT(sc.nextLine());
        System.out.println("la cadena de texto es: "+ StringBox.getT());
        
    }
}
