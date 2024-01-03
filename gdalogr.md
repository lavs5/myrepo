GDAL Geospatial Data Abstraction Library

- GDAL is an open-source library for raster and vector geospatial data formats. The library comes with a vast collection of utility programs that can perform many geoprocessing tasks."GDAL" was used to refer to the raster-related half of the library, while "OGR" referred to the vector part. Numpy: One advanced feature of the GDAL Python bindings not found in the other language bindings is integration with the Python numerical array facilities.

GDAL
--Explore your image data with gdalinfo
--Format translations with gdal_translate
--Reproject your data with gdalwarp
--Mosaic your data with gdal_warp or gdal_merge.py
--Build a shapefile as a raster tileindex with gdaltindex

OGR
--Get information about your data with ogrinfo
--Use ogr2ogr to transform your data to other formats

Getting started:
Start > All Programs > QGIS > OSGeo4W Shell or OSGeo4W

Commonly-used commands
ogrinfo: Get information about a vector dataset
gdalinfo: Get information about a raster dataset
ogr2ogr: Convert vector data between file formats
gdal_translate: Convert raster data between file formats

--The -outsize switch can be used to set the size of the output file.
>gdal_translate -outsize 50% 50% HYP_50M_SR_W.tif  HYP_50M_SR_W_small.tif

--The -scale switch can be used to rescale data. Explicit control of the input and output ranges is also available. The gdalinfo -mm switch can be used to see pixel min/max values.

--Let’s split our image into two with -srcwin which makes a copy based on pixel/line location (xoff yoff xsize ysize). You also could use -projwin and define the corners in georeferenced coordinates (ulx uly lrx lry).
>gdalinfo -mm HYP_50M_SR_W.tif
>gdal_translate -srcwin 0 0 5400 5400 HYP_50M_SR_W.tif  west.tif
>gdal_translate -srcwin 5400 0 5400 5400 HYP_50M_SR_W.tif  east.tif

--Assign WGS84 as coordinate system to the image in the first step.
>gdal_translate -a_srs WGS84 HYP_50M_SR_W.tif HYP_50M_SR_W_4326.tif

--The gdalwarp command can be used to reproject images. Here we reproject the WGS84 geographic image to the Mercator projection:
>gdalwarp -t_srs '+proj=merc +datum=WGS84' HYP_50M_SR_W_4326.tif mercator.tif

Geoprocessing example:
Clip:
>ogr2ogr -skipfailures -clipsrc 
myfolder\Clipusing.shp 
myfolder\clippedresult.shp 
myfolder\tobeclipped.shp

Projection:
>ogr2ogr -t_srs EPSG:3857 -s_srs EPSG:4326 
myfolder\result.shp 
myfolder\input.shp

Raster:
Hillshade:
>gdaldem hillshade

Slope:
>gdaldem color-relief slope.tif sloperamp.txt slopeshade.tif