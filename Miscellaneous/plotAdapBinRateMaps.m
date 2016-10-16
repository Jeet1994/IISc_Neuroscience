matFiles = dir('rawMaps*.mat');
[N,L] = size(matFiles);

gwidth = 5;
sigma = 1;
h = fspecial('gaussian',gwidth, sigma);

%generating color map by adding black and white color to jet colormap
%on lower and higher end of colormap
cmp = [0 0 0; colormap(jet(256)); 1 1 1];

samplingRate = 30; %frames/sec
alpha = 0.001; %change according to our experimental settings

for i = 1:N
    data = load(matFiles(i).name);
    data = data(:);  
    spikeMap = data.spikeMap;
    occMap = data.occMap;
    
    gaussOccMap = imfilter(occMap,h,'same'); %gaussian filtered occupancy map
    unvisited = find(occMap==0);  
    visited = find(occMap>0);
    
    adapBinnedRateMap = calcAdaptive(spikeMap,occMap, samplingRate, alpha);
    
    [name, ~] = strsplit(matFiles(i).name, '.UpdatedTimestamps.mat');
    name = [char(name{1,1})];
    
    savefile = sprintf('%s.abrmap.mat',name);
    save(savefile,'adapBinnedRateMap');
    
    occMap = occMap/samplingRate;
    cmaxOccMap = max(max(occMap));
    newcminOccMap = -cmaxOccMap/63;
    occMapwhite = cmaxOccMap + abs(newcminOccMap);
    occMap(unvisited) = occMapwhite;
    
    cmaxSpikeMap = max(max(spikeMap));
    newcminSpikeMap = -cmaxSpikeMap/63;
    spikeMapwhite = cmaxSpikeMap + abs(newcminSpikeMap);
    spikeMapUpdated = spikeMap;
    spikeMapUpdated(unvisited)= spikeMapwhite;
    spikeMap = spikeMapUpdated;
    
    adapBinnedRateMap = adapBinnedRateMap*samplingRate;
    cmaxAdaptiveRateMap = max(max(adapBinnedRateMap));
    newcminAdaptiveRateMap = -cmaxAdaptiveRateMap/63;
    adaptiveRateMapwhite = cmaxAdaptiveRateMap + abs(newcminAdaptiveRateMap);
    adapBinnedRateMapUpdated = adapBinnedRateMap;
    adapBinnedRateMapUpdated(unvisited)= adaptiveRateMapwhite;
    adapBinnedRateMap = adapBinnedRateMapUpdated;
    
    figure;
    subplot(1,3,1);
    imagesc(adapBinnedRateMap);
    colormap(cmp);
    colorbar;
    title('Adaptive Rate Map(Hz)');
    subplot(1,3,2);
    imagesc(spikeMap);
    colormap(cmp);
    colorbar;
    title('Spike Map');
    subplot(1,3,3);
    imagesc(occMap);
    colormap(cmp);
    colorbar;
    title('Occupancy Map(secs)');
    name = [name '.fig'];
    savefig(name);
    close all;
end

