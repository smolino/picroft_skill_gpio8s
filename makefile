install:
	mkdir -p /opt/mycroft/skills/skill-gpio
	cp -r * /opt/mycroft/skills/skill-gpio

remove:
	rm -rf /opt/mycroft/skills/skill-gpio
