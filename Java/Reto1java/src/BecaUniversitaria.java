public class BecaUniversitaria {
    //atributos
    private int tiempo;
    private double monto;
    private double interes;
    
    public BecaUniversitaria() {

    }

    public BecaUniversitaria(int tiempo, double monto, double interes) {
        this.tiempo = tiempo;
        this.monto = monto;
        this.interes = interes;
    }
    public double calcularInteresSimple( ){
       double interesSimple = monto * (interes/100)* tiempo;
        return Math.round(interesSimple);
    }
   
    public double calcularInteresCompuesto(){
        double interesCompuesto = monto * (Math.pow(1+interes/100, tiempo)-1);
        return Math.round(interesCompuesto);
    }
    public String compararInversion (int pTiempo, double pMonto, double pInteres){

        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;

        double diferencia = calcularInteresCompuesto() -  calcularInteresSimple();
        if (diferencia != 0){
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;}
        else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }
    public String compararInversion ( ){
        double diferencia = calcularInteresCompuesto() -  calcularInteresSimple();
        if (diferencia != 0){
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;}
        else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

    
}
