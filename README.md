2 Making a simple web server

2.1 Testing with a web browser
How to run:
- Open a terminal and go to the folder with the .py-files
- Run the following the command: python3 simple-webserver.py
  
2.2 Testing with your own web client
How to run:
- Open a terminal and go to the folder with the .py-files
- Run the following command: python3 simple-client.py -i localhost -p 8000 -f index.html
- Output: HTTP/1.1 200 OK

3 Making a multi-threaded web server
How to run:
- Open a terminal and go to the folder with the .py-files
- Run the following command: python3 multi-server.py -i localhost -p 8080
- Open a browser a go to "localhost:8080"

4 Run a simple web server and web client in Mininet
- Transfer the files to Mininet.
- Run the following commands:
h1: sudo python3 simple-client.py -i 10.0.1.2 -p 8000 -f index.html
r2: tcpdump -i r2-eth1 -tttt -u traces.pcap
h2: sudo python3 simple-webserver.py
