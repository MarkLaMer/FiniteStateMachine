def simulate_dfa(dfa_description, input_str):
    # Initial state
    current_state = dfa_description["start_state"]
    # Process each symbol in the input string
    for symbol in input_str:
        transition_key = (current_state, symbol)
        # If there is no valid transition, reject the input
        if transition_key not in dfa_description["transitions"]:
            return False
        # Move to the next state
        current_state = dfa_description["transitions"][transition_key]
        # Reject if the current state is the invalid state
        if current_state == "trap":
            return False
    # Accept if the final state is in the set of accept states
    return current_state in dfa_description["accept_states"]

dfa_description = {
    "states": {"q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "trap", "start"},
    "alphabet": {"a", "b"},
    "transitions": {
        ("start", "a"): "q1", ("start", "b"): "r1",
        ("q1", "a"): "q2", ("q1", "b"): "start",
        ("q2", "a"): "q3", ("q2", "b"): "q1",
        ("q3", "a"): "q4", ("q3", "b"): "q2",
        ("q4", "a"): "q5", ("q4", "b"): "q3",
        ("q5", "a"): "q6", ("q5", "b"): "q4",
        ("q6", "a"): "q7", ("q6", "b"): "q5",
        ("q7", "a"): "q8", ("q7", "b"): "q6",
        ("q8", "a"): "q9", ("q8", "b"): "q7",
        ("q9", "a"): "trap", ("q9", "b"): "q8",
        ("r1", "a"): "start", ("r1", "b"): "r2",
        ("r2", "a"): "r1", ("r2", "b"): "r3",
        ("r3", "a"): "r2", ("r3", "b"): "r4",
        ("r4", "a"): "r3", ("r4", "b"): "r5",
        ("r5", "a"): "r4", ("r5", "b"): "r6",
        ("r6", "a"): "r5", ("r6", "b"): "r7",
        ("r7", "a"): "r6", ("r7", "b"): "r8",
        ("r8", "a"): "r7", ("r8", "b"): "r9",
        ("r9", "a"): "r8", ("r9", "b"): "trap",
        ("trap", "a"): "trap", ("trap", "b"): "trap",
    },
    "start_state": "start",
    "accept_states": {"start", "q1", "q2", "q3", "r1", "r2", "r3"}
}

# Input strings
input_strings = ["aaa", "abab", "aaaabbb", "aaaaaaa", "bbbbbbb", 
                 "aaaaaaabbbbbbbb", "bbbb", "aaaabbbbaaaa", "bbbaaaabbbb", 
                 "aaaaaaaabbbbbbbb", "abababab", "ababababab", "aaabbbbaa", 
                 "abbbaaaa", "bbbaaabbb", "", "a", "b", "aaabbb", "abababababab"]

# Testing input strings
for s in input_strings:
    result = simulate_dfa(dfa_description, s)
    print(f"Input: {s} -> Accepted: {result}")