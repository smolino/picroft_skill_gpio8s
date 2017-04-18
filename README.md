# gpio_skill
This is a skill for picroft that will interact with the GPIO

## Requirements

This requires a Picroft install on the RPi you can find instructions on the home.mycroft.ai site.
Be sure that mycroft user has the following the group for gpio

## Installing
Once you have a picroft image configure it for SSH access.  Change the Makefile ip address for the RPi you installed the image onto.  

```make install.pi```

This will installl this source onto the RPi.  

## Testing

```make test.pi```

This will run a test to be sure you have access to the gpio be sure to test on the system in a simular manner as mycroft.
