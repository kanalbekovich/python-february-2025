import urllib3
import json

slack_url = ""  # Replace with your Slack webhook
http = urllib3.PoolManager()

def get_alarm_attributes(sns_message):
    return {
        'name': sns_message['AlarmName'],
        'description': sns_message['AlarmDescription'],
        'reason': sns_message['NewStateReason'],
        'region': sns_message['Region'],
        'instance_id': sns_message['Trigger']['Dimensions'][0]['value'],
        'state': sns_message['NewStateValue'],
        'previous_state': sns_message['OldStateValue']
    }

def build_slack_message(alarm, status):
    emoji = {
        "register": ":warning:",
        "activate": ":red_circle:",
        "resolve": ":large_green_circle:"
    }[status]

    header = f"{emoji} Alarm: {alarm['name']}"
    if status == "register":
        header += " was registered"
    elif status == "resolve":
        header += " was resolved"

    return {
        "type": "home",
        "blocks": [
            {"type": "header", "text": {"type": "plain_text", "text": header}},
            {"type": "divider"},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"- {alarm['reason']} -"}},
            {"type": "divider"},
            {"type": "context", "elements": [{"type": "mrkdwn", "text": f"*Region:* {alarm['region']}"}]}
        ]
    }

def lambda_handler(event, context):
    sns_message = json.loads(event["Records"][0]["Sns"]["Message"])
    alarm = get_alarm_attributes(sns_message)

    msg = None
    if alarm['previous_state'] == "INSUFFICIENT_DATA" and alarm['state'] == 'OK':
        msg = build_slack_message(alarm, "register")
    elif alarm['previous_state'] == 'OK' and alarm['state'] == 'ALARM':
        msg = build_slack_message(alarm, "activate")
    elif alarm['previous_state'] == 'ALARM' and alarm['state'] == 'OK':
        msg = build_slack_message(alarm, "resolve")

    if msg:
        resp = http.request("POST", slack_url, body=json.dumps(msg).encode('utf-8'))
        print({"message": msg, "status_code": resp.status, "response": resp.data})