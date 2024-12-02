def simulate_action_execution(actions):
    for action in actions:
        print(f"Executing {action['action']} for Campaign ID {action['campaign_id']}...")
        print(f"Reason: {action['reason']}")
        print("Action completed!")
