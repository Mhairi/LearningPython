#For standaridized effects, error is 1 and mean differences are SDs
from scipy.stats import f,t #this imports the f and t distribution functions

def anovapower(df1, df2, alpha): #we take the n, the alpha and the effect size
	alpha = 1-alpha #to convert to the cumulative partition
	#df2 is related to sample size
	
	#
	return f.ppf (alpha, df1, df2)
	
def samplesize(arrayofmeans, alpha): #we'll take some standardized means, and an alpha level
	#we want to return the sample size needed
	alpha = 1-alpha
	meandifference = arrayofmeans[1]-arrayofmeans[0]
	n = 30
	if t.cdf(meandifference,n) > alpha:
		return 
