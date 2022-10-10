from collections import Counter
import math
import scipy.stats as ss

def conditional_entropy(x, y):
    y_counter = Counter(y)
    xy_counter = Counter(list(zip(x, y)))
    total_occurrences = sum(y_counter.values())
    entropy = 0
    for xy in xy_counter.keys():
        p_xy = xy_counter[xy] / total_occurrences
        p_y = y_counter[xy[1]] / total_occurrences
        entropy += p_xy * math.log(p_y / p_xy)
    return entropy

def theils_u(x, y):
    s_xy = conditional_entropy(x, y)
    x_counter = Counter(x)
    total_occurrences = sum(x_counter.values())
    p_x = list(map(lambda n: n/total_occurrences, x_counter.values()))
    s_x = ss.entropy(p_x)
    if s_x == 0:
        return 1
    else:
        return (s_x - s_xy) / s_x

def correlation_ratio(categories, measurements):
    measurements = np.array(measurements)
    fcat, _ = pd.factorize(categories)
    cat_num = np.max(fcat)+1
    y_avg_array = np.zeros(cat_num)
    n_array = np.zeros(cat_num)
    for i in range(0,cat_num):
        cat_measures = measurements[np.argwhere(fcat == i).flatten()]
        n_array[i] = len(cat_measures)
        y_avg_array[i] = np.average(cat_measures)
    y_total_avg = np.sum(np.multiply(y_avg_array,n_array))/np.sum(n_array)
    numerator = np.sum(np.multiply(n_array,np.power(np.subtract(y_avg_array,y_total_avg),2)))
    denominator = np.sum(np.power(np.subtract(measurements,y_total_avg),2))
    if numerator == 0:
        eta = 0
    else:
        eta = np.sqrt(numerator/denominator)
    return eta

# dtype object 아닌 경우는 다 continuous라는 가정 하에
mat = pd.DataFrame(index=data.columns, columns=data.columns)
for i in range(len(mat.columns)):
    for j in range(len(mat.columns)):
        if (data[mat.columns[i]].dtype != "object") & (data[mat.columns[j]].dtype != "object"):
            mat.iloc[i, j] = data[mat.columns[i]].corr(data[mat.columns[j]])
        elif (data[mat.columns[i]].dtype == "object") & (data[mat.columns[j]].dtype == "object"):
            mat.iloc[i, j] = theils_u(data[mat.columns[i]], data[mat.columns[j]])
        elif (data[mat.columns[i]].dtype == "object") & (data[mat.columns[j]].dtype != "object"):
            mat.iloc[i, j] = correlation_ratio(data[mat.columns[i]], data[mat.columns[j]])
        elif (data[mat.columns[i]].dtype != "object") & (data[mat.columns[j]].dtype == "object"):
            mat.iloc[i, j] = correlation_ratio(data[mat.columns[i]], data[mat.columns[j]])
