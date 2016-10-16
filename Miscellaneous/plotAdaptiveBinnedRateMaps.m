matFiles = dir('rawMaps*.mat');
[N,L] = size(matFiles);
for i = 1:N
    data = load(matFiles(i).name);
    data = data(:);
    spikeMap = data.spikeMap;
    occMap = data.occMap;
    adapBinnedRateMap = calcAdaptive(spikeMap,occMap);%,matFiles(i).name);
end

