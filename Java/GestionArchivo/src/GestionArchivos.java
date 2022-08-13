public class GestionArchivos {
    public static void main(String[] args) throws Exception {
        leerArchivo acceder = new leerArchivo();
        acceder.leer();
        EscribirArchivo escribirA = new EscribirArchivo();
        escribirA.escribir();
    }
}
