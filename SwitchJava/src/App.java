
public class App {
    public static void main(String[] args) throws Exception {
        // traer del sistema el dia
        // Clase Date... fecha del sistema.. dia, año, mes...
        // int dia
        java.util.Date fecha = new java.util.Date();
        System.out.println("la fecha del sistema es: " + fecha);
        int dia = fecha.getDay();
        System.out.println("Dia: " + dia);
        switch (dia) {
            case 1:
                System.out.println("Hoy es Lunes");
                break;
            case 2:
                System.out.println("Hoy es Martes");
                break;
            case 3:
                System.out.println("Hoy es Miercoles");
                break;
            case 4:
                System.out.println("Hoy es Jueves");
                break;
            case 5:
                System.out.println("Hoy es Viernes");
                break;
            case 6:
                System.out.println("Hoy es Sabado");
                break;
            case 0:
                System.out.println("Hoy es Domingo");
                break;
            default:
                System.out.println("No es un dia valido");

        }

    }
}
