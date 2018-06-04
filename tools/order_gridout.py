#!/usr/bin/python

import sys
import os

if __name__ == '__main__':
    
    print ("The arguments are: " , str(sys.argv))
    if len(sys.argv) < 3:
        print( sys.argv[0] + " <in file 1> <in file 2>")
        sys.exit(-1)
    degree = {}
    filepath = sys.argv[1]
    filepath1 = sys.argv[2]
    n = 0
    print("Reading \n")
    with open(filepath, 'r') as file:
        for line in file:
            n += 1
            node_pair = line.split(",")
            node_pair[2] = node_pair[2][0:-1]
            #degree
            if node_pair[0] not in degree:
                degree[node_pair[0]] = (node_pair[1],node_pair[2]) 
                
                

            if n % 500 == 0:
                print("Reading " + str(n))

    with open(filepath1, 'r') as file1:
        for line in file1:
            node_pair = line.split(",")
            node_pair[2] = node_pair[2][0:-2]
            #degree
            #print((node_pair[1],node_pair[2]))
            #print("\n")
            #print(degree[node_pair[0]])
            if node_pair[0] not in degree:
                print("Not in " + node_pair[0])
            elif degree[node_pair[0]] != (node_pair[1],node_pair[2]):
                print("Error " + degree[node_pair[0]])

                

#    n = 0
#    print("Writing \n")
#    fileAdj = open(sys.argv[2],"w")
#    for k,v in degree.items():
#        n =+ 1
#        node = str(k) + "," + str(v[0]) + "," + str(v[1])
#        fileAdj.write(str(node) + "\n")
#        if n % 500 == 0:
#            print("Writing %d",n)
        
#    fileAdj.close()

	