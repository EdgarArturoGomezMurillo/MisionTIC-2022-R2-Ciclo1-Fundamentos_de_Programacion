import java.util.Scanner;
import java.util.Locale.Category;

public class Universidad {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        // Estudiantes
        System.out.println("-------------------- SECCION DE ESTUDIANTES --------------------");
        System.out.print("Porfavor digite la cantidad de estudiantes que quiere ingresar: ");
        int nEstudiantes = sc.nextInt();
        sc.nextLine();// limpiar
        estudiante[] estudiantes = new estudiante[nEstudiantes];
        for (int i = 0; i < estudiantes.length; i++) {
            System.out.println("Digite el nombre del estudiante " + (i + 1) + " : ");
            String nombre = sc.nextLine();
            System.out.println("Digite el apellido del estudiante " + (i + 1) + " : ");
            String apellido = sc.nextLine();
            System.out.println("Digite el telefono del estudiante " + (i + 1) + " : ");
            String telefono = sc.nextLine();
            estudiantes[i] = new estudiante(telefono);
            estudiantes[i].setNombre(nombre);
            estudiantes[i].setApellido(apellido);
        }
        // Empleados
        System.out.println("-------------------- SECCION DE EMPLEADOS --------------------");
        System.out.println("---------------- DIRECTOR ----------------");
        System.out.print("Porfavor digite la cantidad de directores que quiere ingresar: ");
        int nDirectores = sc.nextInt();
        sc.nextLine();// limpiar
        director[] directores = new director[nDirectores];
        for (int i = 0; i < directores.length; i++) {

            System.out.println("Digite el nombre del director " + (i + 1) + " : ");
            String nombre = sc.nextLine();
            System.out.println("Digite el apellido del director " + (i + 1) + " : ");
            String apellido = sc.nextLine();
            System.out.println("Digite la categoria del director " + (i + 1) + " : ");
            String categoria = sc.nextLine();
            directores[i] = new director(categoria);
            directores[i].setNombre(nombre);
            directores[i].setApellido(apellido);
        }
        // Profesor
        System.out.println("---------------- PROFESOR ----------------");
        System.out.print("Porfavor digite la cantidad de profesores que quiere ingresar: ");
        int nProfesores = sc.nextInt();
        sc.nextLine();// limpiar
        profesor[] profesores = new profesor[nProfesores];
        for (int i = 0; i < profesores.length; i++) {

            System.out.println("Digite el nombre del profesor " + (i + 1) + " : ");
            String nombre = sc.nextLine();
            System.out.println("Digite el apellido del profesor " + (i + 1) + " : ");
            String apellido = sc.nextLine();
            System.out.println("Digite la categoria del profesor " + (i + 1) + " : ");
            String categoria = sc.nextLine();
            profesores[i] = new profesor(categoria);
            profesores[i].setNombre(nombre);
            profesores[i].setApellido(apellido);
        }
        System.out.println("---------------- DECANO ----------------");
        System.out.println("Digite cuantos decanos tiene su Universidad: ");
        int nDecanos = sc.nextInt();
        sc.nextLine();// limpiar
        decano[] decanoI = new decano[nDecanos];
        for (int i = 0; i < decanoI.length; i++) {
            System.out.println("Digite el nombre del decano: ");
            String nombre = sc.nextLine();
            System.out.println("Digite el apellido del decano: ");
            String apellido = sc.nextLine();
            System.out.println("Digite la categoria del decano: ");
            String categoria = sc.nextLine();
            decanoI[i] = new decano(categoria);
            decanoI[i].setNombre(nombre);
            decanoI[i].setApellido(apellido);
        }
        System.out.println("-------------------- DATOS DE ESTUDIANTES --------------------");
        for (int i = 0; i < estudiantes.length; i++) {
            System.out.println(estudiantes[i].toString());
        }
        System.out.println("-------------------- DATOS DE EMPLEADOS --------------------");
        for (int i = 0; i < directores.length; i++) {
            System.out.println(directores[i].toString());
        }
        for (int i = 0; i < profesores.length; i++) {
            System.out.println(profesores[i].toString());
        }
        for (int i = 0; i < decanoI.length; i++) {
            System.out.println(decanoI[i].toString());
        }
    }
}
