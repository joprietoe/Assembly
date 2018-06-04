#!/usr/bin/python

import sys
import os

if __name__ == '__main__':
    
    print ("The arguments are: " , str(sys.argv))
    if len(sys.argv) < 3:
        print( sys.argv[0] + " <in file edge list> <out file>")
        sys.exit(-1)
    outdegree = {}
    indegree = {}
    degree = {}
    filepath = sys.argv[1]
    n = 0
    print("Reading \n")
    with open(filepath, 'r') as file:
        for line in file:
            n += 1
            node_pair = line.split("\t")
            node_pair[1] = node_pair[1][0:-1]
            #out degree
            if node_pair[0] not in degree:
                degree.setdefault(node_pair[0],[]).append(1) 
                degree[node_pair[0]].append(0)
            else:                
                degree[node_pair[0]][0] += 1
            
            if node_pair[1] not in degree:
                degree.setdefault(node_pair[1],[]).append(0) 
                degree[node_pair[1]].append(1)
            else:                
                degree[node_pair[1]][1] += 1

            #in degree

            if n % 500 == 0:
                print("Reading " + str(n))

    n = 0
    print("Writing \n")
    fileAdj = open(sys.argv[2],"w")
    for k,v in degree.items():
        n =+ 1
        node = str(k) + "," + str(degree[k][0]) + "," + str(degree[k][1])
        fileAdj.write(str(node) + "\n")
        if n % 500 == 0:
            print("Writing %d",n)
        
    fileAdj.close()

	