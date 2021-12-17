import pandas as pd

squirrel_data = pd.read_csv("Squirrel_Data.csv")
# print(squirrel_data)
all_colors = squirrel_data["Primary Fur Color"].unique()
color_list = []
count = []
for i in range(1, 4):
	new_color = squirrel_data[squirrel_data["Primary Fur Color"] == all_colors[i]]
	color_list.append(all_colors[i])
	count.append(new_color["Primary Fur Color"].count())
data_dict = {
	"Fur Color": ["Gray", "Cinnamon", "Black"],
	"Count": count
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)
