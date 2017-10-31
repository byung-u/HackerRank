import java.io.*;
import java.util.*;
import java.text.*;

public class Date_and_Time {

    public static String getDay(String day, String month, String year) {
        String dateInString = day + "/" + month + "/" + year;
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat formatter2 = new SimpleDateFormat("EEEE");
        try {
            Date date = formatter.parse(dateInString);
            return (formatter2.format(date).toUpperCase());

        } catch (ParseException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }
}
