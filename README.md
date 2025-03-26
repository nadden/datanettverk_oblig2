2 Making a simple web server

2.1 Testing with a web browser
How to run:
- Open a terminal and go to the folder with the .py-files
- Run the following the command: python3 simple-webserver.py
- Open a web browser and type in your IP, portnumber, and index.html
    - For example: 192.483.0.22:8000/index.html
    - To test for error message: Use something different than "index", for example "index1.html". 
  
2.2 Testing with your own web client
How to run:
- Open a terminal and go to the folder with the .py-files
- Run the following command to run the server: python3 simple-webserver.py
- Run the following command to run the client: python3 simple-client.py -i localhost -p 8000 -f index.html
- Output (client): HTTP/1.1 200 OK

3 Making a multi-threaded web server
How to run:
- Open a terminal and go to the folder with the .py-files
- Run the following command: python3 multi-server.py -i localhost -p 8080
- Open a browser a go to "localhost:8080"

4 Run a simple web server and web client in Mininet
- Transfer the files to Mininet.
    - I started an HTTP server for the files in the folder. Open a terminal and redirect to the folder containing the files.
    - Run the following command to start a HTTP server: python -m http.server 8000 (this will start a server on port 8000)
    - Use the command "wget" to downlaod the files to Mininet. For example, "wget http://*Your IP-address*:8000/*file-name.py* 
- Run the following commands after the files are transferd to Mininet:
    - sudo mn
    - xterm h1 h2 rn
- Run the following commands on h1, h2, and r2
    - h1: sudo python3 simple-client.py -i 10.0.1.2 -p 8000 -f index.html
    - r2: tcpdump -i r2-eth1 -tttt -u traces.pcap
    - h2: sudo python3 simple-webserver.py
