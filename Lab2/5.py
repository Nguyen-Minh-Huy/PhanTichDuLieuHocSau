
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
file_path = '/mnt/data/processed_dulieuxettuyendaihoc.csv'
data = pd.read_csv(file_path)

# Mô tả độ tập trung và phân tán của dữ liệu T1
T1 = data['T1']
description = T1.describe()
mean = T1.mean()
median = T1.median()
variance = T1.var()
std_dev = T1.std()
min_value = T1.min()
max_value = T1.max()

print("Mô tả thống kê cho biến T1:")
print(description)
print(f"Trung bình: {mean}")
print(f"Trung vị: {median}")
print(f"Phương sai: {variance}")
print(f"Độ lệch chuẩn: {std_dev}")
print(f"Giá trị nhỏ nhất: {min_value}")
print(f"Giá trị lớn nhất: {max_value}")

# Vẽ biểu đồ Box-Plot và xác định các 10 đại lượng trong biểu đồ đó
plt.figure(figsize=(10, 5))
sns.boxplot(x=T1)
plt.title('Box Plot of T1')
plt.xlabel('T1')
plt.show()

# Mô tả hình dáng lệch của phân phối T1 dựa vào các đại lượng hướng tâm
if mean > median:
    skewness_description = "Phân phối lệch phải"
elif mean < median:
    skewness_description = "Phân phối lệch trái"
else:
    skewness_description = "Phân phối đối xứng"

print(f"Phân phối T1: {skewness_description}")

# Vẽ biểu đồ Histogram biểu thị hình dáng phân phối
plt.figure(figsize=(10, 5))
sns.histplot(T1, kde=True, bins=30)
plt.title('Histogram of T1')
plt.xlabel('T1')
plt.ylabel('Frequency')
plt.show()

# Mô tả các đặc trưng của phân phối, mức độ lệch và mức độ nhọn
skewness = T1.skew()
kurtosis = T1.kurt()

print(f"Độ lệch (Skewness) của T1: {skewness}")
print(f"Độ nhọn (Kurtosis) của T1: {kurtosis}")

# Kiểm chứng phân phối chuẩn QQ-Plot
plt.figure(figsize=(10, 5))
stats.probplot(T1, dist="norm", plot=plt)
plt.title('QQ Plot of T1')
plt.show()

# Nhận xét và đánh giá về phân phối của T1
print("Nhận xét:")
if skewness > 0:
    print("Phân phối của T1 lệch phải.")
elif skewness < 0:
    print("Phân phối của T1 lệch trái.")
else:
    print("Phân phối của T1 đối xứng.")

if kurtosis > 0:
    print("Phân phối của T1 có đỉnh nhọn hơn so với phân phối chuẩn.")
elif kurtosis < 0:
    print("Phân phối của T1 có đỉnh thấp hơn so với phân phối chuẩn.")
else:
    print("Phân phối của T1 có độ nhọn tương tự phân phối chuẩn.")
