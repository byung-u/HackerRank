import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Anagrams {

    static boolean isAnagram(String a, String b) {

        List<String> al = Arrays.asList(a.toLowerCase().split(""));
        List<String> bl = Arrays.asList(b.toLowerCase().split(""));

        Map<String, Integer> counter = new HashMap<String, Integer>();
        // Counter
        for (String s : al) {
            Integer LastVal = counter.get(s);
            counter.put(s, LastVal == null ? 1 : LastVal + 1);
        }
        // System.out.println(counter);
        // Subtract
        for (String s : bl) {
            Integer LastVal = counter.get(s);
            counter.put(s, LastVal == null ? 1 : LastVal - 1);
        }
        // System.out.println(counter);

        int total = 0;    
        for (String key: counter.keySet()) {
            // System.out.println(key +  " " + counter.get(key));
            total += Math.abs(counter.get(key));
        }
        // System.out.println(total);
        if (total == 0) {
            return true;
        }
        else {
            return false;
        }
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
