library(ggplot2)
# Suppose U and V are independent Uniform(0,1) random variables
U = runif(1000,0,1)
V = runif(1000,0,1)

# Consider the nasty-looking RV 
Z = sqrt(-2*log(U))*cos(2*pi*V)

# where the cosine calculation is carried out in radians (not degrees).
# NOTE: the cos(x) function in R works with angles in radians

# Go ahead and carry out the calculation 1000 times and make a histogram
p <- ggplot(data.frame(Z), aes(x = Z)) +
  geom_histogram(color = 'darkblue', fill = 'lightblue')
p
