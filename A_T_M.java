import java.util.Scanner;
import java.util.Random;
public class A_T_M{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int balance = 10000;

        sc.close();


        System.out.println("_________WELCOME TO VVITU ATM______");
        System.out.println("Enter your card please");
        Random rand = new Random();
        int pasword = rand.nextInt(1000 , 10000 );
        System.out.println("your pasword is : " + pasword);

        System.out.print("Enter the password:");
        int enteredpasword = sc.nextInt();

        if(enteredpasword == pasword){
            System.out.println("options");
            System.out.println("1.check the balance");
            System.out.println("2.deposite money");
            System.out.println("3.withdraw money");
            System.out.println("4.exit");

            System.out.print("Enter the choice:");
            int choice = sc.nextInt();

            switch(choice){
                case 1 :
                    System.out.println("your balance is" + balance);
                break;

                case 2 :
                    System.out.print("Enter the amount to deposite:\n");
                    int depositeamount = sc.nextInt();
                    System.out.print("rupees" + depositeamount + "Successfully deposited\n");
                    balance = balance + depositeamount;
                    System.out.print("NEW BALANCE = " + balance);
                    break;

                case 3 :
                    System.out.print("enter the amount to witrhdraw:");
                    int withdrawamount = sc.nextInt();
                    if (withdrawamount <= balance){
                         System.out.print(withdrawamount + "withdraw successfully\n");
                    } 
                    else{
                        System.out.print("Insufficent balance!!!\n");
                    }
                    balance = balance-withdrawamount;
                    System.out.print("New balance = " + balance );
                    break;
                case 4 :
                    System.out.print("THANK YOU FOR USING VVITU ATM\n");
                    System.out.print("HAVE A GOOD DAY");
                    break;
                default : 
                    System.out.print("inavlid choice");
            }


        }
        else{
            System.out.print("Entered pasword is wrong \n TRY AGAIN!!!!");
        }
    }
}    