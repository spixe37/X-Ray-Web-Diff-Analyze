import db.DataBase;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class MainServlet extends HttpServlet
{
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        DataBase.getInstance();
    }

    @Override
    protected void finalize() throws Throwable {
        super.finalize();
        DataBase.getInstance().getConnection().close();
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
