import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot
import matplotlib.image as mpimage

# massif = np.array([1,2,3])
# print(massif)

# massif = np.array([[1,2],[3,4]])
# print(massif)

# massif = np.array([[1,2],[3,4]])
# sum = np.sum(massif)
# print(sum)

# massif1 = np.array([1,2,3,4,5])
# massif2 = np.array([6,7,8,9,10])
# connected_massif = np.concatenate((massif1, massif2))
# print(connected_massif)

# random_numbers = np.random.random((2,2))
# print(random_numbers)

# random_numbers = np.random.randint(0,10, size = 5)
# print(random_numbers)

# massif = np.array([10,20,30,40,50])
# random_elements = np.random.choice(massif, size = 3)
# print(random_elements)

# massif = np.arange(0,10,2)
# print(massif)

# massif1 = np.array([1,3,5])
# massif2 = np.array([2,3,4])
# compare = massif1 > massif2
# print(compare)

# massif = np.array([1,2,3,4,5,6,7,8,9,10])
# filtered_array = massif[massif > 5]
# print(filtered_array)

# massif = np.array([1,2,3,4,5,6])
# split_array = np.split(massif, 2)
# print(split_array)

# array = np.array(np.arange(1,13)).reshape(4,3)
# print(array)

# array = np.array(np.arange(0,20)).reshape(5,4)
# df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D'])
# sum = df.groupby('A')['B'].sum()
# second_column = array[:, 1].sum()
# print(second_column)

# array = np.array(np.arange(0,20)).reshape(5,4)
# df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D'])
# sum = df.groupby('A')['B'].sum()
# second_column = array[:, 0] + array[:, 1]
# print(second_column)

# array = np.array(np.arange(0,20)).reshape(5,4)
# df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D'])
# sum = df.groupby('A')['B'].sum()
# second_column = np.sum(array[:, 1])
# print(second_column)

# threed_matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
# line_sum = np.sum(threed_matrix, axis = 1)
# column_sum = np.sum(threed_matrix, axis = 0)
# print(column_sum)

# threed_matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
# column_sum = np.sum(threed_matrix [1])
# print(column_sum)

# massif = np.array([0,1,2,3,4,5,6,7,8,9])
# filtered_array = massif[2:6]
# print(filtered_array)

# df = pd.DataFrame(np.random.randn(100,3), columns= ['1', '2', '3'])
# filtered_array = df[df["1"] > 0]
# print(filtered_array)

# df = pd.DataFrame({
#     "x": np.arange(1,6),
#     "y": np.arange(1,6)
# })
# df["xy_sum"] = df['x'] + df['y']
# print(df)

# df = pd.DataFrame({
#     "a": [1, np.nan, 3],
#     "b": [4,5, np.nan],
# })
# df.fillna(0, inplace=True)
# print(df)

# df = pd.DataFrame(columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
# line = np.random.rand(10)
# df.loc[len(df)] = line
# print(df)

# df.loc["nauja eilutė"] = ["reikšmės"]

# data = {
#     "age": [27, 17],
#     "city": ['mykonos', 'athens']
# }
# df = pd.DataFrame(data, index=['roberta', 'gertrūda'])
# df.loc['elžbieta'] = [7, "rhode"]
# # print(df)
#
# df.loc[df["age"] > 25, "city"] = "crete"
# print(df)

# matrix_ofones = np.ones([3,3])
# border_matrix = np.pad(matrix_ofones, pad_width=1, mode="constant", constant_values=0)
# print(border_matrix)

# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[5, 6], [7, 8]])
# c = np.add(matrix1,matrix2)
# print(c)

# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[5, 6], [7, 8]])
# multiple = np.matmul(matrix1,matrix2)
# print(multiple)

# prices = np.random.normal(100,10,100)
#
# def varying_average(data, tab):
#     va_filters = np.cumsum(data, dtype = float)
#     va_filters[tab:] = va_filters[tab:] - va_filters[:-tab]
#     return va_filters[tab -1:] /tab
#
# tab = 5
# va_prices = varying_average(prices, tab)
# plt.plot(prices, label = "original prices")
# plt.plot(np.arange(tab -1, len(prices)), va_prices, label = "varying average", color = "red")
# plt.legend()
# plt.title("financial data refinement by filtering varying average")
# plt.show()

# share_prices = pd.read_csv("all_stocks_5yr.csv")
# prices = np.array(share_prices["close"])
# prices_average = np.mean(share_prices["close"])
# prices_median = np.median(share_prices["close"])
# prices_stand = np.std(share_prices["close"])
#
# plt.figure(figsize = (14,5))
# plt.subplot(1, 4, 1)
# plt.plot(prices, label = "share prices")
# plt.legend()
# plt.title("share prices")
#
# plt.subplot(1, 4, 2)
# plt.plot([prices_average]*len(prices), label = "prices average")
# plt.legend()
# plt.title("prices average")
#
# plt.subplot(1, 4, 3)
# plt.plot([prices_median]*len(prices), label = "prices median")
# plt.legend()
# plt.title("prices median")
#
# plt.subplot(1, 4, 4)
# plt.plot([prices_stand]*len(prices), label = "prices stand")
# plt.legend()
# plt.title("prices stand")
#
# plt.show()

# zingsniu_skaicius = 1000
#
# x_zingsniai = np.random.choice([-1, 1], size=zingsniu_skaicius)
# y_zingsniai = np.random.choice([-1, 1], size=zingsniu_skaicius)
# z_zingsniai = np.random.choice([-1, 1], size=zingsniu_skaicius)
#
# x_trajektorija = np.cumsum(x_zingsniai)
# y_trajektorija = np.cumsum(y_zingsniai)
# z_trajektorija = np.cumsum(z_zingsniai)
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = "3d")
# ax.plot(x_trajektorija, y_trajektorija, z_trajektorija)
# ax.view_init(elev=20, azim=45)
# ax.set_title("atsitiktine trajektorija daleles judejimo erdveje")
# plt.show()

# originalus_vaizdas = mpimage.imread("Space-Background-Images-1600x1066.jpg")
# invertuotas_vaizdas = 255-originalus_vaizdas
# fig, ax = plt.subplots(1,2)
# ax[0].imshow(originalus_vaizdas)
# ax[0].set_title("originalus vaizdas")
# ax[0].axis("off")
# ax[1].imshow(invertuotas_vaizdas)
# ax[1].set_title("invertuotas vaizdas")
# ax[1].axis("off")
# plt.show()