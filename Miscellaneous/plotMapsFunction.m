function plotMapsFunction(datum, name, samplingRate)
    %loading the ratemap, spikemap, occupancy map
    rateMap = datum.rateMap;
    spikeMap = datum.spikeMap; 
    occMap = datum.occMap;
    
    [row, col] = find(occMap);
    minrow = min(row);
    maxrow = max(row);
    mincol = min(col);
    maxcol = max(col);
    
    %generating color map by adding black and white color to jet colormap
    %on lower and higher end of colormap
    cmp = [0 0 0; colormap(jet(256)); 1 1 1];
    
    occMap = occMap/samplingRate;
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
    
    cmaxSpikeMap = max(max(spikeMap));
    newcminSpikeMap = -cmaxSpikeMap/63;
    spikeMapwhite = cmaxSpikeMap + abs(newcminSpikeMap);
    spikeMap(occMap==occMapwhite)= spikeMapwhite;
    spikeMap(occMap==newcminOccMap)= 0;
    
    rateMap = (rateMap*samplingRate);
    cmaxRateMap = max(max(rateMap));
    newcminRateMap = -cmaxRateMap/63;
    rateMapwhite = cmaxRateMap + abs(newcminRateMap);
    rateMap(occMap==occMapwhite)= rateMapwhite;
    rateMap(occMap==newcminOccMap)= 0;
    
    figure;
    subplot(1,3,1);
    imagesc(rateMap);
    colormap(cmp);
    colorbar;
    title('Rate Map (Hz)');
    subplot(1,3,2);
    imagesc(spikeMap);
    colormap(cmp);
    colorbar;
    title('Spike Map');
    subplot(1,3,3);
    imagesc(occMap);
    colormap(cmp);
    colorbar;
    title('Occupancy Map (secs)');
    [name, ~] = strsplit(name, '.UpdatedTimestamps.mat');
    name = [char(name{1,1})];
    name = [name '.fig'];
    savefig(name);
    close all;
end