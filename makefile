all: install.pi

install:
	mkdir -p /opt/mycroft/skills/skill-gpio
	cp -r * /opt/mycroft/skills/skill-gpio

remove:
	rm -rf /opt/mycroft/skills/skill-gpio

install.pi:
	scp -r * pi@10.0.0.12:/opt/mycroft/skills/skill-gpio

test.pi:
	ssh pi@10.0.0.12 python /opt/mycroft/skills/skill-gpio/GPIO.py
