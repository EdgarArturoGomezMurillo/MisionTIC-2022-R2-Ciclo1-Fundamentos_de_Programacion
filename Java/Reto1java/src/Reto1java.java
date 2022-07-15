public class Reto1java {
    public static void main(String[] args) {

        BecaUniversitaria becaUniversitaria = new BecaUniversitaria(48, 10000,2.0);
        System.out.println(becaUniversitaria.calcularInteresSimple());
        System.out.println(becaUniversitaria.calcularInteresCompuesto());
        System.out.println(becaUniversitaria.compararInversion());
    }
}
