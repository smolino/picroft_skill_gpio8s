all: install.pi


#Local Install for testing on desktop or laptop
install:
	mkdir -p /opt/mycroft/skills/skill-gpio
	cp -r * /opt/mycroft/skills/skill-gpio

#For removing the local install
remove:
	rm -rf /opt/mycroft/skills/skill-gpio

#For remote install to a Picroft image on a RPi
install.pi:
	scp -r * pi@10.0.0.12:/opt/mycroft/skills/skill-gpio

#For testing the install on the RPi
test.pi:
	ssh pi@10.0.0.12 python /opt/mycroft/skills/skill-gpio/GPIO.py
