import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n;
        double max, min;
        n = in.nextInt();
        double[] array = new double[n];
        
        for(int i = 0; i < n; i++){
            array[i] = in.nextDouble();
        }
        in.close();
        max = array[0];
        min = array[0];
        for(int i = 0; i < n; i++){
           if (min > array[i]) {
               min = array[i];
           }
            if (max < array[i]) {
                max = array[i];
            }
        }
        System.out.println(min);
        System.out.println(max);
    }
}