# Rage
Rage is a tool to find minecraft servers without a whitelist to grief them.

Setup
--------

Installing Node & npm
  Ubuntu, Debain:
  ```
  $ sudo apt update
  $ sudo apt install nodejs
  $ sudo apt install npm
  ```

  Arch:
  ```
  $ sudo pacman -S nodejs
  $ sudo pacman -S npm
  ```

  CentOS, Fedora:
  ```
  $ dnf module install nodejs:17
  ```

Installing Rage:
  ```
  $ cd ~/Desktop
  $ git clone https://github.com/MatrixBytes/Rage.git
  $ cd Rage
  $ npm install mineflayer
  $ pip install mcstatus
  ```

If you want to check for Whitelist:
  Open bot.js in the Rage folder and enter your Minecraft account info.\
  lines: 6,7,8

  Open main.py and set checkwhitelist to True\
  line: 8

Running
--------
It's simple. just execute the main.py:
```
python3 main.py
```

Specific file to Scan?
```
python3 main.py FILE
```
