# Cluster_GeneExpression
An implementation of finding clusters from gene expression data using Evolutionary Computation method in python.

1. What is this program for?
This program is an implementation of finding clusters from gene expression data using Evolutionary Computation method in python. 
It has the input of expression matrix and the theta value, as a threshold for the mean squared residue. 
Then it returns either a cluster with mean squared residue lower than the threshold. 
The returned cluster is stored in a list called Results, and function is called again. When the end condition is met, the list Results is returned.

2. Parameters the program used:
	Population size: 200
	Number of generations: 100
	Weight for conditions: 10
	Weight for genes: 1
	Crossover probability: 0.85
	Mutation probability: 0.2
	Elitism probability: 0.9
	Yeast Threshold: 300
	lymphomaThreshold: 1200

3. Overview the program code: 
	his program has 5 python files, one main file and four function files in ~/Fun_Package/.
	SEBI_main.py     
	Data_Load_Encode.py     Load_Data(), Preprocess_Data()
	GA.py     				Genetic_Algorithm()
	Genetic_Operator.py     Crossover_Operator(), Selection_Operator(), Mutation_Operator()
	Fitness_Function.py     Mean_Squared(), Row_var(), Decode_Binary(), Penalty_cal()

	SEBI_main.py            - the main part of the program
	Data_Load_Encode.py 	- load the gene expression matrix, replace the missing values with random number and encode the elements in the matrix into binary strings.
	GA.py 					- use the typical evolutionary computation method Genetic Algorithm to find the optimal clusters within the gene expression data
	Genetic_Operator.py 	- give crossover and mutation operators to each individual
	Fitness_Function.py 	- calculate the fitness value for each individual, this value indicates each individual’s quality.

	Program structure:
	main file  -->  Data_Load_Encode
						--> Load_Data()
						--> Preprocess_Data()
			   -->  GA
						--> Genetic_Algorithm()
								--> Fitness_Function
									   --> Mean_Squared()
									   --> Row_var()
									   --> Decode_Binary()
									   --> Penalty_cal()
								--> Genetic_Operator
									   --> Crossover_Operator()
									   --> Mutation_Operator()
									   --> Mutation_Operator()
									   --> Selection_Operator()

4. How to use the program?
	For example, run the program in Bluenose: 
		Bluenose: python main.py
	The program will ask you to choose a data file, there are three data files: yeast.matrix, lymphoma.matrix and yeast_test.matrix. 
	Because running the first two files will take an extremely long time, it recommend to use yeast_test.matrix for testing. 
	The result is saved in “Result_File.txt” file.
								  
