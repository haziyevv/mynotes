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



7. 





1. 

2. To run inline in jupyter notebook:

```
%matplotlib inline
```

2. To put the x and y axis to a range:

```
plt.ylim([-1, 1])
```

Like this y axis will be in range -1 to 1

3. To add grid lines:

```
plt.grid()
```

4. 
