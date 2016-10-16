matFiles = dir('rawMaps*.mat');
[N,L] = size(matFiles);

gwidth = 5;
sigma = 1;
h = fspecial('gaussian',gwidth, sigma);

samplingRate = 30; %frames/sec
alpha = 0.0001; %change according to our experimental settings

for i = 1:N
    data = load(matFiles(i).name);
    data = data(:);  
    spikeMap = data.spikeMap;
    occMap = data.occMap;
    gaussOccMap = imfilter(occMap,h,'same'); %gaussian filtered occupancy map
    unvisited = find(occMap==0);  
    visited = find(occMap>0);
    %occupancy figure and save
    cmax = max(max(occMap));
    cmin = -(cmax/60); %setting the value of the unoccupied
    occMap(unvisited) = cmin; %pixels just -ve enough to be the first color in the color map
    savefile = sprintf('%s.occ.mat',matFiles(i).name);
    save(savefile,'occMap');
    
    adapBinnedRateMap = calcAdaptive(spikeMap,occMap, samplingRate, alpha);
    
    savefile = sprintf('%s.abrmap.mat',matFiles(i).name);
    save(savefile,'adapBinnedRateMap');

    mask = zeros(size(occMap));
    rateMap = mask;
    gaussRateMap = mask;
    rateMap(visited) = (spikeMap(visited)*30)./occMap(visited);
    gaussSpikeMap = imfilter(spikeMap,h,'same'); %gaussian filtered spkmap
    gaussRateMap(visited) = (gaussSpikeMap(visited)*30)./gaussOccMap(visited); %taking the ratio of gaussian smoothed spk map and gaussian smoothed rate map takes care of lesser number of pixels used while smoothing pixels next to the unoccupied pixels.
    cmax = max(max(rateMap));
    if cmax > 0
        cmin = -(cmax/60);
    else
        cmin = -1;
    end
    rateMap(unvisited) = cmin;
    savefile = sprintf('%s.rawrmap.mat',matFiles(i).name);
    save(savefile,'rawrmap');
    cmax = max(max(gaussRateMap));
    if cmax > 0
        cmin = -(cmax/60);
    else
        cmin = -1;
    end
    gaussRateMap(unvisited) = cmin;
    savefile = sprintf('%s.grmap.wid%d.sig%d.mat',matFiles(i).name,gwidth,sigma);
    save(savefile,'gaussrmap');
end

