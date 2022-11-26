<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Student details</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
	<link rel="stylesheet" type="text/css" href="css/tableeffect.css">
<!--===============================================================================================-->
</head>
<body>
<%
try{
int a;

String email2=" ",pass=" ";

 email2= request.getParameter("email");
 pass= request.getParameter("pass");


int n=email2.lastIndexOf('/');
String email,roll;
if(n==-1)
{
	pass="kol";
	n=0;
	response.sendRedirect("invalid.html");
	//out.print("invalid username type");
}
email=email2.substring(0, n);



roll=email2.substring(n+1);

String var="";

try {
	Class.forName("com.mysql.cj.jdbc.Driver");
		Connection con0= DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","1234");
		Statement ps0=con0.createStatement();
		ResultSet re0=ps0.executeQuery("SELECT contact from student where roll=\""+roll+"\" AND email=\""+email+"\" ");
		re0.next();
		var=re0.getString(1);
		System.out.print(var+" "+pass);
		if(var.equals(pass))
		{
			System.out.println("ok");
			
			




//String emp="";
//if((email.equals(emp)||(roll.equals(emp))))
//{
//	out.print("invalid user input type");
	
//}
//else{
try {
	Class.forName("com.mysql.cj.jdbc.Driver");
		Connection con= DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","1234");
		Statement ps=con.createStatement();
		ResultSet re=ps.executeQuery("SELECT * from student where email=\""+email+"\" AND contact=\""+pass+"\" ");
		
		out.print("<div>");
		
		out.print("<table>");
		out.print("<h2>Student details</h2>");
	while (re.next()) {
			out.println("<tr><th>Roll No 	:</th><td> "+re.getInt(1));out.print("</td></tr>");
			out.println("<tr><th>Name	 	:</th><td> "+re.getString(2));out.print("</td></tr>");
			out.println("<tr><th>Email	 	:</th><td> "+re.getString(3));out.print("</td></tr>");
			out.println("<tr><th>Course 	:</th><td> "+re.getString(5)+" ("+re.getString(4)+") ");out.print("</td></tr>");
			out.println("<tr><th>Gender	 	:</th><td> "+re.getString(6));out.print("</td></tr>");
			out.println("<tr><th>Phno.	 	:</th><td> "+re.getString(7));out.print("</td></tr>");
			out.println("<tr><th>DOB	 	:</th><td> "+re.getString(8));out.print("</td></tr>");
			out.println("<tr><th>Address 	:</th><td> "+re.getString(9));out.print("</td></tr>");
			}
		
		out.print("</table>");
		//out.print("</div>");
		
		Connection con1= DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","1234");
		Statement ps1=con1.createStatement();
		ResultSet re1=ps1.executeQuery("SELECT f1,f2,f3,f4,f5,f6 FROM fees where roll="+roll);
		//out.print("<div>");
		out.print("<table>");
		out.print("<h2>Fees</h2>");;
		out.print("<tr>");
		out.print("<th>Sem 1</th>");
		out.print("<th>Sem 2</th>");
		out.print("<th>Sem 3</th>");
		out.print("<th>Sem 4</th>");
		out.print("<th>Sem 5</th>");
		out.print("<th>Sem 6</th>");
		out.print("</tr>");
		out.print("<tr>");
		while (re1.next()) {
			out.println("<td>"+re1.getString(1));out.print("</td>");
			out.println("<td>"+re1.getString(2));out.print("</td>");
			out.println("<td>"+re1.getString(3));out.print("</td>");
			out.println("<td>"+re1.getString(4));out.print("</td>");
			out.println("<td>"+re1.getString(5));out.print("</td>");
			out.println("<td>"+re1.getString(6));out.print("</td>");
		}
		out.print("</tr></table>");
		//out.print("</div>");
		Connection con2= DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","1234");
		Statement ps2=con2.createStatement();
		ResultSet re2=ps2.executeQuery("SELECT sem1,sem2,sem3,sem4,sem5,sem6 FROM result where roll="+roll);
		//out.print("<div>");
		out.print("<table>");
		out.print("<h2>Results</h2>");
		out.print("<tr>");
		out.print("<th>Sem 1</th>");
		out.print("<th>Sem 2</th>");
		out.print("<th>Sem 3</th>");
		out.print("<th>Sem 4</th>");
		out.print("<th>Sem 5</th>");
		out.print("<th>Sem 6</th>");
		out.print("</tr>");
		out.print("<tr>");
		while (re2.next()) {
			out.println("<td>"+re2.getString(1));out.print("</td>");
			out.println("<td>"+re2.getString(2));out.print("</td>");
			out.println("<td>"+re2.getString(3));out.print("</td>");
			out.println("<td>"+re2.getString(4));out.print("</td>");
			out.println("<td>"+re2.getString(5));out.print("</td>");
			out.println("<td>"+re2.getString(6));out.print("</td>");
		}
		out.print("</tr></table>");
		out.print("</div>");
		
	
		
}
		catch (SQLException e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		

}
else
{
	response.sendRedirect("invalid.html");
	//out.print("invalid useer");
}
}
catch (SQLException e) {
	// TODO: handle exception
	e.printStackTrace();
}
}
catch(NullPointerException e){
	
	response.sendRedirect("login.html");

}
%>
</body>
</html>