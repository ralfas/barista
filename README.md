# barista

sudo pip install -r requirements.txt

python server.py


# Full screen web browser

## Hide Window Decorations

vi /home/pi/.config/openbox/lxde-pi-rc.xml

In the applications block, add the following:
```
        <application name="epiphany-browser">
        <decor>no</decor>
        <focus>yes</focus>
        <fullscreen>yes</fullscreen>
        <maximized>true</maximized>
        </application>
```

## Autostart
sudo vi /home/pi/.config/lxsession/LXDE-pi/autostart
OR
sudo vi /etc/xdg/lxsession/LXDE-pi/autostart

```
# Disable the taskbar
#@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
# Disable the Xscreensaver
#@xscreensaver -no-splash
# Don't move the cursor to the Launch button
#@point-rpi
# Disable screensaver
@xset s off
# Disable blank-screensaver
@xset s noblank
# Disable DPMS (Energy Star) features
@xset -dpms
# Start Barista
@/home/pi/workspace/barista/run.sh
# Start Epiphany in kiosk mode
@epiphany-browser -a --profile /home/pi/.config http://127.0.0.1:8080/configure
```