x = what;
x = x.mat;

for i = 1:2
    t = load(char(x(i)));
    t = t(:);
    FFT_ResponsePlot(t,char(x(i)) );
end

