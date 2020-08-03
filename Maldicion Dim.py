
# Generating random numbers between zero and one from uniform 
# distribution with the given dimension
def random_point_gen(dimension): 
     return [random.random() for _ in range(dimension)] 

# Root mean sum of squares of Euclidean distances (2-norm) between points 
def distance(a,b): 
     diff = [a_i-b_i for a_i,b_i in zip(a,b)] 
     sum_of_sqrs = sum(a_i**2 for a_i in diff) 
     return math.sqrt(sum_of_sqrs) 

# Calculating the distances 
def random_distances_comparison(dimension,number_pairs): 
     return [distance(random_point_gen(dimension),random_point_gen(dimension)) 
            for _ in range(number_pairs)] 
    
def mean(x): 
     return sum(x) / len(x)

dimensions = range(1, 201, 5)



avg_distances = [] 

dummy = np.empty((20,2)) 
dist = pd.DataFrame(dummy) 
dist.columns = ["Dimension","Avg_Distance"] 
 
random.seed(34) 
i = 0 
for dims in dimensions: 
    distances = random_distances_comparison(dims, 1000)   
    avg_distances.append(mean(distances))     
     
    dist.loc[i,"Dimension"] = dims 
    dist.loc[i,"Avg_Distance"] = mean(distances) 
           
    print(dims,mean(distances))
    i = i+1

plt.plot(dist["Dimension"],dist["Avg_Distance"])
plt.title("Average Distance with Number of Dimensions for 1k Observations")
plt.xlabel('Dimensions') 
plt.ylabel('Avg. Distance') 
plt.legend(loc='best') 
plt.show();