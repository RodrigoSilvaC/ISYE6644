# Single server queues 
We will simulate the line that forms in front of a single server at a bakery.
This is our first "real" simulation model involving non-static customers.

Customers arrive at a single-server queue with iid interarrival times and iid service times. Customers must wait in a first in first out (FIFO) line if the server is busy.
**We will estimate:**
* The expected customer waiting time;
* The expected number of people in the system; and
* The server utilization (proportion of busy time)

### Notation
1. **Interarrival time between customers** *i-1* **and** *i* is *I<sub>i*. We will generate this variable randomly.
2. **Customer** *i* **'s arrival time is:**\
 *A<sub>i</sub> = <a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{j=1}^{i}{I_{i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{j=1}^{i}{I_{i}}" title="\sum_{j=1}^{i}{I_{i}}" /></a>*\
 This means that the customer's arrival time is just the sum of all the interarrival time between customers.
3.  **Customer** *i* **is going to start service at time**\
*T<sub>i</sub> = max(A<sub>i</sub>,D<sub>i-1</sub>)*\
The customer is going to start service at time: the maximum between his arrival time or if there is someone ahead of him, the departure time of the previous customer.
4. **Customer** *i* **'s waiting time is**\
*W<sub>i</sub><sup>Q</sup> = T<sub>i</sub> - A<sub>i</sub>\
The customers waiting time is **the difference between the time that he starts service (T<sub>i</sub>) and the customer's arrival time (A<sub>i</sub>).**\
5. **Customer** *i* **'s time in the system is**\
*W<sub>i</sub> = D<sub>i</sub> - A<sub>i</sub>\
The customer's time in the system is equal to **the difference between the time that he/she leaves (D<sub>i</sub>) and the time that he/she arrives (A<sub>i</sub>).** 
6. **Customer** *i* **'s service time is:**\
*S<sub>i</sub>\
This is one of the variables that we will generate randomly.
7. **Customer** *i* **'s departure time is:**\
*D<sub>i</sub> = T<sub>i</sub> + S<sub>i</sub>*\
Example:

|*i*  |I<sub>i</sub>|A<sub>i</sub>|T<sub>i</sub>|W<sub>i</sub><sup>Q</sup>|S<sub>i</sub>|D<sub>i</sub>|
|-----|-------------|-------------|-------------|-------------------------|-------------|-------------|
|1    |3            |3            |3            |0                        |7            |10           |
|2    |1            |4            |10           |6                        |6            |16           |
|3    |2            |6            |16           |10                       |4            |20           |
|4    |4            |10           |20           |10                       |6            |26           |
|5    |5            |15           |26           |11                       |1            |27           |
|6    |5            |20           |27           |7                        |2            |29           |
