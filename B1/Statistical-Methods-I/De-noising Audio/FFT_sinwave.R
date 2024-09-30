#Loading necessary libraries
library(tuneR)

#Constructing a clean wave by combining 3 sine waves with different
#parameters including frequencies.

samp_rate = 44100 #Sampling rate
time = 10*samp_rate
clean_wave = sine(29, duration = time, from = 0.69, bit = 32) +
             sine(17, duration = time, from = 29, bit  = 32) +
             sine(6, duration = time, from = pi/23, bit = 32)

#Creating noise using the inbuilt noise function which is to be
#filtered by FFT.
noise_wave = 5*noise("power", duration = time, bit = 32)

#Combining the clean wave and noise.
comb_wave = clean_wave + noise_wave

#Plotting the combined wave and highlighting the clean and noisy parts.
plot(comb_wave@left, ty = 'l',col='grey',lwd=2,ylab='Amplitude',xlab='Sample points')
lines(clean_wave@left,lwd=2)
legend('topright',legend=c('Noise','Clean wave'),col=c('grey','black'), lty=1, lwd=2)

#Implementing Fast Fourier Transform on the combined wave and plotting it.
FFT = fft(comb_wave@left)
PSD = Mod(FFT)/time #Power Spectrum Density
freq = (samp_rate/time)*(1:time) 
uplim = as.numeric(time/2) #Setting upper limit
plot(ylab='FFT',xlab='frequency',freq[2:uplim], PSD[2:uplim], ty = 'l')
#The three peaks correspond to the 3 frequencies of the original 3 sine waves.