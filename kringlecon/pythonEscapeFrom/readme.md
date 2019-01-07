## Python Escape From Shell

For this challenge the docker container initializes into a python REPL. There a numerous ways to perform any escape typically, the simplest is of course to try executing import os or another system challenge

![banner](banner.png)

This does not work though as they have limited us in functionality through a whitelist. Which means we have a couple of options: beat the white list or utilize provided functionality.

Let's see what we have available.

![dir](dir.png)

Well now we know what is restricted.

![restricted](restricted.png)

What is this code module?

![code](code.png)

That sounds extremely useful, why don't we just open up an interactive console then?
```
code.InteractiveConsole.interact()
```

![escaped](escaped.png)

That was simple. Now you can execute commands with OS or spawn a TTY shell with pty. 

![sovled](solved.png)
