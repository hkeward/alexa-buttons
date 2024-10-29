# Alexa buttons

Press physical buttons hooked up to a Raspberry Pi to trigger Alexa routines without using voice.

## Requirements

- An Amazon account
- An Alexa-enabled device, like an Echo Dot
- The Alexa app
- A Raspberry Pi and charger, ideally with WiFi; an SD card to load the code and OS onto; some buttons and wires

## Setup

### Setting up the triggers and routines

We will set up virtual doorbells that can be triggered via URL; these can be used to run routines.

1. Follow the instructions [here](https://virtualsmarthome.freshdesk.com/support/solutions/articles/202000046256-getting-started-with-url-routine-trigger) to connect your Amazon account and set up a URL Routine Trigger. Name the trigger something distinct. Make note of the JSON response URL.
2. Open the Alexa app. It should automatically detect the new device. It will show up as a doorbell with the name you gave the trigger.
3. Define a Routine in Alexa. See [example routines](#example-routines) for some ideas. The "When" should be Smarthome, then select the name you gave the trigger in step 1.

_This uses the excellent URL Routine Trigger setup provided by [https://www.virtualsmarthome.xyz/](https://www.virtualsmarthome.xyz/); please donate to them if you find this tool useful._

### Setting up the Raspberry Pi

Note that the board is set up in BCM numbering mode.

![BCM board numbering](https://raw.githubusercontent.com/pinout-xyz/Pinout.xyz/master/resources/raspberry-pi-pinout.png)

1. Download [the Raspberry Pi imager](https://www.raspberrypi.com/software/). Follow the instructions to install the appropriate OS for your device. Make sure that you configure the WiFi and add your SSH public key, and optionally set the user. Make a note of the domain name (probably `raspberrypi.local`).
2. Edit [the template config.py file](./src/config.template.py) to add information about each of your buttons. Each different trigger should have its own button config. The config file should be structured as an array of objects with keys `pin_out`, `pin_in`, `trigger_url`:

```json
[
    {
        "pin_out": "The output pin [Int]",
        "pin_in": "The input pin [Int]",
        "trigger_url": "The URL retrieved when setting up the trigger [String]"
    }  
]
```

Any pins can be used as the pin in and pin out, so long as they are GPIO pins.

3. Connect your input and output pins to your buttons, depending on your configuration from step 2.
4. Copy the script and config into the RPi, then ssh in and move them to `/opt/`.

```bash
RPI_USER=

scp -r src/* ${RPI_USER}@raspberrypi.local:~/alexa_buttons
ssh ${RPI_USER}@raspberrypi.local
sudo mv alexa_buttons /opt/
```

5. To enable the script to run on startup, add the following line to `/etc/rc.local`:

```bash
python3 /opt/alexa_buttons/alexa_buttons.py
```

# Example routines

## Call a contact

- **Name**: _Enter a descriptive name_
- **When**: Smarthome -> _Select the name of the trigger_
- **Alexa Will**: Customized -> "Call \<Alexa Contact name>"

If the person you're trying to call is not an Alexa contact, you can write out their full phone number including country code instead of the contact name.
