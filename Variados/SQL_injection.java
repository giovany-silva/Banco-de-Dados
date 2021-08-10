
import java.sql.*;

public class Main{
	public static void main(String[] args) throws Exception{

	String name="Joao";
	Main.addUser(name);
	}
	private static void addUser (String name)throws Exception{
	Connection c=null;
	PreparedStatement s=null;

	try{
	c=connectPostgres();
	String sql="insert into northwind.usuario(name) values('"+name+"')";
       //insert into northwind.usuario(name) values('Joao')
        s=c.prepareStatement(sql);

	s.executeUpdate();
	System.out.println("Done!");

	}finally {

	try { if(s!=null)s.close();}catch(Exception e){}
	try { if(c!=null)s.close();}catch(Exception e){}
	}


 	}

 

}