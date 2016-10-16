//You can include any C libraries that you normally use
#include "math.h"
#include "mex.h"   //--This one is required

void adapt_while(double rsq, double EnoughPoints, double r, int i, int j,double *pdists, int rowLen, int colLen, double *Nspikes, double *prawspkmap,  double Nocc, double *pocc, double Nspikes2,  double alpha, double *Noccout)
{
    while ((rsq < 200.00) && (EnoughPoints == 0))
    {
        r = sqrt(rsq);
        *Nspikes = 0; //need to set these things to zero, otherwise the two for loops above add the same spikes over again.
        Nocc = 0;
        for (i=0;i<rowLen;i++)
        {
            for (j=0;j<colLen;j++)
            {
                if (pdists[(i*colLen)+j]<=r)
                {
                    *Nspikes += prawspkmap[(i*colLen)+j];
                    Nocc += pocc[(i*colLen)+j];
                }
            }
        }
        if (*Nspikes > 0)
        {
            Nspikes2 = *Nspikes;
        }
        if (alpha*alpha*Nocc*Nocc*rsq*Nspikes2 > 1)
        {
            EnoughPoints = 1;
        }
        rsq = rsq + 1;
    }
    *Noccout = Nocc;
}

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
    //declarations
    double rsq;
    double EnoughPoints;
    double r;
    double *Nspikes;
    double Nocc;
    double *Noccout;
    double Nspikes2;
    double *pdists;
    double *prawspkmap;
    double alpha;
    mxArray *xData;
    int i;
    int j;
    int rowLen;
    int colLen;
    double *pocc;
    mxArray *temp;
    
    // create a 1-by-1 matrix for the return argument */
    plhs[0] = mxCreateDoubleMatrix(1,1,mxREAL);
    // assign a pointer to the output */
    Nspikes = mxGetPr(plhs[0]);

    // create a 1-by-1 matrix for the return argument */
    plhs[1] = mxCreateDoubleMatrix(1,1,mxREAL);
    // assign a pointer to the output */
    Noccout = mxGetPr(plhs[1]); 

    //Copy input pointer for rawspkmap
    xData = prhs[0];
    //Get matrix rawspkmap
    prawspkmap = mxGetPr(xData);
    rowLen = mxGetN(xData);
    colLen = mxGetM(xData);

    //Get scalar alpha
    alpha = mxGetScalar(prhs[1]);
    
    //Get scalar Nocc
    Nocc = mxGetScalar(prhs[2]);
    
    
    //Copy input pointer for dists
    xData = prhs[3];
    //Get matrix dists
    pdists = mxGetPr(xData);
    
    //Copy input pointer for occ
    xData = prhs[4];
    //Get matrix occ
    pocc = mxGetPr(xData);    
    

    Nspikes2 = 1;
    rsq = 0;
    EnoughPoints = 0;
    *Nspikes = 0;
    Nocc = 0;

    adapt_while(rsq, EnoughPoints, r, i, j, pdists, rowLen, colLen, Nspikes, prawspkmap, Nocc, pocc, Nspikes2, alpha, Noccout);

return;
}
