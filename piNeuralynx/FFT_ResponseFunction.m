   function plotting(datum, name)
   %% Time specifications:
   Fs = datum.samplingRate;       % samples per second
   dt = 1/Fs;                     % seconds per sample
   StopTime = 1;                  % seconds
   t = (0:dt:StopTime-dt);
   %% Sine wave
   %%x = load('AnalogRat_Ir1000_t256_64CSC_FullBand_1SSI_KEBPower_DedicatedGround2016-08-13_17-17-30_CSC30_rawData.mat', 'rawData');
   x = datum.rawData;
   [L,N] = size(x);
   %% Frequency specifications:
   dF = Fs/N;                      % hertz
   f = Fs*(0:(N/2))/N;          % hertz
   %% Fourier Transform:
   Y = fft(x); 
   P2 = abs(Y/N);
   P1 = P2(1:N/2+1);
   P1(2:end-1) = 2*P1(2:end-1);
   %% Plot the spectrum:
   figure;
   plot(f,P1)
   title('FFT Plots')
   xlabel('f (Hz)')
   ylabel('Magnitude |P1(f)| (MicroVolts)')
   [name, r] = strtok(name, '.')
   savefig(name);
   close all;
   end