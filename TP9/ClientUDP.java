import java.io.*;
import java.net.*;

public class main {

InetAdrress addr = InetAddress.getLocalHost();
System.out.print1n( "addresse=" +addr.getHostName() );

DatagramPacket packet = new DatagramPacket( data, data.length, addr, 1234 );
DatagramSocket sock = new DatagramSocket();
sock.send(packet);
sock.close();
