import numpy as np

class fit:
	'''
	This creates an instance of the class OLS with attributes coefficients, fitted_values, residuals, and rsquared 
	'''
	def __init__(self, data, outcome, predictors):
		#We do the following so we can call them as attributes
		#self.data = data
		self.outcome = outcome
		self.predictors = predictors
		self.results = {}
		self.iterate(data, outcome, predictors)
		
	def ols(self, Y, X): #Y is an nx1 vector, X is an nxp matrix
		X_transpose = np.transpose(X)
		X_transpose_X = np.dot(X_transpose, X)
		X_inverse = np.linalg.inv(X_transpose_X)
		X_transpose_Y = np.dot(X_transpose, Y)
		
		
		self.coefficients = np.dot(X_inverse, X_transpose_Y)
		#self.fitted_values = np.dot(X, self.coefficients)		
		#self.residuals = Y - self.fitted_values
		self.intercept = float(self.coefficients[0])
		self.coefficients = list(self.coefficients[1:]) #Change type to list
		#SStotal
		#yty = np.dot(np.transpose(Y),Y)
		#j = np.ones((len(Y),len(Y)))
		#ytj = np.dot(np.transpose(Y), 	j)
		#ytj = np.dot(ytj,Y)/len(Y)
		#ssto = yty - ytj
		#SSerror
		#sse = np.dot(np.transpose(self.residuals), self.residuals)
		#SSregression
		#ssr = ssto - sse
		#rsquared
		#self.rsquared = ssr/ssto
		
	def iterate(self,data, outcome, predictors):
		#eventually we need to iterate through all the permutations of variables, but let's just try one column first
		
		#Create dataset where we listwise remove missing values
		Y = np.array(data['{0}'.format(outcome)])
		all_data = np.column_stack((Y, np.ones((len(Y), 1))))
		for bs in predictors:
			all_data =  np.column_stack((all_data, np.array(data[bs])))
		all_data = all_data[~np.isnan(all_data).any(axis=1)]
		Y = all_data[:,0]
		C = all_data[:,1]
		X = all_data[:,2:]
		
		#We might need to code this a different way - store by number of predictors in model rather than by each predictor
		
		for j in range(0, len(predictors)): #for all the predictors in this case 1 to 6
			#all the other predictors besides J
			other_predictors = range(0,len(predictors))
			other_predictors = [x for x in other_predictors if x != j]
			#range from one additional predictor to all predictors
			temp_coeffs = []
			for k in range(1, len(other_predictors)+1):
				z = other_predictors[:k]
				#iterate through all the other predictors, and fit each one
				#Define what the X array is
				curr_X = X[:,j] #This is the column of the current predictor 
				curr_X = np.column_stack((C,curr_X)) #Adding the intercept
				curr_X = np.column_stack((curr_X, X[:,z]))
				self.ols(Y, curr_X)
				temp_coeffs.append(self.coefficients[0])
			print temp_coeffs
			self.results[predictors[j]] = np.mean(temp_coeffs)
			