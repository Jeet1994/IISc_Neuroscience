matFiles = dir('rawMaps*.mat');
[N,L] = size(matFiles);
for i = 1:N
    data = load(matFiles(i).name);
    data = data(:);
    plotMapsFunction(data,matFiles(i).name);
end

