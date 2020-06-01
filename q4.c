#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double f (double x)					/*exponential distribution with mean 0.5*/
{
    return(2*exp(-2*x));   
}

int main()
{
	FILE *mptr;
 	mptr = fopen("q4.dat","w");			/*opening file to print random numbers*/
	
	double runi, rexp;				/*initializing variables*/
	int i, j, num, npts;
	
	num = 100000;					/*number of random nos. generated*/
	npts = 50;
	
	for(i=0; i<num; i++)
		{
			runi = (double)rand() / (double)RAND_MAX ;	/*random nos. generated between 0 and 1 by dividing the random number by the max value*/
			rexp = -0.5*log(runi);				/*transformation from uniform pdf to exponential pdf*/
			if (i < 70)										
			{
				fprintf(mptr, "%e\t%e\t%e\n", runi, rexp, f(i/10));/*printing the numbers into file*/
			}																/*for the plot of true PDF only range from 0 to 7 is getting printed (70 points)*/
			else
			{
				fprintf(mptr, "%e\t%e\n", runi, rexp);	
			}
		}
	fclose(mptr);
	return 0;
}
