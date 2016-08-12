import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;

public class P019_Counting_Sundays {


    private static int calcDays(String s, String e) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy MM dd");
        Date sDate = sdf.parse(s);
        Date eDate = sdf.parse(e);
        Calendar start = Calendar.getInstance();
        start.setTime(sDate);
        Calendar end = Calendar.getInstance();
        end.setTime(eDate);

        return calcDays(start, end);
    }

    private static int calcDays(Calendar start, Calendar end) throws ParseException {
        int result = 0;
        while (start.before(end)) {
            if (start.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
//                System.out.println(start.getTime().toString());
                result++;
            }
            start.add(Calendar.MONTH, 1);
        }
        return result;
    }

    public static void main(String[] args) {
        try {
            int _400 = calcDays("1900 1 1", "2299 12 31");
            Scanner in = new Scanner(System.in);
            int testNum = Integer.parseInt(in.nextLine());
            for (int i = 0; i < testNum; i++) {
                String a = in.nextLine();
                String b = in.nextLine();
                long aY = Long.parseLong(a.split(" ")[0]);
                long bY = Long.parseLong(b.split(" ")[0]);

                long delta = bY - aY;
                long mod = delta / 400;
                long left = delta % 400;

                long startYear = (aY - 1900) % 400 + 1900;
                long endYear = startYear + left;

                long result = 0;

                String start = startYear + " " + a.split(" ")[1] + " " + a.split(" ")[2];
                String end = endYear + " " + b.split(" ")[1] + " " + b.split(" ")[2];

                int diff = 0;
                SimpleDateFormat sdf = new SimpleDateFormat("yyyy MM dd");
                Date s = sdf.parse(start);
                Calendar sc = Calendar.getInstance();
                sc.setTime(s);
                if (!(sc.get(Calendar.DAY_OF_MONTH) == 1 && sc.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY)) {
                    sc.add(Calendar.MONTH, 1);
                    sc.set(Calendar.DAY_OF_MONTH, 1);
                }

                Date e = sdf.parse(end);
                Calendar ec = Calendar.getInstance();
                ec.setTime(e);
                if (ec.get(Calendar.DAY_OF_MONTH) == 1 && ec.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
                    diff++;
                }
                diff += calcDays(sc, ec);


                result = diff + _400 * mod;
                System.out.println(result);
            }
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }
}
