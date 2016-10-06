import random
import numpy as np
import matplotlib.pyplot as plt
import time
import pathlib
import configparser

Config = configparser.ConfigParser()
Config.read("config.txt")
verbose = Config.getboolean('Main', 'verbose')
trials = Config.getint('Main', 'trials')

perfectmatch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counts = []
results = []
prettyresults = []

start = time.time()

for x in range(trials):
	correct = 0
	component = random.sample(range(11), 11)
	if component == perfectmatch:
		if verbose == True:		
			print(component)			
			print("success")
		else:
			pass	
	else:
		if verbose == True:		
			print(component)
			print("failure")		
		else:		
			pass
		for x in component:
			if component.index(x) == x:
				correct = correct + 1
				if verbose == True:
					print("correct")
				else:
					pass
			else:
				if verbose == True:
					print("incorrect")
				else:
					pass
	counts.append(correct)	
		
for x in counts:
	percent = (float(x)/float(11))
	results.append(percent)

for x in results:
	pretty = str(round(x, 2))
	prettyresults.append(pretty)


npresults = np.array(results)
npcounts = np.array(counts)

if verbose == True:
	print(results)
	print(prettyresults)
	print(counts)
else:
	pass

print("n:" + " " + str(len(counts)))
print()
print("min:" + " " + str(min(counts)))
print("Q1:" + " " + str(np.percentile(npcounts, 25, interpolation="linear")))
print("med:" + " " + str(np.percentile(npcounts, 50, interpolation="linear")))
print("Q3:" + " " + str(np.percentile(npcounts, 75, interpolation="linear")))
print("max:" + " " + str(max(counts)))
print()
print("mean:" + " " + str(np.mean(npcounts)))
print("std:" + str(np.std(npcounts)))
graph = plt.hist(npcounts, bins = (0,1,2,3,4,5,6,7,8,9,10,11), alpha = 0.75)
fig = plt.gcf()
fig.canvas.set_window_title('ESP Histogram') 

plt.title("Correctly Matched Envelopes")
plt.xlabel("Number of Envelopes Correct")
plt.ylabel("Frequency")

elapsedtime = time.time() - start
print("elapsed time:" + " " + str(elapsedtime))
plt.show()


