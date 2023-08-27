library(MASS)
a = read.csv('~/Code/R programming/assignment 2/data_poisson.csv', head = T)
y = as.numeric(a$y)
y=y[!is.na(y)]
l=fitdistr(y,"Poisson")$estimate[["lambda"]]
print(table(y))
x = 0:max(y)
pmf=280*dpois(x,l)
ob_f= table(y)
table = data.frame('Count of deaths'= x,'Observed relative frequencies' = ob_f, 'Fitted Poisson PMFs' = pmf)
plot(x, ob_f, type = "b", pch = 16, col = "#030569", ylim = c(0, 150), xlab = "Number of Deaths", ylab = "Relative Frequency", main = "Observed vs. Poisson PMF", yaxt='n')
axis(2, yaxp=c(0, 200, 20), las=2)
lines(x, pmf, type = "b", pch = 16, col = "#E3593A")
legend("topright", legend = c("Observed", "Poisson PMF"), col = c("#030569", "#E3593A"), lty = c(1, 1), pch = c(16, 16))