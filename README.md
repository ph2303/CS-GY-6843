# ICMP Pinger Lab

<p>
In this lab, you will gain a better understanding of Internet Control Message Protocol (ICMP). You will learn to 
implement a Ping application using ICMP request and reply messages.
</p>
<p>
Ping is a computer network application used to test whether a particular host is reachable across an IP network. It is 
also used to self-test the network interface card of the computer or as a latency test. It worksby sending ICMP “echo 
reply” packets to the target host and listening for ICMP “echo reply” replies. The "echo reply" is sometimes called a 
pong. Ping measures the round-trip time, records packet loss, and prints a statistical summary of the echo reply packets 
received (the minimum, maximum, and the mean of the round-trip times and in some versions the standard deviation of the 
mean).
</p>
<p>
Your task is to develop your own Ping application in Python. Your application will use ICMP but, in order to keep it 
simple, will not exactly follow the official specification in RFC 1739. Note that you will only need to write the client 
side of the program, as the functionality needed on the server side is built into almost all operating systems.
</p>
<p>
You should complete the Ping application so that it sends ping requests to a specified host separated by approximately 
one second. Each message contains a payload of data that includes a timestamp. After sending each packet, the 
application waits up to one second to receive a reply. If one second goes by without a reply from the server, then the 
client assumes that either the ping packet or the pong packet was lost in the network (or that the server is down).
</p>

<h2>Code</h2>
<p>
Below you will find the skeleton code for the client. You are to complete the skeleton code. The place where you need to 
fill in code is marked with #Fill in start and #Fill in end. In addition, you will need to add a few lines of code in 
order to calculate minimum time, average time, maximum time, and stdev time and print the results like in the operating 
system.
</p>

<h2>Additional Notes</h2>
<ol>
<li>
In the “receiveOnePing” method, you need to receive the structure ICMP_ECHO_REPLY and fetch the information you 
need, such as checksum, sequence number, time to live (TTL), etc. Study the “sendOnePing” method before trying to 
complete the “receiveOnePing” method.
</li>
<li>
You do not need to be concerned about the checksum, as it is already given in the code.
</li>
<li>
This lab requires the use of raw sockets. In some operating systems, you may need administrator/root privileges to be 
able to run your Pinger program.
</li>
<li>
See the end of this programming exercise for more information on ICMP.
</li>
</ol>

<h2>Testing the Pinger</h2>
<p>
First, test your client by sending packets to localhost, that is, 127.0.0.1.
Then, you should see how your Pinger application communicates across the network by pinging servers
in different continents.
</p>

<h2>What to Hand in</h2>
<p>
Use your GitHub repository to upload the complete code for the assignment.
</p>

<h2>Example of a correct output:</h2>
<ul>
<li>
“No.no.e” is a non-valid domain, therefore, the return value (vars) of ping is ['0', '0.0', '0', '0.0']. Please make 
sure you use this exact value.
</li>
<li>
“Google.co.il” is a valid domain, therefore, the return value is a list that can be created in the following way:
</li>
<li>
vars = [str(round(packet_min, 2)), str(round(packet_avg, 2)),str(round(packet_max, 2)), str(round(stdev(stdev_var),2))]
</li>
<li>
The method “ping” must return a Python list with the above values for a valid and a non-valid domain. 
[min,avg,max,stdev]. Return values must be in milliseconds.
</li>
</ul>

<h2>Internet Control Message Protocol (ICMP)</h2>
<h3>ICMP Header</h3>
<p>
The ICMP header starts after bit 160 of the IP header (unless IP options are used).
</p>

<ul>
<li>
Type - ICMP type.
</li>
<li>
Code - Subtype to the given ICMP type.
</li>
<li>
Checksum - Error checking data calculated from the ICMP header + data, with value 0 for this field.
</li>
<li>
ID - An ID value, should be returned in the case of echo reply.
</li>
<li>
Sequence - A sequence value, should be returned in the case of echo reply.
</li>
</ul>

<h2>Echo Request</h2>
<p>
The echo request is an ICMP message whose data is expected to be received back in an echo reply ("pong"). The host must 
respond to all echo requests with an echo reply containing the exact data received in the request message.
</p>
<ul>
<li>
Type must be set to 8.
</li>
<li>
Code must be set to 0.
</li>
<li>
The Identifier and Sequence Number can be used by the client to match the reply with the request that caused the reply
</li>
<li>
In practice, most Linux systems use a unique identifier for every ping process, and sequence number is an increasing 
number within that process. Windows uses a fixed identifier, which varies between Windows versions, and a sequence 
number that is only reset at boot time.
</li>
<li>
The data received by the echo request must be entirely included in the echo reply.
</li>
</ul>


<h2>Echo Reply</h2>
<p>
The echo reply is an ICMP message generated in response to an echo request, and is mandatory for all hosts and routers.
</p>
<ul>
<li>
Type and code must be set to 0.
</li>
<li>
The identifier and sequence number can be used by the client to determine which echo requests are associated with the 
echo replies.
</li>
<li>
The data received in the echo request must be entirely included in the echo reply.
</li>
</ul>




<h2>FAQ</h2>
<p>
Q: I am getting the following error in gradescope: 
“cp: cannot stat '/autograder/submission/solution.py': No such file or directory”
</p>
<p>
A: If you are submitting a python solution, all python submissions must have the filename titled “solution.py” (minus 
the quotation marks). Make sure your file meets this naming requirement.
</p>

<h2>Recommended Textbook Reference</h2>
<p>
Chapter 5: 5.6 ICMP: The Internet Control Message Protocol
</p>

<h2>Most Common issues</h2>
<ul>
<li>
var values are not strings
</li>
<li>
var values are not calculated correctly
</li>
<li>
Recommend to print out your var values and analyze them to see if they actually make sense. If they don’t, revisit your 
method for calculating.
</li>
</ul>
