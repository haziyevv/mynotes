1. How to add xlabel and ylabel and title to a plot ?

```
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("plot showing some results")
```

2. How to add a legend ?

```
Plotları yaradanda label argumentine ad ver ve sonda da plt.legend çağır

plt.plot(x, y1, label="Birinci")
plt.plot(x, y2, label="İkinci")

plt.legend()
```

3. How to apply different plot style ?

```
- plt.style.available --> this will show available styles
- plt.use(stylename) -->
```

4. How to apply comics style graph ?

```
- plt.xkcd()
```

5. How to make a bar to be transparent with respect to other bar ?

```
plt.bar(d_index, dev_y, color="blue", zorder=3, label="All dev")
plt.bar(d_index, pydev_y, color="green",zorder=1, label="Python dev")
plt.bar(d_index, jdev_y, color="red", zorder=2, label="Javascript dev")


- giving higher zorder value makes the bar less transparent. 
```

<img title="" src="file:///home/haziyevv/Documents/mynotes/figures/bars_zorder.png" alt="" width="377">

6. How to make side by side barcharts in a figure ? 
- Define the **width** parameter and then change each bar with that value

```
width=0.25
plt.bar(d_index-width, dev_y, color="blue", width=width, label="All dev")
plt.bar(d_index, pydev_y, color="green", width=width, label="Python dev")
plt.bar(d_index+width, jdev_y, color="red", width=width, label="Javascript dev")
```

7. How to make horizontal barchart ?

```
plt.barh() instead of plt.bar()
```

8. How to make pie chart ?

```
slices = [59249, 55466, 47544, 36443, 35917]
labels  ["JS", "HTML", "SQL", "Python", "Java"]

explode = [0, 0, 0, 0.1, 0]
plt.pie(slices, labels=labels, explode=explode,
        shadow=True, wedgeprops={"edgecolor":"black"}, 
        explode=explode, autopct="%1.1f%%")
```

explode --> if you want to crop a class from others

wedgeprops --> to add border between classes

shadow --> to put shadow

autopct --> to add percentages

9. How to make histogram ?

```
plt.hist(ages, edgecolor="black", 
         bins=bins, log=True)

plt.axvline(median_age, color="#EF7C8E", label="Age Median")
plt.title("Distribution of ages in Survey")
plt.xlabel("Age")
plt.ylabel("Total Respondends")
plt.legend()
plt.tight_layout()
```

axvline --> to draw vertical line

10. How to make scatterplot to see correlation between variables ? 

```
plt.scatter(counts, likes, c=ratios, cmap="copper",
            alpha=0.75, edgecolor="black", linewidth=1)

cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")

plt.xscale("log")
plt.yscale("log")

plt.title("Trending Youtube Videos")
plt.xlabel("View Count")
plt.ylabel("Total Likes")

plt.tight_layout()
```

**cbar** --> colorbar near the figure

**.xscale** --> to scale x

**.yscale** --> to scale y

**alpha** --> brightness of the color of the dots

**c** --> colors

**cmap** --> type of the color map

<img title="" src="figures/scatter.png" alt="">

We can also change the radius of the dots for a column :

```
plt.scatter(counts, likes, s=follower_size, c=ratios, cmap="copper",
            alpha=0.75, edgecolor="black", linewidth=1)


```

Here s=follower\_size, will change the sizes of the dots according to the follower size.
