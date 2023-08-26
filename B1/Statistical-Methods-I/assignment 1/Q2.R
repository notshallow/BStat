#Q2
#Ans
coin1 = sample(2,1000,replace=T,prob=c(0.3,0.7))-1
coin2 = sample(2,1000,replace=T,prob=c(0.6,0.4))-1
temp = rep(0,2000)
odd = seq(1,1999,2)
even = seq(2,2000,2)
temp[odd] = coin1
temp[even] = coin2
ntoss = 1:2000
list = cumsum(temp)
plot(ntoss,list/ntoss,ty='l',ylim=c(0,1))