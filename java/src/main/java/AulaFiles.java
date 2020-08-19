import java.io.File;

public class AulaFiles {
    public static void main(String[ ] args) {
        File x = new File("C:\\sololearn\\test.txt");
        if(x.exists()) {
            System.out.println(x.getName() +  "exists!");
        }
        else {
            System.out.println("The file does not exist");
        }
    }
//    try {
//        File x = new File("C:\\sololearn\\test.txt");
//        Scanner sc = new Scanner(x);
//          while(sc.hasNext()) {
//            System.out.println(sc.next());
//        }
//        sc.close();
//    } catch (FileNotFoundException e) {
//        System.out.println("Error");
//    }

// import java.util.Formatter;
//
//    public class MyClass {
//        public static void main(String[ ] args) {
//            try {
//                Formatter f = new Formatter("C:\\sololearn\\test.txt");
//                f.format("%s %s %s", "1","John", "Smith \r\n");
//                f.format("%s %s %s", "2","Amy", "Brown");
//                f.close();
//            } catch (Exception e) {
//                System.out.println("Error");
//            }
//        }
//    }
}
