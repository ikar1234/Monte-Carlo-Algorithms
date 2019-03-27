if (!require(numbers)) {
  stop('The package foo was not installed')
}

pi_est <- function(n) {
  # simulating n dice rolls
  x <- sample(1:120,size=n,replace=T)
  y <- sample(1:120,size=n,replace=T)
  
  # coprime works only with vectors of length 1
  m <- mapply(coprime,x,y)
  # proprtion of coprimes between all pairs of integers
  prop <- length(m[m==T])

  sqrt(6*n/prop)
}
