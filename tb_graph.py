# input week_means={"Monday": 12034, "Tuesday": 6789}

def histogram(data):

    max_value = max(data.values())
    longest_label = len(max(data.keys()))

    for label, value in data.items():

        bar = '█'*int(value*40/max_value)
        label_adjust = label + " "*(longest_label - len(label))
        
        print(label_adjust+': '+bar+"  "+str(value))
