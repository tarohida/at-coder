#static info
array = ['Sunny', 'Cloudy', 'Rainy', 'Sunny']

#input
weather = str(input())

#def
def predict_wether(weather):
    for k,s in enumerate(array):
        if weather == s:
            output = array[k+1]
            break

    return output

#main
print(predict_wether(weather))
