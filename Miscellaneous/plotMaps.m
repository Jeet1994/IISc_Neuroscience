matFiles = dir('rawMaps*.mat');
[N,L] = size(matFiles);
samplingRate = 30; %frames/sec

for i = 1:N
    data = load(matFiles(i).name);
    data = data(:);
    plotMapsFunction(data,matFiles(i).name, samplingRate);
end

