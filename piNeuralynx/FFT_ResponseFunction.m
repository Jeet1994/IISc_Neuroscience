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
   f = -Fs/2:dF:Fs/2-dF;           % hertz
   %% Fourier Transform:
   X = fftshift(fft(x));   
   %% Plot the spectrum:
   figure;
   plot(f,abs(X));
   xlabel('Frequency (in hertz)');
   title('Magnitude Response');
   [name, r] = strtok(name, '.')
   savefig(name);
   close all;
   end