

def Weights (Number_layer, Number_Mix_Per_Layer):
    probability = []
    for i in range(Number_layer):
        probabTem = []
        for j in range(Number_Mix_Per_Layer):
            probabTem.append((1) / (Number_Mix_Per_Layer))
        probability.append(probabTem)
    return probability


