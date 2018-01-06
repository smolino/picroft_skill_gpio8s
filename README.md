# picroft 8 Switch Relay skill gpio Readme 

This is a skill for picroft that will interact with the GPIO and 8 Swich Relay

## Requirements

This requires a Picroft install on the RPi you can find instructions on the home.mycroft.ai site.
Be sure that mycroft user has the following the group for gpio

### Requires

These are required for doc generation.

 - graphviz
 - sphinx
 - python-rpi.gpio
 - python3-rpi.gpio

### Generation

GPIO Pins used to this project

Project has been made with GPIO Extension Board

Pins connected to the RelaySwitch (27,17,22,05,06,13,19,26)

The documentation is done by sphinx with some of it in the code.  The following will generate the html docs.

```make docs```

You can then find the generated html in ```docs/build/html/index.html```.  Open that file in your browser and you should be able to navigate the docs.

## Installing
First method

msm install https://github.com/smolino/picroft_skill_gpio8s.git

Second method

Once you have a picroft image configure it for SSH access.  Change the Makefile ip address for the RPi you installed the image onto. Also create the folder ```/opt/mycroft/skills/skill-gpio8s``` on the RPi for the installer.

```make install.pi```

This will installl this source onto the RPi.

## Testing

```make test.pi```

This will run a test to be sure you have access to the gpio be sure to test on the system in a simular manner as mycroft.

## Using

Once installed on a paired Picroft you should be able to issue commands:

```
Turn Switch On
Turn Switch Off
Turn Light on
Turn Light Off
Turn Fan On
Turn Fan Off
Turn Living On
Turn Living Off
Turn Bathroom On
Turn Bathroom Off
Turn Kitchen On
Turn Kitchen Off
Turn Lamp On
Turn Lamp Off
Turn Bedroom On
Turn Bedroom Off
```

And Picroft do not respond

Remember to add mycroft user to gpio group:

sudo usermod -g gpio mycroft

## Files

    vocab - This captures entities used by the skill to understand the vocal command.
    dialog - This is used for responces back to the users.

