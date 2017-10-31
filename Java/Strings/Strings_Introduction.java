import java.io.*;
import java.util.*;
import java.text.*;

public class Strings_Introduction {

    public static String capitalize(String s) {
        if (s.length() == 0) {
            return s;
        }
        return s.substring(0, 1).toUpperCase() + s.substring(1).toLowerCase();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();

        System.out.println(A.length() + B.length());

        int LexLen = Math.min(A.length(), B.length());
        for (int i = 0; i < LexLen; i++) {
            if (A.charAt(i) > B.charAt(i)) {
                System.out.println("Yes");
                break;
            }
            else {
                System.out.println("No");
                break;
            }
        }

        System.out.println(capitalize(A) + " " + capitalize(B));
    }
}
