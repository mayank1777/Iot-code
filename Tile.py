class SmartLight:
    def __init__(self, status='off', brightness=0):
        self.status = status
        self.brightness = brightness

    def turn_on(self):
        self.status = 'on'
        print("Light turned on.")

    def turn_off(self):
        self.status = 'off'
        print("Light turned off.")

    def set_brightness(self, level):
        self.brightness = level
        print(f"Brightness set to {level}%.")

class SmartThermostat:
    def __init__(self, temperature=72):
        self.temperature = temperature

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"Temperature set to {temp}°F.")

class SmartDoorLock:
    def __init__(self, is_locked=True):
        self.is_locked = is_locked

    def lock(self):
        self.is_locked = True
        print("Door locked.")

    def unlock(self):
        self.is_locked = False
        print("Door unlocked.")



# DEFINE INTENT toTILE:
#     FROM device ('device_name' | 'device_group') # intend could be for a particular device or for a group of devces
#     PERFORM action ('action_name') # set the temperature between 20 to 25 in all rooms 
#     WITH parameters ('param1', 'param2', ...) 
#     IF condition ('state' | 'external_input') # actions can be conditional like if motion detected in cameras then record
#     AT time ('scheduled_time')
#     REPEAT frequency ('occurrence') # Actions can be scheduled for specific times and set to repeat at defined intervals or under specific conditions.
#     UNTIL condition ('end_condition')


# # FOR INTENT LIKE : " when motion is detected, start recording through camera "s
# DEFINE INTENT toTILE:
#     FROM device ('SecurityCamera')
#     PERFORM action ('record')
#     WITH parameters (None)
#     IF condition ('motion_detected')
#     REPEAT frequency ('24*60*60/DAY')
#     UNTIL condition (True)


class LLMS:
    def __init__(self):
        self.device_groups = {
            'all lights': 'SmartLight'
        }
        self.actions = {
            'turn on': 'turn_on'
        }
        self.timings = {
            'sunset': '18:00',  # assuming sunset at 6 PM for simplification
            'daily': 'daily'
        }

    def parse_intent(self, intent):
        words = intent.split()
        device = None
        action = None
        time = None
        frequency = None

        # Identify device or group
        if 'all lights' in intent:
            device = self.device_groups['all lights']

        # Identify action
        if 'turn on' in intent:
            action = self.actions['turn on']

        # Identify timing and frequency
        if 'sunset' in intent:
            time = self.timings['sunset']
        if 'daily' in intent:
            frequency = self.timings['daily']

        return self.format_tile(device, action, time, frequency)

    def format_tile(self, device, action, time, frequency):
        tile_intent = f"""
DEFINE INTENT EveningLightOn:
    FROM device ('{device}')
    PERFORM action ('{action}')
    AT time ('{time}')
    REPEAT frequency ('{frequency}')
"""
        return tile_intent

# Example Usage
llms = LLMS()
high_level_intent = "Turn on all lights at sunset daily"
tile_command = llms.parse_intent(high_level_intent)
print(tile_command)




# DEFINE INTENT AdvancedDeviceControl:
#     FROM device ('device_name' | 'device_group')
#     PERFORM action ('action_name')
#     WITH parameters ('param1', 'param2', ...)
#     IF condition ('state' | 'external_input')
#     ELSE PERFORM action ('alternative_action')
#     FOLLOWED BY action ('subsequent_action')
#     USING dynamic parameters ('${expression}')
#     AT time ('scheduled_time')
#     REPEAT frequency ('occurrence')
#     UNTIL condition ('end_condition')
#     ON ERROR PERFORM action ('error_handling_action')
#     WITH SECURITY ('role_based_access')


# DEFINE INTENT SmartSecurityMonitoring:
#     FROM device ('SecurityCamera')
#     PERFORM action ('record')
#     WITH parameters (None)
#     IF condition ('motion_detected')
#     ELSE PERFORM action ('send_alert')
#     FOLLOWED BY action ('store_video')
#     USING dynamic parameters ('${video_length_variable}')
#     AT time ('immediately')
#     REPEAT frequency ('24*60*60/DAY')
#     UNTIL condition ('system_disabled')
#     ON ERROR PERFORM action ('log_error')
#     WITH SECURITY ('admin')


# DEFINE INTENT EveningLightOn:
#     FROM device ('SmartLight')
#     PERFORM action ('turn_on')
#     AT time ('18:00')
#     REPEAT frequency ('daily')

# DEFINE INTENT TemperatureAdjustIfAway:
#     FROM device ('SmartThermostat')
#     PERFORM action ('set_temperature')
#     WITH parameters ('60')  # Lower temperature
#     IF condition ('user_status_away')

# DEFINE INTENT VacationMode:
#     FROM device ('SmartHomeSystem')
#     PERFORM action ('set_mode')
#     WITH parameters ('vacation')
#     UNTIL condition ('user_returns')

# DEFINE INTENT SecurityCheck:
#     FROM device ('SecurityCamera')
#     PERFORM action ('record')
#     IF condition ('motion_detected')
#     REPEAT frequency ('as_occurs')

# DEFINE INTENT MultiDeviceRoutine:
#     FROM device ('device_group')
#     PERFORM action ('turn_off')
#     AT time ('22:00')
#     REPEAT frequency ('weekly')