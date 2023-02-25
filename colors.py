# Create a list of colors from comma-separated color names entered by user. Display first and last colors.
color=input("enter the color")
print(color)
color_list=color.split(',')
print(color_list)
print(color_list[0])
print(color_list[-1])
