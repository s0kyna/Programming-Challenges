public class Lesson2_programmingchallenges {
    public static void main(String[] args){
        for_loop();
        loop_cars();
        if_day();
        switch_day();
        get_10th();
    }
    public static void for_loop(){
        for (int i = 0; i<5;i++){
            System.out.println("Yes");
        }
    }
    public static void loop_cars(){
        String[] cars = {"Volvo","BMW","Ford","Mazda"};
        for (String el : cars){
            System.out.println(el);
        }

    }
    public static void if_day(){
        int day = 4;
        if (day == 6){
            System.out.println("Today is Saturday");
        }
        else if (day == 7) {
            System.out.println("Today is Sunday");
        }
        else{
            System.out.println("Looking forward to the weekend");
        }
    }
    public static void switch_day(){
        int day = 4;
        switch(day){
            case 4:
                System.out.println("Looking forward to the weekend");
                break;
            case 6:
                System.out.println("Today is Saturday");
                break;
            case 7:
                System.out.println("Today is Sunday");
                break;
        }
    }
    public static void get_10th(){
        int[] myNumbers = {1,2,3};
        try {
            System.out.println(myNumbers[10]);

        } catch (Exception e){
            System.out.println("Error");

        }
    }
}
