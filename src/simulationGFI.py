#! /usr/bin/env python
__author__ = "Mehmood Alam Khan, adapted by Lars Arvestad"
__email__  = "malagori@kth.se, arve@nada.su.se"
__version__= "0.9"
__credits__ = ["Mehmood Alam Khan", "Lars Arvestad"]
'''
Created on Apr 4, 2014

@author: malagori
'''
import sys
import argparse
import os
import subprocess
import random
import datetime
import time
import tempfile
import logging

def checkExe(exePath):
    return os.path.isfile(exePath) # and os.access(exePath, os.X_OK)
    
def Where(program):
    '''
    input: name of executable
    output: path to executable
    '''
    fpath, fname = os.path.split(program)
    if fpath:
        if checkExe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            pathToProgram = os.path.join(path, program)
            if checkExe(pathToProgram):
                return pathToProgram
    return None

def generateGTreesAndAlignmets(work_dir, outFile, sTree, seed, dup, trans, loss, length, model, theta, k, minper, jarFileName, logfile):
    '''
    Call GenPhyloData and seq-gen to generate gene trees and their sequences.

    Parameters:
    sTree - Dated species tree
    seed  
    minper - Minimum number of gene tree leaves per species
    logfile - Destination for progress output
    '''

    # check if path exists
    print jarFileName
    cmd= Where(jarFileName)
    #cmd= '/Users/malagori/Documents/Academic/project/infer-gfamily-project/data/simulation/jars/jprime-0.3.4.d.jar'
    if cmd != None:
        gTree= os.path.join(work_dir, outFile)
        brGTree= os.path.join(work_dir, outFile+".relaxed.tree")

        try:
            print "--> GenPhyloData begins..."
            logfile.write("Seed: " + str(seed) + "\n")
            subprocess.call("java -jar "+cmd+ " GuestTreeGen -s "+ str(seed) + " -minper "+str(minper)+" -max 1000 -a 10000000 "+ sTree+ " "+ str(dup) + " "+ str(loss)+ " "+ str(trans) +" "+ gTree, shell=(sys.platform!="win32"), stdout=logfile, stderr=logfile)
            
        except IOError, e:
            print ("Error in function: generateGTreesAndAlignmets: %s " % e)
            exit(1)
        print "--> GenPhyloData ends..."
        print "--> Branch Relaxation begins..."
        try:
            seed += 11
            #varying branch length
            subprocess.call("java -jar "+cmd+ " BranchRelaxer -s "+ str(seed) + " "+ gTree+".pruned.tree " +"IIDGamma "+ str(k)+ " "+ str(theta) +" -o " +brGTree, shell=(sys.platform!="win32"), stdout=logfile, stderr=logfile)
            subprocess.call("java -jar "+cmd+ " BranchRelaxer -x -innms -s "+ str(seed) + " "+ gTree+".pruned.tree " +"IIDGamma "+ str(k)+ " "+ str(theta) +" -o " +brGTree+".no.primeid", shell=(sys.platform!="win32"), stdout=logfile, stderr=logfile)
            # for constant rates
            #subprocess.call("java -jar "+cmd+ " BranchRelaxer -s "+ str(seed) + " "+ gTree+".pruned.tree " +"Constant "+ str(1)+" -o " +brGTree, shell=(sys.platform!="win32"), stdout=logfile, stderr=logfile)
            #subprocess.call("java -jar "+cmd+ " BranchRelaxer -x -innms -s "+ str(seed) + " "+ gTree+".pruned.tree " +"Constant "+ str(1)+" -o " +brGTree+".no.primeid", shell=(sys.platform!="win32"), stdout=logfile, stderr=logfile)
            
        except IOError, e:
            print ("Function: generateGTreesAndAlignmets: %s " % e)
        print "--> Branch Relaxation ends..."
        
    else:
        print ("generateGTreesAndAlignmets: Error: Path to JPrIme.jar is not set ") 
        sys.exit()
        
        
    cmd= Where('seq-gen')
    if cmd != None:
        seed += 11
        subprocess.call(cmd+ " -m " + model +" -z "+ str(seed) + " -l " + str(length) + " < "+ brGTree +" > "+ work_dir+"/"+outFile+".phylip", shell=(sys.platform!="win32"), stdout=logfile, stderr=logfile)
        
    else:
        print ("generateGTreesAndAlignmets: Error: Path to seq-gen is not set ") 
        sys.exit()


############################################################################        
def main(argv):
    parser = argparse.ArgumentParser(description="Parse input arguments and print output. NOTE: you need to export poath to jprime jar file and seq-gen exe.")
    parser.add_argument('-stree', metavar='speciesTree' ,type=str, help='Specify path to the species tree file. ')
    parser.add_argument('-j', metavar='jprime' ,type=str, help='Specify the name of the jprime jar file i.e. jprime-0.3.5.jar.')
    parser.add_argument('-d', metavar='dup' ,type=float, help='Specify duplication rate.default=0.5', default=0.5)
    parser.add_argument('-l', metavar='loss' ,type=float, help='Specify loss rate.default=0.5', default=0.5)
    parser.add_argument('-L', metavar='length', type=int, help='Sequence length', default=1000)
    parser.add_argument('-tr', metavar='trans' ,type=float, help='Specify transfer rate.default=0.5', default=0.5)
    parser.add_argument('-O', metavar='outdir' ,type=str, help='Specify path to the output directory. ')
    parser.add_argument('-p', metavar='prefix', type=str, help='Prefix for output files. An counter will be added to the prefix, like "_17",  and then follows other info.')
    parser.add_argument('-k', metavar='shape' ,type=float, help='Specify Shape parameter for IIDGamma distribution for branch relaxation.', default=2.0)
    parser.add_argument('-t', metavar='theta' ,type=float, help='Specify Theta parameter for IIDGamma distribution for branch relaxation.', default=0.5)
    parser.add_argument('-m', metavar='minper', type=int, help='Required number of genes for each extant species', default=1)
    parser.add_argument('-M', metavar='model', type=str, help='Model of sequence evolution. See seq-gen documentation! Examples: JTT (proteins) and HKY (DNA)', default='JTT')
    parser.add_argument('-n', metavar='ntrees' ,type=int, help='Specify the number of gene trees to be generated', default=100)
    parser.add_argument('-s', metavar='seed' ,type=int, help='Specify seed. default=121', default=121)

    args = parser.parse_args()
    
    sTree = args.stree
    workDir = args.O
    prefix = args.p
    k = args.k
    theta = args.t
    model = args.M
    minper = args.m
    nTrees = args.n
    seed= args.s
    dup= args.d
    loss= args.l
    length = args.L
    trans= args.tr
    jarFileName= args.j
    seed= args.s
    
    
    
#    # Fixed parameters 1/T i.e 1/200 MYA
#    dup     = 0.005
#    loss    = 0.005
#    trans   = 0.0
    
#    # Fixed parameters 1/T i.e 1/180 MYA
#    dup     = 0.0055
#    loss    = 0.0055
#    trans   = 0.0
    
    # Fixed parameters for species tree scaled to 1
#    dup     = 0.5
#    loss    = 0.5
#    trans   = 0.0
    
    if workDir == None:
        workDir=tempfile.mkdtemp()
    elif os.path.exists(workDir) == False:
        os.mkdir(workDir)

    if prefix == None:
        prefix = ""
        
    with open(workDir+"/gfi.simulation."+str((datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-h%H-m%M-s%S')))+".info", 'w') as wf:
        wf.write("Jar File: %s\n" %(jarFileName))
        wf.write("Directory: %s\n" %(workDir))
        wf.write("Species tree: %s\n" %(sTree))
        wf.write("IIDGamma paramenter K: %f\n" %(k))
        wf.write("IIDGamma paramenter Theta: %f\n" %(theta))
        wf.write("Total gene tree: %d\n" %(nTrees))
        wf.write("Initial Seed: %d\n" %(seed))
        wf.write("Duplication rate: %f\n" %(dup))
        wf.write("Loss rate: %f\n" %(loss))
        wf.write("Trans rate: %f\n" %(trans))
        wf.write("Sequence length: %d\n" %(length))
        wf.write("Model: " + model)
        
    print "-->Simulation starts"
    for i in xrange(1, nTrees+1):
        seed += 11
        logfilename = os.path.join(workDir, str(i) + ".log")
        try:
            with open(logfilename, "w") as logfile:
                generateGTreesAndAlignmets(workDir, str(i), sTree, seed, dup, trans, loss, length, model, theta, k, minper, jarFileName, logfile)
                print "-->Simulation Done"
        except Exception as e:
            print str(e)
            exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])
