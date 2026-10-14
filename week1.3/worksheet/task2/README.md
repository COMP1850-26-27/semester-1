# Task 2 – PORTFOLIO – Traffic light simulation

A road crossing is controlled by a traffic light. A red light means traffic must stop; a green light means traffic may go. The traffic light shows red and amber when it is about to change to green, and amber when it is about to change to red.
The traffic light passes through a repeating set of states, with a fixed duration, as defined by the dictionary below:

    states = {"red":4, "red_amber":3, "green":5, "amber":3}

The `traffic_light.py` code provides a skeleton for the simulation of the traffic light system for 40 time units.

There is one input to the code – the number of steps required (>0).

You should complete the code so that at each step the state of the system is printed to screen. For your submission that should be the only output – as shown in the first print statement.  

For example the output after the first 7 steps should be: 

    Time 000 State red
    Time 001 State red
    Time 002 State red
    Time 003 State red
    Time 004 State red_amber
    Time 005 State red_amber
    Time 006 State red_amber
    Time 007 State green

You will need to use a combination of iteration and logical control of the state. 
Submitting to Gradescope will test the state transitions through the defined states.
