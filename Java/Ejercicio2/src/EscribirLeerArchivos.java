import javax.swing.JOptionPane;

public class EscribirLeerArchivos {
    public static void main(String[] args) throws Exception {
        String nombre = JOptionPane.showInputDialog("Dijite su nombre");
        JOptionPane.showMessageDialog(null, " Hola " + nombre.toUpperCase());
        String ruta = JOptionPane.showInputDialog("introduzca la ruta del archivo");
        String texto = JOptionPane.showInputDialog("introduzca el texto que desea escribir");
        EscribirArchivo escribirA = new EscribirArchivo();
        LeerArchivo leerA = new LeerArchivo();
        leerA.leer(ruta);
        escribirA.escribir(ruta, texto);
    }
}
