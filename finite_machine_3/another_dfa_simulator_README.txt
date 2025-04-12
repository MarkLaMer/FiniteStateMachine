Simulating Finite Automaton
--------------------------------  

**Overview**
This program simulates a finite automaton (FA) and determines whether a given input string is accepted based on a predefined set of states, transitions, and acceptance criteria.

**Features**
- Defines a finite automaton using states, an alphabet, transitions, a start state, and accept states.
- Processes input strings symbol by symbol to determine if they are accepted by the automaton.
- Prints whether each input string is accepted or rejected.

**Purpose**  
Simulate a finite automaton (5-tuple) to determine if input strings are accepted. Ensures:  
- Transitions follow the defined rules.  
- Strings are accepted if the automaton ends in an accepted state.  

**Automaton Structure**
- `states`: Set of all states (e.g., `{"q0", "q1", "q2"}`).  
- `alphabet`: Valid input symbols (e.g., `{"0", "1"}`).  
- `transitions`: Dictionary mapping `(current_state, symbol)` to `next_state`.  
- `start_state`: Initial state (e.g., `"q0"`).  
- `accept_states`: Set of accept states (e.g., `{"q2"}`).