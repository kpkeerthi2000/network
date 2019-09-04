import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
public class HTTPServer
 {

    public static void main(String args[] ) throws IOException {

        ServerSocket server = new ServerSocket(5678);
        System.out.println("Listening for connection on port 5678 ....");
        while (true) {
            Socket clientSocket = server.accept();
            InputStreamReader isr =  new InputStreamReader(clientSocket.getInputStream());
            BufferedReader reader = new BufferedReader(isr);
            String line = reader.readLine();            
            while (!line.isEmpty()) {
                System.out.println(line);
                line = reader.readLine();
            }
        }
    }
}

