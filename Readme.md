## All Sky Camera

### Specifications
    - Base: Raspberry Pi 3 B+ (1 GB RAM)
    - Camera: Raspberry Pi HQ Camera V1.0 2018
    - Lens: Fujinon FE185C046HA-1 (1/2" 1.4mm f/1.4 C-Mount Fish-Eye)

### Description
1. On starting up, the allsky camera will start its web server and start capturing and storing images.

2. Everytime allsky boots up, it will try to connect to the wifi-
    - It has the following wifi credentials saved and will cconnect to one of the following-
        1.  - SSID: ```Lab_ground```
            - password: ```40inch12345```
        2.  - SSID: ```ARIES-WIFI```
            - password: ```Aries@Manora```
        3.  - SSID: ```Aries_Nainital```
            - password: ```campus@aries```

3. The locally hosted server can be accessed over the same network at-
    ```
    http://allskyariespi.local/
    ```

### Connecting to the Raspi
1. You can check the status of the Raspi by-
    ```
    $ ping allskyariespi.local
    ```
2. Connect to the Raspi by-
    ```
    $ ssh pi@allskyariespi.local
3. When prompted for password, enter-
    ```
    password: 12345
    ```
4. You can now access the Raspi terminal.

### When connecting to Raspi through a external display over hdmi
1. Raspi is configured to login as user ```pi``` without prompting for any password.
2. You can access the Raspi setting by-
    ```
    $ sudo raspi-config
    ```
3. You can see all the available wireless networks by-
    ```
    $ sudo nmcli dev wifi
    ```
4. You can connect to any available network by-
    ```
    $ sudo nmcli dev connect SSID password "password".
    ```
