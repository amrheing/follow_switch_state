# Definitions

#get debug
sensor = data.get("debug", None)

ENTITY_ID = ""
if sensor != None:
	if sensor == True:
		DEBUG = True
	else:
		DEBUG = False
else:
	DEBUG = False

def ld(msg, *args):
	if DEBUG == True:
		logger.info("%s :: %s", ENTITY_ID, msg % args)

logger.info("Start Follow Switch state - DEBUG: %s", DEBUG)

follow_object = data.get("follow_object", None)

entity_ids = data.get("entity_ids", [])

target_state = hass.states.get(follow_object).state

ld("Follow Object: %s", follow_object)
ld("Entty IDs: %s", entity_ids)
ld("Target state: %s", target_state)

for entity in entity_ids:
	type = entity.split(".")[0]
	ld("Type: %s", type)
	sd = []
	sd = {"entity_id": entity}
	if target_state == "off":
		ld("- Set climate to mode: %s - Service Data: %s", target_state, sd)
		logger.info("Switch %s: %s", entity, target_state)
		hass.services.call(type, "turn_off", sd, False)
	else:
		ld("- Set climate to mode: %s - Service Data: %s", target_state, sd)
		logger.info("Switch %s: %s", entity, target_state)
		hass.services.call(type, "turn_on", sd, False)
			