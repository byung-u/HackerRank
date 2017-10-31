import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class End_of_file {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s;
        int line = 1;

        while (scan.hasNext() == true) {
            s = scan.nextLine();
            System.out.format("%d %s\n", line, s);
            line += 1;
        }
    }
}