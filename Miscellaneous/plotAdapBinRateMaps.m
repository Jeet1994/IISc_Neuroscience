matFiles = dir('Day*.UpdatedTimestamps.mat');
[N,L] = size(matFiles);

gwidth = 8;
sigma = 1.5;
h = fspecial('gaussian',gwidth, sigma);

%generating color map by adding black and white color to jet colormap
%on lower and higher end of colormap
cmp = [colormap(jet(256)); 1 1 1];

samplingRate = 30; %frames/sec
alpha = 0.001; %change according to our experimental settings

for i = 1:N
    data = load(matFiles(i).name);
    data = data(:);  
    spikeMap = data.spikeMap;
    occMap = data.occMap;
    
    [row, col] = find(occMap);
    minrow = min(row);
    maxrow = max(row);
    mincol = min(col);
    maxcol = max(col);
   
    [name, ~] = strsplit(matFiles(i).name, '.UpdatedTimestamps.mat');
    name = char(name{1,1});
    
    occMap = occMap/samplingRate;
    occMap2 = occMap;
    occMap2(occMap<.25) = 0;
    cmaxOccMap = max(max(occMap));
    newcminOccMap = -cmaxOccMap/63;
    occMapwhite = cmaxOccMap + abs(newcminOccMap);
    occMap(occMap==0) = occMapwhite;
    for i=1:size(occMap,1)
        for j=1:size(occMap,2)
            if ((i>=minrow) && (i<=maxrow) && (j>=mincol) && (j<=maxcol) && (occMap(i,j)==occMapwhite))
                occMap(i,j) = newcminOccMap;
            end
        end
    end
    
    spikeMap2 = spikeMap;
    spikeMap2(occMap2==0) = 0;
    cmaxSpikeMap = max(max(spikeMap));
    newcminSpikeMap = -cmaxSpikeMap/63;
    spikeMapwhite = cmaxSpikeMap + abs(newcminSpikeMap);
    spikeMap(occMap==occMapwhite)= spikeMapwhite;
    spikeMap(occMap==newcminOccMap)= 0;
 
    adapBinnedRateMap = calcAdaptive(spikeMap,occMap, samplingRate, alpha);
    savefile = sprintf('%s.abrmap.mat',name);
    save(savefile,'adapBinnedRateMap');
    
    cmaxAdaptiveRateMap = max(max(adapBinnedRateMap));
    newcminAdaptiveRateMap = -cmaxAdaptiveRateMap/63;
    adaptiveRateMapwhite = cmaxAdaptiveRateMap + abs(newcminAdaptiveRateMap);
    adapBinnedRateMap(occMap==newcminOccMap)= newcminAdaptiveRateMap;
    adapBinnedRateMap(occMap==occMapwhite)= adaptiveRateMapwhite;
    
    figure;
    axis off;
    axis equal;
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
    name2 = [name '_abrmap.fig'];
    savefig(name2);
    
    gaussOccMap = imfilter(occMap2, h, 'same');
    gaussSpikeMap = imfilter(spikeMap2, h,'same');
    
    gaussRateMap = (gaussSpikeMap)./gaussOccMap;
    cmaxgaussRateMap = max(max(gaussRateMap));
    newcmingaussRateMap = -cmaxgaussRateMap/63;
    gaussRateMapwhite = cmaxgaussRateMap + abs(newcmingaussRateMap);
    gaussRateMap(occMap==newcminOccMap)= newcmingaussRateMap;
    gaussRateMap(occMap==occMapwhite)= gaussRateMapwhite;
    
    clf(figure);
    figure;
    x1 = subplot(1,3,1);
    imagesc(gaussRateMap);
    axis(x1, 'image');
    axis(x1, 'off');
    colormap(cmp);
    colorbar;
    title('Rate Map (Hz)');
    x2 = subplot(1,3,2);
    imagesc(spikeMap);
    axis(x2, 'image');
    axis(x2, 'off');
    colormap(cmp);
    colorbar;
    title('Spike Map');
    x3 = subplot(1,3,3);
    imagesc(occMap);
    axis(x3, 'image'); 
    axis(x3, 'off');
    colormap(cmp);
    colorbar;
    title('Occupancy Map (secs)');
    name3 = [name '_gaussianrmap.fig'];
    savefig(name3);
    close all;
end

