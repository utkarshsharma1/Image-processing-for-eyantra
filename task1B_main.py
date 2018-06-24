#classes and subclasses to import
import cv2
import numpy as np
import os

#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#subroutine to write rerults to a csv
def writecsv(color,shape,size,count):
    #open csv file in append mode
    filep = open('results1B_eYRC#5220.csv','a')
    # create string data to write per image
    datastr = "," + color + "-" + shape + "-" + size + "-" + str(count)
    #write to csv
    filep.write(datastr)
    filep.close()




def main(path):
#####################################################################################################
    #Write your code here!!!
#####################################################################################################
    img = cv2.imread(fp)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    canny = cv2.Canny(img,100,200)
    def medianCanny(img, thresh1, thresh2):
        median = np.median(img)
        img = cv2.Canny(img, int(thresh1 * median), int(thresh2 * median))
        return img
 
    ret, thresh = cv2.threshold(canny, 250, 255, cv2.THRESH_BINARY)
    _, contours ,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    area = 0
    size = []
    color = []
    shape = []
    cv2.drawContours(img,contours,-1,(110,110,110),3)
    cnt = []
    maxlength = max(map(len, contours))
    for i, contour in enumerate(contours):
        contour = np.array(contour, dtype = np.int32)
        cnt.append(contour)

    cnts = np.array(cnt)
    count = 1
    match = []
    for p in range (0, 60):
        match.append(0)
    cnts = []
    cx = []
    cy = []
    cys = []
    same = 0
    for i in cnt:
        if count%2==1:
            cnts.append(i)
        count += 1
    i = 0  
    for s in cnts:

        M = cv2.moments(s)
        cx.append(int(M['m10']/M['m00']))
        cy.append(int(M['m01']/M['m00']))
        peri = cv2.arcLength(s, True)
        area = cv2.contourArea(s)
        approx = cv2.approxPolyDP(s, 0.04 * peri, True)
        

    
        if len(approx) == 3:
            shape.append("triangle")
          ##  radius = int (peri/ 3)
          ##  radius = int (radius/ np.sqrt(3))
          ##  cys = int (cy + (radius/2) - 5)
            cys.append(cy[i])
            if ( area >= area2[7]):
                size.append("large")
            elif ( area <= area2[8]):
                size.append("small")
            else:
                size.append("medium")

        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            cys.append(( cy[i] + (h/2) -5))
            if ar >= 0.95 and ar <= 1.05:
                shape.append("square")
                if ( area >= area2[5]):
                    size.append("large")
                elif ( area <= area2[6]):
                    size.append("small")
                else:
                    size.append("medium")
                    
            else:
                shape.append("rectangle")
                if ( area >= area2[3]):
                    size.append("large")
                elif ( area <= area2[4]):
                    size.append("small")
                else:
                    size.append("medium")

        elif len(approx) == 5:
            shape.append("pentagon")

        else:
            shape.append("circle")
            radius = np.sqrt( 4 * area/np.pi)/2
            cys.append(int ( cy[i] + radius - 5))
            if ( area >= area2[1]):
                size.append("large")
            elif ( area <= area2[2]):
                size.append("small")
            else:
                size.append("medium")

     
        if np.all( img[ cys[i], cx[i]] == [255 , 0, 0]):
            color.append("Blue")
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    match[0] += 1
                elif (size[i] == "medium"):
                    match[1] += 1
                elif (size[i] == "large"):
                    match[2] += 1
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    match[3] += 1
                elif (size[i] == "medium"):
                    match[4] += 1
                elif (size[i] == "large"):
                    match[5] += 1
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    match[6] += 1
                elif (size[i] == "medium"):
                    match[7] += 1
                elif (size[i] == "large"):
                    match[8] += 1
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    match[9] += 1
                elif (size[i] == "medium"):
                    match[10] += 1
                elif (size[i] == "large"):
                    match[11] += 1
        elif np.all( img[ cys[i], cx[i]] == [ 0, 255, 0]):
            color.append("Green")
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    match[12] += 1
                elif (size[i] == "medium"):
                    match[13] += 1
                elif (size[i] == "large"):
                    match[14] += 1
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    match[15] += 1
                elif (size[i] == "medium"):
                    match[16] += 1
                elif (size[i] == "large"):
                    match[17] += 1
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    match[18] += 1
                elif (size[i] == "medium"):
                    match[19] += 1
                elif (size[i] == "large"):
                    match[20] += 1
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    match[21] += 1
                elif (size[i] == "medium"):
                    match[22] += 1
                elif (size[i] == "large"):
                    match[23] += 1
        elif np.all( img[ cys[i], cx[i]] == [ 0, 0, 255]):
            color.append("Red")
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    match[24] += 1
                elif (size[i] == "medium"):
                    match[25] += 1
                elif (size[i] == "large"):
                    match[26] += 1
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    match[27] += 1
                elif (size[i] == "medium"):
                    match[28] += 1
                elif (size[i] == "large"):
                    match[29] += 1
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    match[30] += 1
                elif (size[i] == "medium"):
                    match[31] += 1
                elif (size[i] == "large"):
                    match[32] += 1
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    match[33] += 1
                elif (size[i] == "medium"):
                    match[34] += 1
                elif (size[i] == "large"):
                    match[35] += 1
        elif (np.all( img[ cys[i], cx[i]] == [ 0, 140, 255])| np.all( img[ cys[i], cx[i]] == [ 0, 150, 255])):
            color.append("Orange")
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    match[36] += 1
                elif (size[i] == "medium"):
                    match[37] += 1
                elif (size[i] == "large"):
                    match[38] += 1
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    match[39] += 1
                elif (size[i] == "medium"):
                    match[40] += 1
                elif (size[i] == "large"):
                    match[41] += 1
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    match[42] += 1
                elif (size[i] == "medium"):
                    match[43] += 1
                elif (size[i] == "large"):
                    match[44] += 1
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    match[45] += 1
                elif (size[i] == "medium"):
                    match[46] += 1
                elif (size[i] == "large"):
                    match[47] += 1
        elif np.all( img[ cys[i], cx[i]] == [ 0, 150, 255]):
            color.append("Orange")
            
        elif np.all( img[ cys[i], cx[i]] == [ 0, 255, 255]):
            color.append("Yellow")
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    match[48] += 1
                elif (size[i] == "medium"):
                    match[49] += 1
                elif (size[i] == "large"):
                    match[50] += 1
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    match[51] += 1
                elif (size[i] == "medium"):
                    match[52] += 1
                elif (size[i] == "large"):
                    match[53] += 1
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    match[54] += 1
                elif (size[i] == "medium"):
                    match[55] += 1
                elif (size[i] == "large"):
                    match[56] += 1
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    match[57] += 1
                elif (size[i] == "medium"):
                    match[58] += 1
                elif (size[i] == "large"):
                    match[59] += 1
                
        else:
            color.append(" ")
        i += 1
    if len(contours) == 0:
        print "There are no shapes"


    for i in range (0, (len(contours)/2) ):
        if (color[i] == "Blue"):
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    same = match[0]
                elif (size[i] == "medium"):
                    same = match[1]
                elif (size[i] == "large"):
                    same = match[2]
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    same = match[3]
                elif (size[i] == "medium"):
                    same = match[4]
                elif (size[i] == "large"):
                    same = match[5]
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    same = match[6]
                elif (size[i] == "medium"):
                    same = match[7]
                elif (size[i] == "large"):
                    same = match[8]
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    same = match[9]
                elif (size[i] == "medium"):
                    same = match[10]
                elif (size[i] == "large"):
                    same = match[11]
        elif(color[i] =="Green"):
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    same = match[12]
                elif (size[i] == "medium"):
                    same = match[13]
                elif (size[i] == "large"):
                    same = match[14]
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    same = match[15]
                elif (size[i] == "medium"):
                    same = match[16]
                elif (size[i] == "large"):
                    same = match[17]
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    same = match[18]
                elif (size[i] == "medium"):
                    same = match[19]
                elif (size[i] == "large"):
                    same = match[20]
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    same = match[21]
                elif (size[i] == "medium"):
                    same = match[22]
                elif (size[i] == "large"):
                    same = match[23]
        elif(color[i] =="Red"):
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    same = match[24]
                elif (size[i] == "medium"):
                    same = match[25]
                elif (size[i] == "large"):
                    same = match[26]
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    same = match[27]
                elif (size[i] == "medium"):
                    same = match[28]
                elif (size[i] == "large"):
                    same = match[29]
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    same = match[30]
                elif (size[i] == "medium"):
                    same = match[31]
                elif (size[i] == "large"):
                    same = match[32]
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    same = match[33]
                elif (size[i] == "medium"):
                    same = match[34]
                elif (size[i] == "large"):
                    same = match[35]
        elif(color[i] =="Orange"):
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    same = match[36]
                elif (size[i] == "medium"):
                    same = match[37]
                elif (size[i] == "large"):
                    same = match[38]
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    same = match[39]
                elif (size[i] == "medium"):
                    same = match[40]
                elif (size[i] == "large"):
                    same = match[41]
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    same = match[42]
                elif (size[i] == "medium"):
                    same = match[43]
                elif (size[i] == "large"):
                    same = match[44]
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    same = match[45]
                elif (size[i] == "medium"):
                    same = match[46]
                elif (size[i] == "large"):
                    same = match[47]
        elif(color[i] =="Yellow"):
            if (shape[i] == "triangle"):
                if (size[i] == "small"):
                    same = match[48]
                elif (size[i] == "medium"):
                    same = match[49]
                elif (size[i] == "large"):
                    same = match[50]
            elif (shape[i] == "rectangle"):
                if (size[i] == "small"):
                    same = match[51]
                elif (size[i] == "medium"):
                    same = match[52]
                elif (size[i] == "large"):
                    same = match[53]
            elif (shape[i] == "square"):
                if (size[i] == "small"):
                    same = match[54]
                elif (size[i] == "medium"):
                    same = match[55]
                elif (size[i] == "large"):
                    same = match[56]
            elif (shape[i] == "circle"):
                if (size[i] == "small"):
                    same = match[57]
                elif (size[i] == "medium"):
                    same = match[58]
                elif (size[i] == "large"):
                    same = match[59]
    
        cv2.putText(img, str(color[i]) + " " + str(shape[i]) + " " + str(size[i]) , (cx[i], cy[i]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 10, 10), 2)
        writecsv(str(color[i]), str(shape[i]) , str(size[i]), str(same))
        
    cv2.imwrite('output' + fp[6] + '.png', img)



#################################################################################################
# DO NOT EDIT!!!
#################################################################################################





#main where the path is set for the directory containing the test images
if __name__ == "__main__":
    area2 = [0]
    mypath1 = 'Sample Images\.'
    onlyfiles1 = [os.path.join(mypath1, f) for f in os.listdir(mypath1) if f.endswith(".png")]
    for fp1 in onlyfiles1:
        img1 = cv2.imread(fp1)
        gray = cv2.cvtColor(img1 ,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray,240,255,4)
        _,contours1,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img1 ,contours1,-1,(0,255,0),3)
        cv2.drawContours(img1,contours1,-1,(110,110,110),3)        
        area1 = cv2.contourArea(contours1[0])
        area2.append(area1)

    
    mypath = '.'
#getting all files in the directory
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if f.endswith(".png")]
        #iterate over each file in the directory
    for fp in onlyfiles:
    #Open the csv to write in append mode
        filep = open('results1B_eYRC#5220.csv','a')
    #this csv will later be used to save processed data, thus write the file name of the image 
        filep.write(fp)
            #close the file so that it can be reopened again later
        filep.close()
            #process the image
        data = main(fp)
        print data
            #open the csv
        filep = open('results1B_eYRC#5220.csv','a')
            #make a newline entry so that the next image data is written on a newline
        filep.write('\n')
            #close the file
        filep.close()
