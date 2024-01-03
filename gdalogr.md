GDAL Geospatial Data Abstraction Library

- GDAL is an open-source library for raster and vector geospatial data formats. 
- The library comes with a vast collection of utility programs that can perform many geoprocessing tasks.
- "GDAL" was used to refer to the raster-related half of the library, while "OGR" referred to the vector part.

Getting started:
Start > All Programs > QGIS > OSGeo4W Shell or OSGeo4W

Commonly-used commands
ogrinfo: Get information about a vector dataset
gdalinfo: Get information about a raster dataset
ogr2ogr: Convert vector data between file formats
gdal_translate: Convert raster data between file formats

Geoprocessing example:
Clip:
ogr2ogr -skipfailures -clipsrc 
myfolder\Clipusing.shp 
myfolder\clippedresult.shp 
myfolder\tobeclipped.shp

Projection:
ogr2ogr -t_srs EPSG:3857 -s_srs EPSG:4326 
myfolder\result.shp 
myfolder\input.shp

Raster:
Hillshade:
gdaldem hillshade

Slope:
gdaldem color-relief slope.tif sloperamp.txt slopeshade.tif