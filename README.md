<h1>SMTP Email Client</h1>

<p>
By the end of this lab, you will have acquired a better understanding of SMTP 
protocol. You will also gain experience in implementing a standard protocol using
Python.
</p>

<p>
Your task is to develop a simple mail client that sends email to any recipient. 
Your client will need to connect to a mail server, dialogue with the mail server
using the SMTP protocol, and send an email message to the mail server. Python 
provides a module, called smtplib, which has built-in methods to send mail using
SMTP protocol. However, you will not be using this module in this lab, because 
it hides the details of SMTP and socket programming.
</p> 

<p>
In order to limit spam, some mail servers do not accept TCP connections from 
arbitrary sources. For the experiment described below, you may want to try 
connecting both to your university mail server and to a popular Webmail server,
such as an AOL mail server. To connect to the university mail server, you will 
need to use NYU’s VPN. You may also try making your connection both from your 
home and from your university campus.
</p>

<h2>Code</h2>
<p>
Below you will find the skeleton code for the client. You are to complete the 
skeleton code. The places where you need to fill in code are marked with #Fill 
in start and #Fill in end. Each place may require one or more lines of code. 
</p>

<h2>Additional Notes</h2>
<p>
In some cases, the receiving mail server might classify your email as junk. Make
sure that you check your junk/spam folder when you look for the email sent from
your client.
</p>

<h2>What to Hand In</h2>
<p>
Use your GitHub repository to upload the complete code for the SMTP mail client. Make sure you follow the SMTP protocol for non-encrypted communication. In this assignment, GradeScope will use a local SMTP server to grade the assignment. Please make sure to use port 1025 and mail server address 127.0.0.1 to receive full credit.
Note: Comment out all the print statements in your code, otherwise gradescope 
will fail to autograde your assignment.
</p>