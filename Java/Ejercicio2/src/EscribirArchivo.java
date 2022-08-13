import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JOptionPane;

public class EscribirArchivo {
    public void escribir(String ruta, String frase) {

        try {
            FileWriter escritura = new FileWriter(ruta);
            for (int i = 0; i < frase.length(); i++) {
                escritura.write(frase.charAt(i));
            }
            JOptionPane.showMessageDialog(null, "Archivo escrito exitosamente");
            escritura.close();
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Archivo no pudo escribirse");
        }

    }
}
