function adapBinnedRateMap = calcAdaptive(spikeMap, occMap, samplingRate, alpha)
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
                if Nocc < 10 % < 0.5sec occupancy
                    adapBinnedRateMap(y, x) = 0;
                    adapBinnedOccMap(y, x) = 0;
                else
                    adapBinnedRateMap(y, x) = samplingRate * Nspikes/Nocc;
                    adapBinnedOccMap(y, x) = Nocc;
                end
            end
        end
    end
end