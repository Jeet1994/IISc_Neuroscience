
   %% Time specifications:
   Fs = 30000;                    % samples per second
   dt = 1/Fs;                     % seconds per sample
   StopTime = 1;                  % seconds
   t = (0:dt:StopTime-dt);
   %% Sine wave
   x = load('Mux_CSC40_rawData.mat', 'rawData');
   x = x.rawData;
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