# DDS frontend

This is a frontend for our DDS signal generator. It allows User to change amplitude, shape and frequency of the output waveform.


### Installation

Frontend requires [Python](https://www.python.org/downloads/release/python-370/) v3.7.0 to run.

Install the dependencies and start the application!.

```sh
$ cd DDS_frontend
$ pip install -r requirements.txt
```

Pip will install all necesarry packages.

### Usage

Now, you are able to start the application. To do it, type in console:
```sh
$ cd DDS_frontend
$ python main.py
```

Application will now start.


### Troubleshooting
Keep in mind, that your COM port may be different than mine. So in 37 line of sender.py enter valid COM port number and baudrate of transmission.
