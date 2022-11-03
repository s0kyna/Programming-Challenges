public class Calculator {

    private static int addition(int a, int b){
        int total = a + b;
        return total;
    }
    private static int subtraction(int a, int b) {
        int total = a - b;
        return total;
    }
    private static int multiply(int a, int b) {
        int total = a * b;
        return total;
    }
    private static int division(int a, int b) {
        int total = a / b;
        return total;
    }

    private static int power(int a, int b) {
        int total = a;
        for (int i = 0; i < b-1 ; i++) {
            total = total * a;
        }
        return total;
    }
    private static int factorial(int a) {
        int total = a;
        for (int i = 1; i < a ; i++) {
            total = total * i;
        }
        return total;
    }



    public static void main(String[] args){
        String choice = args[0];
        int firstValue = Integer.parseInt(args[1]);
        int secondValue = Integer.parseInt(args[2]);

        switch (choice){
            case "addition":
                int answerA = addition(firstValue,secondValue);
                System.out.println(answerA);
                break;
            case "subtraction":
                int answerS = subtraction(firstValue,secondValue);
                System.out.println(answerS);
                break;
            case "multiplication":
                int answerM = multiply(firstValue,secondValue);
                System.out.println(answerM);
                break;
            case "division":
                int answerD = division(firstValue,secondValue);
                System.out.println(answerD);
                break;
            case "power":
                int answerP = power(firstValue,secondValue);
                System.out.println(answerP);
                break;
            case "factorial":
                int answerF = factorial(firstValue);
                System.out.println(answerF);
                break;
        }

    }
}
