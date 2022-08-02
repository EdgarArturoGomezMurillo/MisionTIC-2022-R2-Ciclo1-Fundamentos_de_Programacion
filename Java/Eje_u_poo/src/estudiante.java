public class estudiante extends persona {
    private String telefono;

    public estudiante() {
    }

    public estudiante(String telefono) {
        this.telefono = telefono;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    @Override
    public String toString() {
        return "--------- Datos del estudiante "+super.getNombre() +" ---------" + "\nNombre : " + super.getNombre() + "\nApellido : " + super.getApellido()
                + "\nTelefono : " + telefono;
    }

}
