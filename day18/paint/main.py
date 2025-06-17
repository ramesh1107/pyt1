import colorgram

colors = colorgram.extract('img.jpg',30)
f_c= colors[0]
rgb = f_c.rgb

print(rgb)
