import java.io.IOException;
import java.io.PrintWriter;
import java.io.UTFDataFormatException;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/login1")
public class login extends HttpServlet 
{
	public void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//student st=new student();
		int a;
		PrintWriter out=resp.getWriter();
		String email2= req.getParameter("uname");
		String pass= req.getParameter("psw");
		
		int n=email2.lastIndexOf('/');
		String email,roll;
		email=email2.substring(0, n);
		roll=email2.substring(n+1);
		System.out.println("email="+email);
		System.out.println("roll="+roll);
		
		
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
				Connection con= DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","1234");
				Statement ps=con.createStatement();
				ResultSet re=ps.executeQuery("SELECT * from student where email=\""+email+"\" AND contact=\""+pass+"\" ");
				
				
				while (re.next()) {
					out.println("Roll No 	: "+re.getInt(1));
					out.println("Name	 	: "+re.getString(2));
					out.println("Email	 	: "+re.getString(3));
					out.println("Course 	: "+re.getString(5)+" ("+re.getString(4)+") ");
					out.println("Gender	 	: "+re.getString(6));
					out.println("Phno.	 	: "+re.getString(7));
					out.println("DOB	 	: "+re.getString(8));
					out.println("Address 	: "+re.getString(9));
					}
				
				Connection con1= DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","1234");
				Statement ps1=con1.createStatement();
				ResultSet re1=ps1.executeQuery("SELECT f1,f2,f3,f4,f5,f6 FROM fees where roll="+roll);
				out.println("Results");
				while (re1.next()) {
					out.println("sem1	 	: "+re1.getString(1));
					out.println("sem2	 	: "+re1.getString(2));
					out.println("sem3	 	: "+re1.getString(3));
					out.println("sem4	 	: "+re1.getString(4));
					out.println("sem5	 	: "+re1.getString(5));
					out.println("sem6	 	: "+re1.getString(6));
				}
				
				
				Connection con2= DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","1234");
				Statement ps2=con2.createStatement();
				ResultSet re2=ps2.executeQuery("SELECT sem1,sem2,sem3,sem4,sem5,sem6 FROM result where roll="+roll);
				out.println("fees");
				while (re2.next()) {
					out.println("sem1	 	: "+re2.getString(1));
					out.println("sem2	 	: "+re2.getString(2));
					out.println("sem3	 	: "+re2.getString(3));
					out.println("sem4	 	: "+re2.getString(4));
					out.println("sem5	 	: "+re2.getString(5));
					out.println("sem6	 	: "+re2.getString(6));
				}
				//printing area ::::::::::::::::::::::::

				
			
				
		}
	
				catch (SQLException e) {
					// TODO: handle exception
					e.printStackTrace();
				}
		catch (ClassNotFoundException e)
		{
			e.printStackTrace();
			// TODO: handle exception
		}
	
		
	}
}

