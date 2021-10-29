# Development Environment
## Platform
Both windows and Linux are supported. The following console snippets are from an ubuntu terminal

## Python
Install Python and the appropriate libraries
```console
username@hostname:~/projects/cps-project$ cd
username@hostname:~$ apt update
username@hostname:~$ apt upgrade
username@hostname:~$ apt install python3.9 python3.9-venv python3.9-dev
```
Create the virtual environment
```console
username@hostname:~$ mkdir .venv
username@hostname:~$ python3.9 -m venv .venv/cps-project
```
Load the virtual environment
```console
username@hostname:~$ source .venv/cps-project/bin/activate
```
Your console should look as follows
```console
(cps-project) username@hostname:~$
```
Install the project's dependencies
```console
(cps-project) username@hostname:~$ cd projects/cps-project
username@hostname:~/projects/cps-project$ pip install -r requirements.txt
```
## Webots
Install Webots from [here](https://cyberbotics.com/)

Set `WEBOTS_HOME` to the installed path of Webots
### Configuring for PyCharm
Though this is intended for PyCharm, it should still be as applicable to other Python IDEs.
For more detailed instructions, visit [Cyberbotic's page on PyCharm configuration for Webots](https://cyberbotics.com/doc/guide/using-your-ide?tab-os=windows#pycharm)

Press `Ctrl+Alt+S` and search for `Project Structure` and click `Add Content Root` button.
Select and add the `WEBOTS_HOME/lib/controller/python<ver>` folder.

Edit your environmental tables for running your script. See Cybernotic's page above for instructions for your OS.
