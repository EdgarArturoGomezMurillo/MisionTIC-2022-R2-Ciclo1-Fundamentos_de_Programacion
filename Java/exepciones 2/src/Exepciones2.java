import javax.annotation.processing.SupportedOptions;

public class Exepciones2 {
    public static void main(String[] args) throws Exception {
        //clase operaciones matematicas sumar,restar,dividir
        operacionesMatematicas Op = new operacionesMatematicas();
        boolean continuar=true;
        do{
            try {
                Op.leer();
            }catch (Exception e) {
                System.out.println("opcion invalida");
            }
        }while(continuar);
    }
}
