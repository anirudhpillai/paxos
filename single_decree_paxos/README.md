# Single Decree Paxos Python Implementation
This folder contains the Python implementation of the Single Decree Paxos
consensus algorithm. The details about the working of the algorithm can
be found in the [Wiki](https://github.com/anirudhpillai/paxos/wiki/Single-Decree-Paxos).

## Requirements
- Python 3

To run the implementation just run the `paxos.py`.

## Implementation Details
This is a simulation of the single decress paxos algorithm. To simulate
asynchronicity, each message sent from a processor is simulated using a new
thread and the thread is made to sleep for a random amount of time.

Also, the simulation only uses one learner right now.
