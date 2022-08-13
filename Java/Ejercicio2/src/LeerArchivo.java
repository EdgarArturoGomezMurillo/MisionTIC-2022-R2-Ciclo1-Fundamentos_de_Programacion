import java.io.FileReader;
import java.io.IOException;

import javax.swing.JOptionPane;

public class LeerArchivo {
    public void leer(String ruta) {
        try {
            FileReader entrada = new FileReader(ruta);
            int archivo = 0;
            String fraseFinal = "";
            while (archivo != -1) {
                archivo = entrada.read();
                char caracter = (char) archivo;
                if (caracter >= 97 & caracter <= 122) {
                    caracter -= 32;
                } else if (caracter >= 65 & caracter <= 90) {
                    caracter += 32;
                }
                fraseFinal += caracter;
            }
            JOptionPane.showMessageDialog(null, fraseFinal);
            entrada.close();
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "no se pudo encontrar el archivo");
        }
    }
}
