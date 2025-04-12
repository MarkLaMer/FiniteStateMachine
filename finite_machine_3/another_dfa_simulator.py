def simulate_automaton(fa_description, input_str):
    # Initial state
    current_state = fa_description["start_state"]
    # Process each symbol in the input string
    for symbol in input_str:
        transition_key = (current_state, symbol)
        # If there is no valid transition, reject the input
        if transition_key not in fa_description["transitions"]:
            return False
        # Move to the next state
        current_state = fa_description["transitions"][transition_key]
    # Accept if the final state is in the set of accept states
    return current_state in fa_description["accept_states"]

fa_description = {
    "states": {"q0", "q1", "q2"},
    "alphabet": {"0", "1"},
    "transitions": {
        ("q0", "0"): "q1",
        ("q0", "1"): "q0",
        ("q1", "0"): "q2",
        ("q1", "1"): "q0",
        ("q2", "0"): "q2",
        ("q2", "1"): "q2",
    },
    "start_state": "q0",
    "accept_states": {"q2"},
}

# Input strings
input_strings = ["0", "01", "001", "0001", "111", "10", "000"]

# Testing input strings
for s in input_strings:
    result = simulate_automaton(fa_description, s)
    print(f"Input: {s} -> Accepted: {result}")