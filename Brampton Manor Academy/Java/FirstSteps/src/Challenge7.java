public class Challenge7 {
    public static void main(String args[]){
        int number = Integer.parseInt(args[0]);
        boolean isPrime = true;
        for(int i = 2; i < number; i++) {

            if (number % i == 0) {
                isPrime = false;
            }
        }
        if (isPrime == true){
            System.out.print(number + " is prime");
        }
        else{
            System.out.print(number + " is not prime");
        }

    }
}
