import db.DataBase;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class MainServlet extends HttpServlet
{
    public static final String URL = "jdbc:mysql://178.170.189.211:3306/xraydata?autoReconnect=true&useSSL=false&useLegacyDatetimeCode=false&serverTimezone=UTC";
    public static final String USER = "spixe";
    public static final String PASSWORD = "Katya1998";
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        Connection connection = null;
        Driver driver;

        try {
            driver = new com.mysql.cj.jdbc.Driver();
            DriverManager.registerDriver(driver);
        }
        catch (SQLException e1) {
            System.out.println("Драйвер не зарегистрировался");
            return;
        }
        try {
            connection = DriverManager.getConnection(URL, USER, PASSWORD);
            if (!connection.isClosed())
                System.out.println("Соединение установлено");
        }catch (SQLException ex){
            System.err.println("Соединение не установлено");
            ex.printStackTrace(); // Понадобился, чтобы отловить исключения, скрытые выводом на экран предупреждения
            return;
        } finally {
            if (connection != null) connection.close();
        }
    }

    @Override
    protected void finalize() throws Throwable {
        super.finalize();
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Getting from request
        String resptext = req.getParameter("info");

        // Parse request to string array
        String[] strArgs = transformRequest(resptext);

        // Checking input
        /*try {
            // Cast string array to float
            float[] floatArgs = stringArrayToFloat(strArgs);
            resp.getOutputStream().print(floatArgs[0]);
        } catch (NumberFormatException  e) {
            resp.getOutputStream().print("Wrong input");
        }*/
        try {
            resp.getOutputStream().print(DataBase.getInstance().getConnection().getMetaData().getDriverName());
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }


        resp.setStatus(HttpServletResponse.SC_OK);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }

    private float[] stringArrayToFloat(String[] str) {
        List<Float> outArray= new ArrayList<Float>();
        for (String out : str) {
            outArray.add(Float.valueOf(out));
        }
        float[] outFloat = new float[outArray.size()];
        int i = 0;

        for (Float f : outArray) {
            outFloat[i++] = (f != null ? f : Float.NaN); // Or whatever default you want.
        }
        return outFloat;
    }
    private String[] transformRequest(String str) {
        str = str.substring(1, str.length() - 1);
        str = str.replaceAll("\"", "");
        return str.split(",");
    }
}
