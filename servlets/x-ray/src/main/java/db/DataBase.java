package db;


import java.sql.*;

public class DataBase {

    private Connection connection = null;
    private ResultSet rs = null;

    // Main information: IP DB and schema's name
    static final private String DBAdress = "jdbc:mysql://178.170.189.211:3306/";
    static final private String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";;
    static final private String DBName = "xraydata";

    // Auth data
    static final private String DBLogin = "spixe";
    static final private String DBPass = "Katya1998";


    public Connection getConnection() throws SQLException {
        if(connection == null) throw new SQLException("DB didn't connected");
        return connection;
    }

    private static DataBase instance;

    // Blocked constructor
    private DataBase() throws ClassNotFoundException, SQLException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        connection = DriverManager.getConnection(DBAdress + DBName, DBLogin, DBPass);

    }


    public ResultSet executeQuery(String query) {
        try {
            Statement statement = getConnection().createStatement();
            rs = statement.executeQuery(query);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return rs;
    }

    public void close() throws SQLException {
        getConnection().close();
    }

    // Singleton
    public static synchronized DataBase getInstance() throws SQLException, ClassNotFoundException {
        if (instance == null) {
            instance = new DataBase();
        }
        return instance;
    }



}
