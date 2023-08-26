#Q-1
#Ans
plot(1:1000,cumsum(sample(2,1000,replace=T,prob=c(0.3,0.7))-1)/1:1000,col='purple',ty='l',ylim=c(0,1))
lines(1:1000,cumsum(sample(2,1000,replace=T,prob=c(0.3,0.7))-1)/1:1000)