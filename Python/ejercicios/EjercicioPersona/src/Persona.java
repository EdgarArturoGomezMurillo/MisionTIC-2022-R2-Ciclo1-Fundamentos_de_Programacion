public class Persona {
    private String nombre;
    private String apellidos;
    private Integer codigo;
    private Integer edad;
    
    public Persona() { 
    }

    public Persona(String nombre, String apellidos, Integer codigo, Integer edad) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.codigo = codigo;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public Integer getEdad() {
        return edad;
    }

    public void setEdad(Integer edad) {
        this.edad = edad;
    }

    public Integer getCodigo() {
        return codigo;
    }

    public void setCodigo(Integer codigo) {
        this.codigo = codigo;
    }

    @Override
    public String toString() {
        return "Persona { apellidos = " + apellidos + ", codigo = " + codigo + ", nombre = " + nombre + ", edad = " + edad + "}";
    }
    
    
}
