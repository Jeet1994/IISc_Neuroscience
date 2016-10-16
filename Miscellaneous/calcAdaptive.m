function adapBinnedRateMap = calcAdaptive(spikeMap, occMap)
samplingrate = 30; %frames/sec
alpha = 0.0001; %change according to our experimental settings
z = zeros(size(occMap)); %zero array of size = occMap size 
adapBinnedRateMap = z; %adaptive binned rate map
adapBinnedOccMap = z; %adapative binned occupancy map

if max(max(spikeMap))>0 %makesure that there is atleast 1 spike in the spike map.
    for x = 1:size(occMap,2)
        for y = 1:size(occMap,1)
            if occMap(y, x) > 0
                rsquare = 0;  % the 'r' scaling factor from Skaggs code
                Nspikes2 = 1; %pretend there's atleas 1 spike, and 1 occ. needed to avoid 0 threshold. 
                Nocc = occMap(y, x); %number of times visited by rat
                d = z;
                d(y, x) = 1; 
                dists = bwdist(d); %distance transform..... ask Sachin about this??
                [Nspikes Nocc] = mexAdaptwhile(spikeMap, alpha, Nocc, dists, occMap); %takes spikeMap, alpha, occupancy count, distance tranformation and occupancy map as input
                if Nocc < 15 % < 0.5sec occupancy. both Skaggs and Jim use this cut off. though I think occupancy for this pixel needs to be set to zero, too. (can't see it done in Jim's code). sac 1/7/09. fixed occupancy issue: sac 1/19/09
                    adapBinnedRateMap(y, x) = 0;
                    adapBinnedOccMap(y, x) = 0;
                else
                    adapBinnedRateMap(y, x) = samplingrate * Nspikes/Nocc;
                    adapBinnedOccMap(y, x) = Nocc;
                end
            end
        end
    end
end
cmax = max(max(adapBinnedRateMap));
if cmax > 0
    cmin = -(cmax/60);
else
    cmin = -1;
end
adapBinnedRateMap(adapBinnedOccMap==0) = cmin; %setting the value of the unoccupied pixels just -ve enough to be the first color in the color map. this includes pixels with too few frames after adaptive binning, not just unoccupied pixels
