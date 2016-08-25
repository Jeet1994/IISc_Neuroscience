function plotting(datum, name)
%% Time specifications:
Fs = datum.samplingRate;       % samples per second
t = 0:1/Fs:1-1/Fs;

x = datum.rawData;
N = length(x);
xdft = fft(x);
xdft = xdft(1:N/2+1);
psdx = (1/(Fs*N)) * abs(xdft).^2;
psdx(2:end-1) = 2*psdx(2:end-1);
freq = 0:Fs/length(x):Fs/2;

% plot(freq,10*log10(psdx))
plot(freq,(psdx))

title('Periodogram Using FFT')
xlabel('Frequency (Hz)')
ylabel('Power/Frequency (V**2/Hz)')
[name, r] = strtok(name, '.')
savefig(name);
close all;   
end