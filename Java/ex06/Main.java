import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        float a, b, result;

        a = in.nextFloat();
        b = in.nextFloat();
        result=a * b;
        System.out.printf("%.2f", result);
        in.close();
    }
}