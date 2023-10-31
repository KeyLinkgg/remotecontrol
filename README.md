# Remote Control
## First semi working version of KeyLink, built in around an hour

This was the first test of the KeyLink idea. For fast communication [websockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) are used. Specifically a web interface used to send inputs and a python file used to receive inputs are served by an ExpressJS / SocketIO server. Both the web interface and python client connect to the server which forwards keyinputs from the web interface to the python client. This results in very low latency dependent on geographic location.

### Newer Versions of KeyLink are not currently source available.