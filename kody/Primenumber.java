import java.util.Scanner;

public class Primenumber {

    public static int fact(int n){

        int fact =1;
        if(n ==0)
        return 1;

        else{
            for(int i=1; i<=n ; i++)
            {
                fact = fact * i;
            }
            return fact;
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fact(n));
    }
}