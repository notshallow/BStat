#Q3
#Ans
library(tuneR)
h1 = hist(readWave('~/Code/R programming/assignment 0/Q3-silent.wav')@left,prob=T)
h2 = hist(readWave('~/Code/R programming/assignment 0/Q3-loud.wav')@left,prob=T)
plot(h1, col=rgb(0,0,1,1/4), xlim=c(-40000,40000))
plot(h2, col=rgb(1,0,0,1/4), xlim=c(-40000,40000), add = T)