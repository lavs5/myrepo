Install the complete tidyverse with a single line of code:
>install.packages("tidyverse")

If updates are available, and optionally install them, by running 
>tidyverse_update()

To use a library
>library(tidyverse)

If we need to be explicit about where a function (or dataset) comes from, we’ll use the special form package::function(). 
For example, ggplot2::ggplot() tells you explicitly that we’re using the ggplot() function from the ggplot2 package

create a plot
>ggplot(data = mpg) + 
    geom_point(mapping = aes(x = displ, y = hwy))

plot using colors for variables based on another variable
>ggplot(data = mpg) + 
    geom_point(mapping = aes(x = displ, y = hwy, color = class))

alpha aesthetic controls the transparency of the points
>ggplot(data = mpg) + 
    geom_point(mapping = aes(x = displ, y = hwy, alpha = class))

shape aesthetic controls the shape of the points
>ggplot(data = mpg) + 
    geom_point(mapping = aes(x = displ, y = hwy, shape = class))

single color to all points
>ggplot(data = mpg) + 
     geom_point(mapping = aes(x = displ, y = hwy), color = "blue")

smooth curve plot
>ggplot(data = mpg) + 
    geom_smooth(mapping = aes(x = displ, y = hwy))

Point and smooth curve
>ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) + 
    geom_point() +
    geom_smooth()

Bar chart
>ggplot(data = diamonds) + 
    geom_bar(mapping = aes(x = cut))

colored bar chart
>ggplot(data = diamonds) + 
    geom_bar(mapping = aes(x = cut, fill = cut))

colored stacked bar
>ggplot(data = diamonds) + 
    geom_bar(mapping = aes(x = cut, fill = clarity))

position = "dodge" places overlapping objects directly beside one another. This makes it easier to compare individual values.
>ggplot(data = diamonds) + 
    geom_bar(mapping = aes(x = cut, fill = clarity), position = "dodge")

Box plot
>ggplot(data = mpg, mapping = aes(x = class, y = hwy)) + 
    geom_boxplot()

Quick map
>nz <- map_data("nz")

>ggplot(nz, aes(long, lat, group = group)) +
  geom_polygon(fill = "white", colour = "black")

>ggplot(nz, aes(long, lat, group = group)) +
  geom_polygon(fill = "white", colour = "black") +
  coord_quickmap()