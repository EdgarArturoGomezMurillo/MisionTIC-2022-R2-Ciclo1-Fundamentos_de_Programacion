import java.io.FileReader;
import java.io.IOException;

public class leerArchivo {
    public void leer() {
        try {
            FileReader entrada = new FileReader("C:\\Users\\artur\\OneDrive\\Escritorio\\ejemplo.txt");
            int archivo = 0;
            // Casting convertir en un tipo de dato primitivo
            //System.out.println((char) archivo);
            while (archivo != -1) {
                //-1 significa que el archivo ha finalizado
                archivo = entrada.read();
                System.out.print((char) archivo);
            }
            entrada.close();
        } catch (IOException e) {
            System.out.println("no se pudo leer el archivo");
        }
    }
}
