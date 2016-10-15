function plotMapsFunction(datum, name)
    %loading the ratemap, spikemap, occupancy map
    rateMap = datum.rateMap;
    spikeMap = datum.spikeMap; 
    occMap = datum.occMap;
    
    %generating color map by adding black and white color to jet colormap
    %on lower and higher end of colormap
    cmp = [0 0 0; colormap(jet(256)); 1 1 1];
    
    rateMap = (rateMap/33.31)*1000;
    cmaxRateMap = max(max(rateMap));
    newcminRateMap = -cmaxRateMap/63;
    rateMapwhite = cmaxRateMap + abs(newcminRateMap);
    rateMap(isnan(rateMap)) = rateMapwhite;
    
    occMap = occMap*0.03331;
    cmaxOccMap = max(max(occMap));
    newcminOccMap = -cmaxOccMap/63;
    occMapwhite = cmaxOccMap + abs(newcminOccMap);
    occMap(occMap==0) = occMapwhite;
    
    cmaxSpikeMap = max(max(spikeMap));
    newcminSpikeMap = -cmaxSpikeMap/63;
    spikeMapwhite = cmaxSpikeMap + abs(newcminSpikeMap);
    spikeMapUpdated = spikeMap;
    spikeMapUpdated(occMap==0)= 0;
    spikeMapUpdated(occMap==occMapwhite)= spikeMapwhite;
    spikeMap = spikeMapUpdated;
    
    figure;
    subplot(1,3,1);
    imagesc(rateMap);
    colormap(cmp);
    colorbar;
    title('Rate Map(Hz)');
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
    [name, ~] = strsplit(name, '.UpdatedTimestamps.mat');
    name = [char(name{1,1})];
    name = [name '.fig']
    savefig(name);
    close all;
end