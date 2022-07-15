public class EjercicioPersona {
    public static void main(String[] args) throws Exception {
        //instancia de clase -- objeto
        //NombreClase nombreObjeto = new NombreClase();
        Persona persona1 = new Persona();
        Persona persona2 = new Persona();
        persona1.setCodigo(1);
        persona1.setNombre("Arturo");
        persona1.setApellidos("Gomez Murillo");
        persona1.setEdad(19);
        System.out.println("la persona con codigo " + persona1.getCodigo()+ " tiene los siguientes datos: " );
        System.out.println("Nombre : " + persona1.getNombre()+" "+persona1.getApellidos());
        System.out.println("Edad : " + persona1.getEdad());

        persona2.setCodigo(2);
        persona2.setNombre("Artorias");
        persona2.setApellidos("Gomez Suarez");
        System.out.println(persona1.toString());
        System.out.println("la persona con codigo " + persona2.getCodigo()+ " tiene los siguientes datos: " );
        System.out.println("Nombre : " + persona2.getNombre()+" "+persona2.getApellidos());
    }
}
