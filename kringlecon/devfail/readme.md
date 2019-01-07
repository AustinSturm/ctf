## Dev Fail

Their is a folder called kcconfmgmt, the hint tells you the password will be within the commit history.

![banner](banner.png)

Check the git commit history with git log after swapping to the list branch. A commit states they removed the password from the git repo in the server/config file.
![gitlog](gitlog.png)

Checkout the commit right before the one noted and you will find the password
![checkout](gitcheckout.png)

There it is solved.
![solved.png](solved.png)
