import numpy as np

def calculate(list):
    try:
        if(len(list) == 9):
            pass
        else:
            raise ValueError
            
    except ValueError:
        print("List must contain nine numbers.")
      
    list = np.array(list)
    arr = list.reshape((3, 3))
    mean_axis0 = np.mean(arr, axis=0)
    mean_axis1 = np.mean(arr, axis=1)
    mean_flattended = np.mean(arr)
    print(mean_axis0)
    print(mean_axis1)
    print(mean_flattended)
    
    var_axis0 = np.var(arr, axis=0)
    var_axis1 = np.var(arr, axis=1)
    var_flattended = np.var(arr)
    print(var_axis0)
    print(var_axis1)
    print(var_flattended)
    
    std_axis0 = np.std(arr, axis=0)
    std_axis1 = np.std(arr, axis=1)
    std_flattended = np.std(arr)
    print(std_axis0)
    print(std_axis1)
    print(std_flattended)
    
    min_axis0 = np.min(arr, axis=0)
    min_axis1 = np.min(arr, axis=1)
    min_flattended = np.min(arr)
    print(min_axis0)
    print(min_axis1)
    print(min_flattended)
    
    max_axis0 = np.max(arr, axis=0)
    max_axis1 = np.max(arr, axis=1)
    max_flattended = np.max(arr)
    print(max_axis0)
    print(max_axis1)
    print(max_flattended)
    
    sum_axis0 = np.sum(arr, axis=0)
    sum_axis1 = np.sum(arr, axis=1)
    sum_flattended = np.sum(arr)
    print(sum_axis0)
    print(sum_axis1)
    print(sum_flattended)
    
    calculations = {
      'mean': [mean_axis0.tolist(), mean_axis1.tolist(), mean_flattended.tolist()],
      'variance': [var_axis0.tolist(), var_axis1.tolist(), var_flattended.tolist()],
      'standard deviation': [std_axis0.tolist(), std_axis1.tolist(), std_flattended.tolist()],
      'max': [max_axis0.tolist(), max_axis1.tolist(), max_flattended.tolist()],
      'min': [min_axis0.tolist(), min_axis1.tolist(), min_flattended.tolist()],
      'sum': [sum_axis0.tolist(), sum_axis1.tolist(), sum_flattended.tolist()]
    }
    
    return calculations
