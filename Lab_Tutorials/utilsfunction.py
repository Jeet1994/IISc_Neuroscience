import numpy as np
import pylab as pl

'''
Function to compute the correlation coefficient given a certain time-window [time_window in ms]
Note, that the spiketrains are given as vectors containing the firing times of each neuron.
Recording time T in seconds!
'''
def corr_coeff(spktr1, spktr2, time_window,T):
	dt = 0.1			# time resolution [ms]		
	t = np.arange(0,1000*T+dt,dt)	
	# time window is implemented as a boxkernel of length time_window/dt
	boxkernel = np.ones(np.ceil(time_window/dt))
	# create arrays that contain 1's for spiketimes, and 0s otherwise 	
	hist1 = np.zeros(len(t))
	hist1[(spktr1*1000/dt).astype(int)]=1
	hist2 = np.zeros(len(t))
	hist2[(spktr2*1000/dt).astype(int)]=1

	# convolution with the boxkernel is an efficient way to count the events in the 
	# interval time_window 
	n1 = np.convolve(hist1,boxkernel,'same')
	n2 = np.convolve(hist2,boxkernel,'same')

	# use a built-in numpy function to compute the correlation coefficient between the 
	# count sequences:
	rho = np.corrcoef(n1,n2)[0,1]
	return rho

'''
Function to compute the Cross Covariance between t2 spike trains
Note, that the spiketrains are given as vectors containing the firing times of each neuron.
Recording time T in seconds!
'''

# cross-covariance function
def cross_cov(spktr1, spktr2,T,plot=True):
    # reverse the order if spktr2 is longer, such that we always loop over the shorter 
    # array later. This speeds up the code.   
    if len(spktr1)>len(spktr2):
	spktr1,spktr2 = spktr2, spktr1
	reverse = True # set a flag, so we can later switch back to the original order
    else:
	reverse = False
    Delta_t = np.array([])
    # collect all the timedifferences
    for k in range(len(spktr1)):
        Delta_t = np.append(Delta_t, spktr2-spktr1[k])
    if reverse: 
	Delta_t=-Delta_t
    meanrate_1 = len(spktr1)/T
    meanrate_2 = len(spktr2)/T
    dt = 0.001 #[s]	
    t = np.arange(-T,T+dt,dt) 
    # bin the time differences	
    crosscov = np.histogram(Delta_t, len(t),(-T,T))[0]/(dt*T)
    # subtract mean rates, the last term is to cancel boundary effects
    crosscov = crosscov-meanrate_1*meanrate_2*(T-np.abs(t))/T
    if plot:
        pl.figure()
        pl.plot(t,crosscov)
        pl.title('Cross covariance function')
        pl.xlabel('$\Delta$t [s]')
        pl.xlim([-1,1])
        pl.ylabel('C($\Delta$t)')
        pl.grid(True)
        pl.show()
    return t, crosscov



'''
This function generates a Poissonian spiketrain. It takes as inputs
the mean rate and the recording interval T. 
The code generates random numbers from an exponential distribution 
in order to arrive at the next spiketime by adding the random number to 
the last spiketime, making use of the fact, that inter-event-intervals 
in a Poisson process follow an exponential distribution.
'''
def poisson_generator(rate,T):
    try:
        N_events = np.random.poisson(rate*T)
    except:
        raise Exception('rate has to be a nonnegative number!')
    return T*np.sort(np.random.rand(N_events))

'''
plots the spiketrains. takes as input a tuple containing the spiketrains, so 
don't forget the extra brackets 
''' 
def spiketrainplot(spiketrains, interval = [0,50]):
    n = len(spiketrains)   
    pl.figure(figsize=(10,n+1.))
    for i,add_sp in enumerate(spiketrains):
        pl.plot(add_sp,-(i+1)*np.ones(len(add_sp)),'|',markersize=50.);   
    pl.ylim([-n-0.5,-0.5])
    yticklabels=['Spiketrain 1']    
    for i in range(2,n+1):
        yticklabels=np.append('Spiketrain '+str(i),yticklabels)
    pl.subplots_adjust(left=0.15, right=0.95, top=1-0.3/(n+1.), bottom=0.7/(n+1.))    
    pl.yticks(range(-n,0),yticklabels)
    pl.xlabel('Time [s]')
    pl.xlim(interval)


'''
A simple implementation of a leaky integrate-and-fire-neuron. The 
input arguments are the input-spiketrain, the recording time T, and
as optional argument an input signal, and the threshold potential v_thr.
The output is again an array of firing-times. 
'''

def simple_neuron(spktr,T,signal=0,Jsyn=5.):
    v_0 = -60	# resting potential
    v_thr = -40     # threshold potential
    tau = 25.       #membrane time constant [ms]
    v = v_0		# initial membrane potential
    dt = 0.1	# timestep of the integration [ms]
    time = np.arange(dt/1000.,T+dt/1000.,dt/1000.)

    # make sure the input firingtimes are in chronological order:
    spktr=np.append(np.sort(spktr),T+dt/1000)
    output=np.array([])	# initialize output firingtimes        
    count=0		# variable to count input spikes
    for t in time:
        v=v+dt/tau*(-(v-v_0)+signal)	# forward Euler
        if t>spktr[count]:	      # input spike condition  	
            v+=Jsyn            
            count+=1	
        # if threshold is reached, reset to resting potential 
     	  # and record output firing time
        if v>v_thr:			
            v=v_0
            output=np.append(output,t)   
    return output
