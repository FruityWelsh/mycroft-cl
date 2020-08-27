# mycroft-cl
A new mycroft command line interface, that is ment to be decoupled from any one particular mycroft instance.

The goals are:

1. Accomplish most of the features found in mycroft/bin in one utility
2. Be able to use it on remote mycroft instances
3. Keep as much of the utility to work with posix shell features for easy scripting
4. Give easier access to the message bus features for outside programs (with a blender plugin and skill being one of those things). As this can be used as an funtional python api as well as in the command line.

This is very much still a work in progress, but I am excited to keep making progress on it.

Dependencies:

pip install websocket

[a running Mycroft instace](https://github.com/MycroftAI/mycroft-core)

Getting started useing this tool:
```
git clone https://github.com/FruityWelsh/mycroft-cl.git
cd mycroft-cl
```

if you are running this for a local mycroft instance then you can run it with no added steps for example:
```./mycroft_cl.py speak hello``` 

Otherwise you can change the IP target address and port by change the ```MYCROFT_ADDR``` and ```MYCROFT_PORT``` env vars.
This can be done prior to use like:
```
export MYCROFT_ADDR='localhost'
export MYCROFT_PORT='8181'
``` 

or by adding those lines (but with your new values) to your ```${HOME}/.profile``` config file.

ENV VARS:
MYCROFTCL_LOGGING ## if unset = 'WARN', other options include 'DEBUG|INFO|WARN|ERROR' 
MYCROFT_ADDR      ## if unset = "localhost", can be any valid address of a mycroft instance
MYCROFT_PORT      ## if unset = "8181", can be any valid port to a mycroft instance
MYCROFT_JSON_DIR  ## if unset = {local_file_path}/mycroft-json-messages, can be any valid directory
LANG              ## if unset = "en-us"

Setup for development:

I currently use poetry for dependency managment.

I also use black and mypy for code linting and include pre-commit hooks for them. 

### Commands tested  
- [x] speak
- [x] say-to
- [x] stop
- [x] increase-volume
- [x] decrease-volume
