#minimize.py

def center(velocity,intensity,param,startline,endline,steplist):
    totallines=endline-startline+1
    sumtermsarray=[0];sumterms=[0]
    centerA=param[0];coefficientA=param[1];sigmaA=param[2]
    step=steplist[0];max_passes=steplist[1]
    for i in range(max_passes):   #create an empty array for sumterms
        sumterms.append(0)
    for i in range(max_passes):
        gaussAA=[0]
        pass_no=i+1
        for j in range(totallines):
            #calculate gaussian function
            exponentA=(-1*(velocity[j]-centerA)**2)/(2*sigmaA**2)
            gaussA=coefficientA*(2.718**exponentA)
            gaussAA.append(gaussA)
            #calculate least sum of squares
            termdiff=(intensity[j]-gaussA)**2
            sumtermsarray.append(termdiff)
        sumterms[i]=sum(sumtermsarray)
        if i==0:
            dir=+1 #start adding    
            centerA=centerA+dir*step
            sumtermsarray=[0]
            continue                        
        if i>0 and sumterms[i]==sumterms[i-1]:
            break              #No change. Leave the i loop and print results
        if i>0 and dir==1 and sumterms[i]<sumterms[i-1]:
            dir=+1 #keep adding
            centerA=centerA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==1 and sumterms[i]>sumterms[i-1]: 
            dir=-1 #start subtracting
            centerA=centerA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]        
            continue
        if i>0 and dir==-1 and sumterms[i]<sumterms[i-1]:
            dir=-1 #keep subtracting
            centerA=centerA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==-1 and sumterms[i]>sumterms[i-1]:
            dir=+1 #start adding
            centerA=centerA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]
            continue
    gaussAA[0]=gaussAA[1]   
    #print("Number of passes: center ",pass_no)
    #print("sumterms ",int(sumterms[i]))
    #print("Center value ", int(centerA), " Hz")
    #print("parameters ", temp_param)
    return centerA,int(sumterms[i])

def coef(velocity,intensity,param,startline,endline,steplist):
    totallines=endline-startline+1
    sumtermsarray=[0];sumterms=[0]
    centerA=param[0];coefficientA=param[1];sigmaA=param[2]
    step=steplist[2]; max_passes=steplist[3]
    for i in range(max_passes): 
        sumterms.append(0)
    for i in range(max_passes):
        gaussAA=[0]
        pass_no=i+1
        for j in range(totallines):
            #calculate gaussian function
            exponentA=(-1*(velocity[j]-centerA)**2)/(2*sigmaA**2)
            gaussA=coefficientA*(2.718**exponentA)
            gaussAA.append(gaussA)
            #calculate least sum of squares
            termdiff=(intensity[j]-gaussA)**2
            sumtermsarray.append(termdiff)
        sumterms[i]=sum(sumtermsarray)
        if i==0:
            dir=+1 #start adding    
            coefficientA=coefficientA+dir*step
            sumtermsarray=[0]
            continue                        
        if i>0 and sumterms[i]==sumterms[i-1]: #no change
            break              #leave the i loop and print results
        if i>0 and dir==1 and sumterms[i]<sumterms[i-1]:
            dir=+1 #keep adding
            coefficientA=coefficientA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==1 and sumterms[i]>sumterms[i-1]: 
            dir=-1 #start subtracting
            coefficientA=coefficientA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]        
            continue
        if i>0 and dir==-1 and sumterms[i]<sumterms[i-1]:
            dir=-1 #keep subtracting
            coefficientA=coefficientA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==-1 and sumterms[i]>sumterms[i-1]:
            dir=+1 #start adding
            coefficientA=coefficientA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]
            continue
    gaussAA[0]=gaussAA[1]    
    #print("Number of passes: coefficient ",pass_no)
    #print("sumterms ",int(sumterms[i]))
    #print("Coefficient value ", coefficientA, " Kelvins")
    #print("parameters ", temp_param)
    return coefficientA,int(sumterms[i])

def sigma(velocity,intensity,param,startline,endline,steplist):
    totallines=endline-startline+1
    sumtermsarray=[0];sumterms=[0]
    centerA=param[0];coefficientA=param[1];sigmaA=param[2]
    step=steplist[4];max_passes=steplist[5]
    for i in range(max_passes): 
        sumterms.append(0)
    for i in range(max_passes):
        gaussAA=[0]
        pass_no=i+1
        for j in range(totallines):
            #calculate gaussian function
            exponentA=(-1*(velocity[j]-centerA)**2)/(2*sigmaA**2)
            gaussA=coefficientA*(2.718**exponentA)
            gaussAA.append(gaussA)
            #calculate least sum of squares
            termdiff=(intensity[j]-gaussA)**2
            sumtermsarray.append(termdiff)
        sumterms[i]=sum(sumtermsarray)
        if i==0:
            dir=+1 #start adding    
            sigmaA=sigmaA+dir*step
            sumtermsarray=[0]
            continue                        
        if i>0 and sumterms[i]==sumterms[i-1]: #no change
            break              #leave the i loop and print results
        if i>0 and dir==1 and sumterms[i]<sumterms[i-1]:
            dir=+1 #keep adding
            sigmaA=sigmaA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==1 and sumterms[i]>sumterms[i-1]: 
            dir=-1 #start subtracting
            sigmaA=sigmaA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]        
            continue
        if i>0 and dir==-1 and sumterms[i]<sumterms[i-1]:
            dir=-1 #keep subtracting
            sigmaA=sigmaA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==-1 and sumterms[i]>sumterms[i-1]:
            dir=+1 #start adding
            sigmaA=sigmaA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]
            continue
    gaussAA[0]=gaussAA[1] 
    #print("Number of passes: sigma ",pass_no)
    #print("sumterms ",int(sumterms[i]))
    #print("Sigma value ", int(sigmaA), " Hz")
    #print("parameters ", temp_param)
    return sigmaA,int(sumterms[i])
