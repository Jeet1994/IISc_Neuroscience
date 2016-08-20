x = what;
x = x.mat;
[N,L] = size(x);
for i = 1:N+2
    t = load(char(x(i)));
    t = t(:);
    FFT_ResponseFunction(t,char(x(i)) );
end

