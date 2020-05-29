# (s,S) Inventory System

## Description of our problem
* Let´s suppose that a store sells a product at *$d* dollars per unit.
* Our inventory policy is to have at least *s* units in stock at the start of each day.
* If the stock slips to less than *s* by the end of the day, we place an order with our supplier to
push the stock back up to *S* by the beginning of the next day.
* We have various costs

## Notation
Let *I<sub>i</sub>* denote the inventory at the end of day *i*, and let *Z<sub>i</sub>* denote the
order that we place at the end of day *i*.

<a href="https://www.codecogs.com/eqnedit.php?latex=Z_{i}&space;=&space;\left\{\begin{matrix}&space;S&space;-&space;I_{i}&space;\&space;,&space;if&space;\&space;I_{i}&space;<&space;s\\&space;0\&space;otherwise&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_{i}&space;=&space;\left\{\begin{matrix}&space;S&space;-&space;I_{i}&space;\&space;,&space;if&space;\&space;I_{i}&space;<&space;s\\&space;0\&space;otherwise&space;\end{matrix}\right." title="Z_{i} = \left\{\begin{matrix} S - I_{i} \ , if \ I_{i} < s\\ 0\ otherwise \end{matrix}\right." /></a>

If an order is placed to the supplier at the end of day *i*, it costs the store:

<a href="https://www.codecogs.com/eqnedit.php?latex=K&plus;cZ_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K&plus;cZ_{i}" title="K+cZ_{i}" /></a>

Where *K* is the cost the store incurs only for calling their supplier (sort of like a fixed cost for
supplying). In addition, you have to pay a unit cost of *cZ<sub>i</sub>*. Moreover, it costs *$h/unit* for the store to hold unsold inventory overnight, and a penalty cost of *$p/unit*
if demand can´t be met. No backlogs are allowed. Demand on the day *i* is *D<sub>i</sub>*. Note that
*D<sub>i</sub>* is the only random variable in the model.

## Model
<a href="https://www.codecogs.com/eqnedit.php?latex=Total&space;=&space;Sales&space;-&space;Ordering&space;Cost&space;-&space;Holding&space;Cost&space;-&space;Penalty&space;Cost" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Total&space;=&space;Sales&space;-&space;Ordering&space;Cost&space;-&space;Holding&space;Cost&space;-&space;Penalty&space;Cost" title="Total = Sales - Ordering Cost - Holding Cost - Penalty Cost" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex==&space;d&space;min(D_{i},&space;inventory\&space;at&space;\&space;beginning&space;\&space;of&space;\&space;day&space;\&space;i)\&space;-&space;\begin{Bmatrix}&space;K&space;&plus;&space;cZ_{i}&space;\&space;,&space;if&space;I_{i}<s\\&space;0&space;\&space;otherwise&space;\end{Bmatrix}&space;\&space;-hI_{i}-pmax(0,D_{i}-\&space;inventory\&space;at\&space;beginning\&space;of\&space;day\&space;i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=&space;d&space;min(D_{i},&space;inventory\&space;at&space;\&space;beginning&space;\&space;of&space;\&space;day&space;\&space;i)\&space;-&space;\begin{Bmatrix}&space;K&space;&plus;&space;cZ_{i}&space;\&space;,&space;if&space;I_{i}<s\\&space;0&space;\&space;otherwise&space;\end{Bmatrix}&space;\&space;-hI_{i}-pmax(0,D_{i}-\&space;inventory\&space;at\&space;beginning\&space;of\&space;day\&space;i)" title="= d min(D_{i}, inventory\ at \ beginning \ of \ day \ i)\ - \begin{Bmatrix} K + cZ_{i} \ , if I_{i}<s\\ 0 \ otherwise \end{Bmatrix} \ -hI_{i}-pmax(0,D_{i}-\ inventory\ at\ beginning\ of\ day\ i)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex==&space;d&space;min(D_{i},&space;I_{i-1},Z_{i-1})\&space;-&space;\begin{Bmatrix}&space;K&space;&plus;&space;cZ_{i}&space;\&space;,&space;if&space;I_{i}<s\\&space;0&space;\&space;otherwise&space;\end{Bmatrix}&space;\&space;-hI_{i}-pmax(0,D_{i}-(I_{i-1}&plus;Z_{i-1}))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=&space;d&space;min(D_{i},&space;I_{i-1},Z_{i-1})\&space;-&space;\begin{Bmatrix}&space;K&space;&plus;&space;cZ_{i}&space;\&space;,&space;if&space;I_{i}<s\\&space;0&space;\&space;otherwise&space;\end{Bmatrix}&space;\&space;-hI_{i}-pmax(0,D_{i}-(I_{i-1}&plus;Z_{i-1}))" title="= d min(D_{i}, I_{i-1},Z_{i-1})\ - \begin{Bmatrix} K + cZ_{i} \ , if I_{i}<s\\ 0 \ otherwise \end{Bmatrix} \ -hI_{i}-pmax(0,D_{i}-(I_{i-1}+Z_{i-1}))" /></a>

## Example
Suppose:

|variable|value|
|--------|-----|
|*d*     |10   |
|*s*     |3    |
|*S*     |10   |
|*K*     |2    |
|*c*     |4    |
|*p*     |2    |

Consider the following sequence of demands:

|Demand         |value|
|---------------|-----|
|*D<sub>1</sub>*|10   |
|*D<sub>2</sub>*|3    |
|*D<sub>3</sub>*|10   |
|*D<sub>4</sub>*|2    |
|*D<sub>5</sub>*|4    |
|*D<sub>6</sub>*|2    |

In addition, suppose that we start out with an initial stock of *I<sub>0</sub> + Z<sub>0</sub> = 10*.

![Example](sS_model_example1.png)





