# mycroft-cl
A new mycroft command line interface, that is ment to be decoupled from any one particular mycroft instance.

Dependencies:
pip install websocket
[a Mycroft instace](https://github.com/MycroftAI/mycroft-core)

Getting started useing this tool:
```git clone https://github.com/FruityWelsh/mycroft-cl.git```
```cd mycroft-cl```
if you are running this for a local mycroft instance then you 
can run it with no added steps for example:
```./mycroft_cl.py speak hello``` 

Otherwise you can change the IP target address and port by change the ```MYCROFT_ADDR``` and ```MYCROFT_PORT``` env vars.
This can be done prior to use like:
```export MYCROFT_ADDR='localhost'```
```export MYCROFT_PORT='8181'``` 

or by adding these lines (but with your new values) to your ```${HOME}/.profile``` config file.


Setup for development:
I currently use poetry for depency managment.
I also use black and mypy for code linting and include pre-commit hooks for them. 

