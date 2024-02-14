# Intro to spatial analysis tutorial
# Satellite data available from https://scihub.copernicus.eu/

# Maude Grenier s0804311@ed.ac.uk
# 03-12-2018
##############################################################

# Set the working directory (example, replace with your own file path)
setwd("C:/Users/lavgo/Documents/GitHub/myrepo/rtutorials")

# Load packages

# If you haven't installed the packages before, use e.g.:
install.packages("sp")

library(sp)
library(rgdal)
library(raster)
library(ggplot2)
library(viridis)
library(rasterVis)

tay <- raster('taycrop.tif')
tay

b1<- raster('taycrop.tif',band=1)
b2 <- raster('taycrop.tif', band=2)
b3 <- raster('taycrop.tif', band=3)
b4 <- raster('taycrop.tif', band=4)
b5 <- raster('taycrop.tif', band=5)
b6 <- raster('taycrop.tif', band=6)
b7 <- raster('taycrop.tif', band=7)
b8 <- raster('taycrop.tif', band=8)
b9 <- raster('taycrop.tif', band=9)
b10 <- raster('taycrop.tif', band=10)
b11 <- raster('taycrop.tif', band=11)
b12 <- raster('taycrop.tif', band=12)

# check if band are same extent
compareRaster(b2,b3)

# reset margins
par("mar")
par(mar=c(1,1,1,1))

#plot vs. image, image stretches view
plot(b8)
image(b8)
zoom(b8)

# define extent and plot cropped image
plot(tay)
e <-drawExtent()
cropped_tay <- crop(b7, e)
plot(cropped_tay)

# plot band 8
image(b8, col= viridis_pal(option="D")(10), main="Sentinel 2 image of Loch Tay")
# close plot
dev.off()

#plot RGB composite
tayRGB <- stack(list(b4, b3, b2))              # creates raster stack
plotRGB(tayRGB, axes = TRUE, stretch = "lin", main = "Sentinel RGB colour composite")
png('False_tay.png', width = 5, height = 4, units = "in", res = 300)
dev.off()

#plot using gplot
gplot(b8) +
  geom_raster(aes(x = x, y = y, fill = value)) +
  # value is the specific value of reflectance
  scale_fill_viridis_c() +
  coord_quickmap() +
  ggtitle("West of Loch tay, raster plot") +
  xlab("Longitude") +
  ylab("Latitude") +
  # removes grey background
  theme_classic() +   					    
  # center plot title
  theme(plot.title = element_text(hjust = 0.5),             
        # font size
        text = element_text(size=11),		       	    
        # rotates x axis text
        axis.text.x = element_text(angle = 90, hjust = 1))  

ggsave("ggtay.png", scale = 1.5, dpi = 300) 	       
dev.off()

#visualize all bands
t <- stack(b1,b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12)

gplot(t)+
  geom_raster(aes(x=x,y=y,fill=value))+
  scale_fill_viridis_c()+
  facet_wrap(~variable) +
  coord_quickmap()+
  ggtitle("Sentinel 2 Loch tay, raster plots")+
  xlab("Long")+
  ylab("Lat")+
  theme_classic()+
  theme(text=element_text(size=11),
        axis.text.x=element_text(angle=90,hjust=1))+
  theme(plot.title = element_text(hjust=0.5))
dev.off()

s_tay <- brick('taycrop.tif')
plot(s_tay)
dev.off()


# NDVI

# Created a VI function (vegetation index)
VI <- function(img, k, i) {
  bk <- img[[k]]
  bi <- img[[i]]
  vi <- (bk - bi) / (bk + bi)
  return(vi)
}

# For Sentinel 2, the relevant bands to use are:
# NIR = 8, red = 4

ndvi <- VI(s_tay, 8, 4)
# 8 and 4 refer to the bands we'll use
plot(ndvi, col = rev(terrain.colors(10)), main = 'Sentinel 2, Loch Tay-NDVI')
dev.off()

# Create histogram of NDVI data

hist(ndvi,
     main = "Distribution of NDVI values",
     xlab = "NDVI",
     ylab= "Frequency",
     col = "aquamarine3",
     xlim = c(-0.5, 1),
     breaks = 30,
     xaxt = 'n')
axis(side = 1, at = seq(-0.5,1, 0.05), labels = seq(-0.5,1, 0.05))
dev.off()

# Mask cells that have NDVI of less than 0.4 (less likely to be vegetation)
veg <- reclassify(ndvi, cbind(-Inf, 0.4, NA))
# We are reclassifying our object and making all values between
# negative infinity and 0.4 be NAs

plot(veg, main = 'Veg cover')
dev.off()

writeRaster(x = ndvi,
              #file path
            filename="tay_ndvi_2018.tif", 	
              # save as a tif
            format = "GTiff",
            	# save as a INTEGER rather than a float
            datatype = 'INT2S') 				



# convert the raster to vector/matrix ('getValues' converts the RasterLAyer to array) )

nr <-getValues(ndvi)
str(nr)

# important to set the seed generator because `kmeans` initiates the centres in random locations
# the seed generator just generates random numbers

set.seed(99)

# create 10 clusters, allow 500 iterations, start with 5 random sets using 'Lloyd' method

kmncluster <- kmeans(na.omit(nr), centers = 10, iter.max = 500,
                     nstart = 5, algorithm = "Lloyd")

# kmeans returns an object of class 'kmeans'

str(kmncluster)


# First create a copy of the ndvi layer
knr <- ndvi

# Now replace raster cell values with kmncluster$cluster
# array
knr[] <- kmncluster$cluster

# Alternative way to achieve the same result
values(knr) <- kmncluster$cluster
knr

par(mfrow = c(1, 2))
plot(ndvi, col = rev(terrain.colors(10)), main = "NDVI")
plot(knr, main = "Kmeans", col = viridis_pal(option = "D")(10))
dev.off()


par(mar = c(10.8, 5, 10.8, 2), mfrow = c(1, 2))
plotRGB(tayRGB, axes = TRUE, stretch = "lin", main = "RGB")
plot(knr, main = "Kmeans", yaxt = 'n', col = viridis_pal(option = "D")(10))
dev.off()
