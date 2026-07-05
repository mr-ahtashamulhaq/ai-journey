import numpy as np

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Karachi Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Town
    [4, 180000, 210000, 240000, 270000],  # Burger O clock
    [5, 160000, 185000, 205000, 230000]   # Chai Station
])

print("==== Food Panda sales analysis ==== ")
print("\n Sales data shape", sales_data.shape)
print("\n Sample data for 1st 3 restau:\n",sales_data[:3])

print("\nTotal Sales per Year, combined all res: ", np.sum(sales_data[: , 1:], axis = 0))

# Minimum sale per resturant
min_sales = np.min(sales_data[:,1:], axis=1 )
print("min sales per resturant: ", min_sales)

# Maximum sales per year
max_sales = np.max(sales_data[:,1:], axis=0)
print("Max sales per year:", max_sales)

# Average sales per resturant
avg_sales = np.mean(sales_data[:,1:], axis= 1)
print("Average Sales : ", avg_sales)


# VECTORIZE = operation on each element of matrix
restaurant_types = np.array(['biryani', 'chinese', 'pizza', 'burger', 'cafe'])
vectorized_upper = np.vectorize(str.upper)
print("\n\nVectorized Upper",vectorized_upper(restaurant_types))
