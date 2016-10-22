matFiles = dir('Day*.UpdatedTimestamps.mat');
[N,L] = size(matFiles);

gwidth = 10;
sigma = 1.0;
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
    rawRateMap = data.rateMap;
    
    unvisited = find(occMap==0);  
    visited = find(occMap>0);
    
    [row col] = find(occMap);
    minRow = min(row);
    minCol = min(col);
    maxRow = max(row);
    maxCol = max(col);
    
    adapBinnedRateMap = calcAdaptive(spikeMap,occMap, samplingRate, alpha);
    adapBinnedRateMap = adapBinnedRateMap*30;
    
    [name, ~] = strsplit(matFiles(i).name, '.UpdatedTimestamps.mat');
    name = [char(name{1,1})];
    savefile = sprintf('%s.abrmap.mat',name);
    save(savefile,'adapBinnedRateMap');
                            
    occMap = occMap/samplingRate;
    cmaxOccMap = max(max(occMap));
    newcminOccMap = -cmaxOccMap/63;
    occMapwhite = cmaxOccMap + abs(newcminOccMap);
    occMap(unvisited) = occMapwhite;
    for i=1:size(occMap,1)
       for j=1:size(occMap,2)
           if i>=minRow && i<=maxRow && j>=minCol && j<=maxCol && occMap(i,j) == occMapwhite
               occMap(i,j) = 0;
           end
       end
    end
    
    cmaxSpikeMap = max(max(spikeMap));
    newcminSpikeMap = -cmaxSpikeMap/63;
    spikeMapwhite = cmaxSpikeMap + abs(newcminSpikeMap);
    spikeMap(occMap==occMapwhite)= spikeMapwhite;
    
    cmaxAdaptiveRateMap = max(max(adapBinnedRateMap));
    newcminAdaptiveRateMap = -cmaxAdaptiveRateMap/63;
    adaptiveRateMapwhite = cmaxAdaptiveRateMap + abs(newcminAdaptiveRateMap);
    adapBinnedRateMap(occMap==occMapwhite)= adaptiveRateMapwhite;
    
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
    savefile = sprintf('%s.abrmap.fig',name);
    savefig(savefile);
    
    mask = zeros(size(occMap));
    rateMap = mask;
    gaussRateMap = mask;
    rateMap(visited) = (spikeMap(visited)*samplingRate)./occMap(visited);
    gaussSpikeMap = imfilter(spikeMap,h,'same'); %gaussian filtered spkmap
    gaussOccMap = imfilter(occMap,h,'same'); %gaussian filtered occupancy map
    gaussRateMap(visited) = (gaussSpikeMap(visited)*30)./gaussOccMap(visited);

    savefile = sprintf('%s.gaussrmap.mat',name);
    save(savefile,'gaussRateMap'); 
    
    cmaxGaussianRateMap = max(max(gaussRateMap));
    newcminGaussianRateMap = -cmaxGaussianRateMap/63;
    gaussianRateMapwhite = cmaxGaussianRateMap + abs(newcminGaussianRateMap);
    gaussRateMap(occMap==occMapwhite)= gaussianRateMapwhite;
    
    clf(figure);
    figure;
    subplot(1,3,1);
    imagesc(gaussRateMap);
    colormap(cmp);
    colorbar;
    title('Gaussian Rate Map(Hz)');
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
    savefile = sprintf('%s.gaussian.fig',name);
    savefig(savefile);

    close all;
end
