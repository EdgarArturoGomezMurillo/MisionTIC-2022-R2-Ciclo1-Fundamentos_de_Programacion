import java.io.FileWriter;
import java.io.IOException;

public class EscribirArchivo {
    public void escribir() {
        String frase = "Esto es una frase escrita desde java";
        try {
            FileWriter escritura = new FileWriter("C:\\Users\\artur\\OneDrive\\Escritorio\\ejemplo.txt");
            for (int i = 0; i < frase.length(); i++) {
                escritura.write(frase.charAt(i));
            }
            System.out.println("Arcivo escrito exitosamente");
            escritura.close();
        } catch (IOException e) {
            System.out.println("No se pudo escribir el archivo");
        }

    }
}
