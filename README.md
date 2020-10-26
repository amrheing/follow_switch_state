<a href="https://github.com/amrheing/follow_switch_state/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/amrheing/follow_switch_state"></a>
<a href="https://github.com/amrheing/follow_switch_state/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/amrheing/follow_switch_state"></a>
<a href="https://github.com/amrheing/follow_switch_state/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/amrheing/follow_switch_state"></a>

This python_script is for use in HomeAssistant

## Features
# follow_switch_state

mirror state of one entity to many others.

i create a helper object: "input_boolean.esszimmer_strahler_switch"
This object i can set with a physical switch (in my case an Aquara Wireless Remote Switch) or by app.

the list of entitys followas the state of this object.

tested with "light" and "switch" entitys.

```Yaml
- id: 'esszimmer_strahler_on_off'
  alias: Esszimmer Strahler On Off
  description: ''
  trigger:
  - entity_id: input_boolean.esszimmer_strahler_switch
    platform: state
  condition: []
  action:
  - data_template:
      debug: False
      follow_object: input_boolean.esszimmer_strahler_switch
      entity_ids:
      - light.esszimmer_strahler_1
      - light.esszimmer_strahler_2
      - switch.strahler_esszimmer
    service: python_script.follow_switch_state
``
