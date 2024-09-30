#Loading necessary libraries
library(tuneR) #Required for reading the input audio wave

#Reading input audio file and extracting relevant information
aud_wave = readWave("Audio/Main Audio.wav")
aud_data = aud_wave@left
sam_rate = aud_wave@samp.rate
sam_count = length(aud_data)

#Plotting the input audio wave
plot(xlab='Sample points',ylab='Amplitude',  aud_data, type = 'l')

#Implementing Fast Fourier Transform on the audio wave and plotting it 
FFT = fft(aud_data)
PSD = Mod(FFT)/sam_count #Power Spectrum Density
freq = (sam_rate/sam_count)*(1:sam_count) 
uplim = as.numeric(sam_count/2) #Setting upper limit
plot(ylab='FFT', xlab='Frequency',freq[2:uplim], PSD[2:uplim], type = 'l')