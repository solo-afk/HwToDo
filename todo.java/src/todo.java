import java.util.ArrayList;
import java.util.Scanner;

public class todo
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> tasks = new ArrayList<String>();    

        System.out.println("Enter hw:");
        String hw = scan.nextLine();
        while (!hw.equals("exit"))
        {
            tasks.add(hw);
            System.out.println("Enter hw:");
            hw = scan.nextLine();
        }

        for(int i = 0; i < tasks.size(); i++)
        {
            System.out.println((i+1) + "." + tasks.get(i) + "\n");
        }
    }
}

