
import java.util.Locale;
import java.util.Scanner;

class ConverterString {

    String toLowerCase(String str){
        return str.toLowerCase();
    }
    String toUpperCase(String str){
         return str.toUpperCase(Locale.ROOT);
    }
}

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        ConverterString converter = new ConverterString();
        String str, strUpper, strLower;
        str=in.nextLine();
        strUpper=converter.toUpperCase(str);
        strLower=converter.toLowerCase(str);

        System.out.println(strUpper);
        System.out.println(strLower);
    }
}