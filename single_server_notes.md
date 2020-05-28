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
 *<a href="https://www.codecogs.com/eqnedit.php?latex={A_{i}}=\sum_{j=1}^{i}{I_{i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{A_{i}}=\sum_{j=1}^{i}{I_{i}}" title="{A_{i}}=\sum_{j=1}^{i}{I_{i}}" /></a>*\
 This means that the customer's arrival time is just the sum of all the interarrival time between customers.
3.  **Customer** *i* **is going to start service at time**\
*T<sub>i</sub> = max(A<sub>i</sub>,D<sub>i-1</sub>)*\
The customer is going to start service at time: the maximum between his arrival time or if there is someone ahead of him, the departure time of the previous customer.
4. **Customer** *i* **'s waiting time is**\
*W<sub>i</sub><sup>Q</sup> = T<sub>i</sub> - A<sub>i</sub>\
The customers waiting time is **the difference between the time that he starts service (T<sub>i</sub>) and the customer's arrival time (A<sub>i</sub>).**
5. **Customer** *i* **'s time in the system is**\
*W<sub>i</sub> = D<sub>i</sub> - A<sub>i</sub>\
The customer's time in the system is equal to **the difference between the time that he/she leaves (D<sub>i</sub>) and the time that he/she arrives (A<sub>i</sub>).** 
6. **Customer** *i* **'s service time is:**\
*S<sub>i</sub>\
This is one of the variables that we will generate randomly.
7. **Customer** *i* **'s departure time is:**\
*D<sub>i</sub> = T<sub>i</sub> + S<sub>i</sub>*\
Example:

**Table 1**

|*i*  |I<sub>i</sub>|A<sub>i</sub>|T<sub>i</sub>|W<sub>i</sub><sup>Q</sup>|S<sub>i</sub>|D<sub>i</sub>|
|-----|-------------|-------------|-------------|-------------------------|-------------|-------------|
|1    |3            |3            |3            |0                        |7            |10           |
|2    |1            |4            |10           |6                        |6            |16           |
|3    |2            |6            |16           |10                       |4            |20           |
|4    |4            |10           |20           |10                       |6            |26           |
|5    |5            |15           |26           |11                       |1            |27           |
|6    |5            |20           |27           |7                        |2            |29           |

From the table we can get easily the **average waiting time for the six customers** by getting a simple average from the 
customer's waiting time (W<sub>i</sub><sup>Q</sup>):

**Table2**

|W<sub>i</sub><sup>Q</sup>|
|-------------------------|
|0                        |
|6                        |
|10                       |
|10                       |
|11                       |
|7                        |

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{i=1}^{6}{W{_{i}^{Q}}/6}&space;=&space;7.33" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{i=1}^{6}{W{_{i}^{Q}}/6}&space;=&space;7.33" title="\sum_{i=1}^{6}{W{_{i}^{Q}}/6} = 7.33" /></a>

**How do we get the average number of people in the system (in line + in service)?**
 
 Note that arrivals and departures are the only possible times for the number of people in the system, *L(t)* to change. 
 These times (and the associated things that happen) are called **events**. This is why the topic is called **Discrete event simulation**.
 
Table 3 below gives a description of the events from Table 1. 

**Table 3**

|*time t*|event                |*L(t)*|
|--------|---------------------|------|
|0       |simulation begins    |0     |
|3       |customer 1 arrives   |1     |   
|4       |2 arrives            |2     |
|6       |3 arrives            |3     |   
|10      |1 departs; 4 arrives |3     |
|15      |5 arrives            |4     |   
|16      |2 departs            |3     |
|20      |3 departs; 6 arrives |3     |   
|26      |4 departs            |2     |
|27      |5 departs            |1     |
|29      |5 departs            |0     |   

Eventually, the system clears at time 29. This table is tedious to do, but every simulation language can do this for you.

Another way of looking at this table is graphically:
 
![Graph 1](C:/Users/Rodrigo Silva/Documents/ISYE6644/virtualenv/.git/Graph1.png)
