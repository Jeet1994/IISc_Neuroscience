function plotMapsFunction(datum, name)
    %loading the ratemap, spikemap, occupancy map
    rateMap = datum.rateMap;
    spikeMap = datum.spikeMap; 
    occMap = datum.occMap;
    
    %generating color map by adding black and white color to jet colormap
    %on lower and higher end of colormap
    cmp = [0 0 0; colormap(jet(256)); 1 1 1];
    
    cmaxRateMap = max(max(rateMap));
    cminRateMap = min(min(rateMap));
    newcminRateMap = -cmaxRateMap/63;
    rateMapwhite = cmaxRateMap + abs(newcminRateMap);
    rateMap(isnan(rateMap)) = rateMapwhite;
    
    cmaxOccMap = max(max(occMap));
    cminOccMap = min(min(occMap));
    newcminOccMap = -cmaxOccMap/63;
    occMapwhite = cmaxOccMap + abs(newcminOccMap);
    occMap(occMap==0) = occMapwhite;
    
    cmaxSpikeMap = max(max(spikeMap));
    cminSpikeMap = min(min(spikeMap));
    newcminSpikeMap = -cmaxSpikeMap/63;
    spikeMapwhite = cmaxSpikeMap + abs(newcminSpikeMap);
    spikeMapUpdated = spikeMap;
    spikeMapUpdated(occMap==0)= 0;
    spikeMapUpdated(occMap==occMapwhite)= spikeMapwhite;
    spikeMap = spikeMapUpdated;
    
    figure;
    subplot(1,3,1);
    title('Rate Map');
    imagesc(rateMap);
    colorbar;
    subplot(1,3,2);
    title('Spike Map');
    imagesc(spikeMap);
    colormap(cmp);
    colorbar;
    subplot(1,3,3);
    title('Occupancy Map');
    imagesc(occMap);
    colormap(cmp);
    colorbar;
    [name, r] = strtok(name, '.');
    savefig(name);
    close all;
end