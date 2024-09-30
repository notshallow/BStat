# Loading necessary libraries.
library(DescTools) #Required for implementing the mode function.
library(tuneR)     #Required for reading the input audio wave.

# Reading input audio file and extracting relevant information.
aud_wave = readWave("Audio/Main Audio.wav")
aud_data = aud_wave@left
sam_rate = aud_wave@samp.rate #Sampling rate
sam_count = length(aud_data) 

# Defining window size based on sample rate.
win_size = as.numeric(sam_rate/10)-1 

# Initializing variables for variance values (VAR) and sequence of indices.
VAR = c()
indices = seq(1, sam_count - win_size, 1000)

# Appending variance values for the overlapping windows.
for(j in indices){
  VAR = append(VAR, var(aud_data[j:(j+win_size)]))
}

# Normalizing variance values to a scale of 0 to 1000.
VAR = 1000*((VAR-min(VAR))/(max(VAR)-min(VAR)))

# Uncomment plot commands to view.
# plot(indices, VAR, type = 'l')

# Defining the cutoff for the noisy audio.
int_var = as.integer(VAR/25) 
mode_var = Mode(int_var)
cut_off = 25*(mode_var+1)+1
# plot(int_var, type = 'l')

# Initializing a variable to store the de-noised audio data.
den_aud_data = aud_data 

# Eliminating noise from the "noisy" parts determined by our cutoff.
for(i in 1:length(VAR)){
  if(VAR[i] < cut_off){
    k = indices[i]
    den_aud_data[k:(k+win_size)] = 0
  }
  else if(VAR[i] >= cut_off & VAR[i] < (1.5)*cut_off){
    k = indices[i]
    den_aud_data[k:(k+win_size)] = (den_aud_data[k:(k+win_size)])/2
  }
}

# plot(aud_data, type = 'l')
# plot(den_aud_data, type = 'l')

# Saving and writing the de-noised audio data.
den_aud_wave = aud_wave
den_aud_wave@left = den_aud_data

writeWave(den_aud_wave, "Output/denoised_Main Audio.wav")