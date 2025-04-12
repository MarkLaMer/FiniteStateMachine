Simulating Finite Automaton
--------------------------------  

**Overview**
This program simulates a finite automaton (FA) and determines whether a given input string is accepted based on a predefined set of states, transitions, and acceptance criteria.

**Features**
- Defines a finite automaton using states, an alphabet, transitions, a start state, and accept states.
- Processes input strings symbol by symbol to determine if they are accepted by the automaton.
- Prints whether each input string is accepted or rejected.

**Purpose**  
Simulate a DFA that checks if an input string's absolute difference of `a`s and `b`s is less than or equal to 3. The automaton transitions to an invalid state if the balance exceeds ±8, resulting in rejection, as specified in the clarification.  

**Automaton Structure**
- `states`: Set of all states (e.g., `q0` for 0, `q1` for +1, `q-1` for -1) up to `q8`/`q-8`, including `q_invalid`.  
- `alphabet`: Valid input symbols `{"a", "b"}`.  
- `transitions`: Dictionary mapping `(current_state, symbol)` to `next_state`.
  - `a` increments the balance (e.g., `q0 → q1`).  
  - `b` decrements the balance (e.g., `q0 → q-1`).  
  - Beyond ±8 transition to `q_invalid` (a trap state).  
- `start_state`: Initial state (e.g., `"q0"`). 
- `accept_states`: Set of accept states `{e.g., "q0", "q1", "q2", "q3", "q-1", "q-2", "q-3"}`.  