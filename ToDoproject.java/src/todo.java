import java.util.ArrayList;
import java.util.Scanner;

public class todo
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        
        ArrayList<String> classname = new ArrayList<String>();
        ArrayList<String> tasks = new ArrayList<String>();    
        ArrayList<String> dates = new ArrayList<String>();   

        System.out.println("Enter class name: ");
        String name = scan.nextLine();

        System.out.println("Enter task:");
        String task = scan.nextLine();

        System.out.println("Enter due date:");
        String date = scan.nextLine();

        while (!name.equals("exit"))
        {
            classname.add(name);
            tasks.add(task);
            dates.add(date);

            System.out.println("Enter class name: ");
            name = scan.nextLine();

            if (name.equals("exit"))
            {
                break;
            }
            System.out.println("Enter task:");
            task = scan.nextLine();

            System.out.println("Enter due date:");
            date = scan.nextLine();

            
        }

        for(int i = 0; i < tasks.size(); i++)
        {
            System.out.println((i+1) + "." + classname.get(i) + "\n" + tasks.get(i) + "\ndue: " + dates.get(i) + "\n");
        }
    }
}

