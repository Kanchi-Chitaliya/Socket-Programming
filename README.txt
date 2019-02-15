Kindly follow the steps given below:
Compatible with python 3.5 
To Run the program:Enter the port number higher than 5000.
Run server.py program and enter the port number as an argument(Say 5001)
This will prompt "The server is ready"
Run client.py program and enter the port address (Say 127.0.0.5) and port number (Say 5001) as arguments. example: client.py 127.0.0.5 5001
This will prompt the options for available commands.
Select a fucntion that is to be performed and enter the command as an argument. Follow the syntax given below:
This will perform the put fuction and prompt the message of successful transfer.
Commands executed and test on various file types:
put: 	To run type:put filename.extension Example:put foo1.txt (Client folder or directory should already contain the file ,here foo1.txt is present in the client directory)
	result:File is transfered from client to server (tested on extensions:.mp3, .txt, .jpg, .png, .pdf) Successful file transfer up to 20MB data without any loss.
		Acknowlegement of packets received after a buffer is also carried out for higher reliability using stop and wait protocol on client and well as server.
list:	To run type:list 
	Result:Provides list of files available in the server folder to the client. It will also acknowledge on successful transfer.

get:	To run type:get filename.extension Example:get foo1.txt (Server folder or directory should already contain the file ,here foo1.txt is present in the server directory)
	result:File is transfered from server to client (tested on extensions: .txt, .jpg, .pdf) Successful file transfer up to 5MB data without any loss.File saved as Received_filename.extension in client
		Acknowlegement of packets received after a buffer is also carried out for higher reliability using stop and wait protocol on client and well as server.
rename:To run type:rename filename1.extension filename2.extension Example:rename foo1.txt foo2.txt (Server folder or directory should already contain the file ,here foo1.txt is present in the server directory)
	Result: This will change the name of the file in the server directory from foo1.txt to foo2.txt
exit:	To run type:exit 
	Result: This will exit the server.