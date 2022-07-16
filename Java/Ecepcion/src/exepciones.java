import java.util.InputMismatchException;
import java.util.Scanner;

import javax.annotation.processing.SupportedOptions;

public class exepciones {
    public static void main(String[] args) throws Exception {
        try{
        Scanner sc = new Scanner(System.in);
        System.out.println("dijite un numero");
        int numero = sc.nextInt();
        System.out.println("dijite otro numero");
        int numero2 = sc.nextInt();
        System.out.println("el numero digitado es : "+ numero);
        System.out.println("la division de los numeros es: "+ (numero/numero2) );
        }catch(InputMismatchException e){
            System.out.println("porfavor digite una opcion valida");
        }catch(ArithmeticException e){
            System.out.println("la division entre 0 no existe....");
        }finally{
            System.out.println("el sistema va a finalizar....");
        }
    }
}
