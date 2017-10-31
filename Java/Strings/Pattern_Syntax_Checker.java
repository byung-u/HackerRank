import java.io.*;
import java.util.*;
import java.util.regex.*;


public class Pattern_Syntax_Checker {

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while (testCases > 0) {
            String pat = in.nextLine();
            try {
                Pattern P = Pattern.compile(pat);
                System.out.println("Valid");
            }
            catch (PatternSyntaxException e) {
                System.out.println("Invalid");
            }
            testCases -= 1;
        }
    }
}
