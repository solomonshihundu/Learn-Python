#prompt user to enter number of blocks
blocks = int(input("Enter the number of blocks: "))

#var to store hieght of the pyramid 
height = 0

#keeps track of blocks needed per layer
inlayer = 1

#checks if we still have enough blocks to build
#a complete layer
while inlayer <= blocks:

    #increase hieght by one every time we build a complete
    #layer
    height += 1

    #reduce the number of available blocks
    #everytime a layer is complete,by the
    #number of blocks used in that layer
    blocks -= inlayer

    #increase number of blocks used by one each time layer
    #is complete
    inlayer += 1

print("The height of the pyramid: ", height)
