import java.util.*;

class GFG {
    public static void main(String args[]) {
        // Implement Scanner Class
        // Take all inputs
        // Print all the values
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        float b = sc.nextFloat();
        long c = sc.nextLong();
        byte d = sc.nextByte();
        sc.nextLine();
        String s = sc.nextLine();
        System.out.printf("%d\n%.3f\n%d\n%d\n%s\n", a, b, c, d, s);
    }
}
