Spatial Data Containers
- sp: The old work-horse for vector data.
- sf: The "tidy" replacement for sp.
- geojson: GeoJSON/TopoJSON web-friendly text-based formats.
- wkb: Well-known in Binary Format
- raster: For raster data

Read External Data
- rgdal / gdalUtils: Supports reading from many spatial data file formats.
- geojsonio: ROpenSci project to read GeoJSON/TopoJSON files.
- ncdf4 / RNetCDF / rhdf5: Multi-Dimensional Spatial/Spatio-Temporal Data.
- rpostgis / postGIStools: Read/Write data from a PostGIS database.
- RQGIS / RSAGA / rgrass7: Interface with external software.
- getlandsat: A treasure trove of Landsat data.
- elevatr: Access elevation data via several web-services.
- tigris / tidycensus / acs / censusapi: Packages for US Census Bureau Data.
- eechidna (AUS census) / pdfetch (UK ONS), and idbr: For international census data.

Spatial Data Operations
- rgeos / gdistance / geosphere: Spatial Operations.
- spatstat / spdep: Spatial Statistics and Analysis.
- spatgraphs: Graph Computation for point pattern analysis.
- maptools: Many Spatial operations like combining spatial data.
- lawn / geoaxe: Operations on GeoJSON data.
- spatial.tools: For working with raster data.
- rmapshaper: Topology aware shape simplification.

Static Maps
- base plotting: Very Powerful, but not intuitive. Many viz. packages provide extensions on top of this.
- cartography: Various types of maps. A very handy package.
- tmap: Thematic mapping.
- ggplot2 / ggalt / ggmap / ggspatial: Tidyverse ecosystem for maps.
- choroplethr: Choropleths
- rasterVis: For raster data, duh!
- gganimate / animation: Stitch a bunch of static plots for animation. Useful for spatio-temporal data


Interactive Maps
- ggiraph : Convert ggplot2 charts to interactive charts.
- leaflet / leaflet.extras / leaflet.minicharts / leaflet.esri: Web Maps using leaflet.js and plug-ins.
- mapview / mapedit: Interactive spatial visualization.
- rbokeh / plotly / highcharter: Solid interactive mapping packages based on different JavaScript libraries.

Odds-n-End
- cartogram / tilegramsR: Cartograms and Tilegrams, as alternative to Geographic maps.
- rnaturalearth: Spatial data from the natural earth project.
- usmap / albersusa: USA Map with Alaska and Hawaii moved.
- RgoogleMaps / googleway / plotGoogleMaps / plotKML: Google maps and APIs.
- OpenStreetMap / osmdata: For working with OpenSteetMap project.

-----------------------------------------------------------

>library(tidyverse)
>library(sf)
>library(tmap)
>library(spData)

Example: US Counties, Georgia

Major US Roads: https://catalog.data.gov/dataset/tiger-line-shapefile-2016-nation-u-s-primary-roads-national-shapefile
GA counties: https://arc-garc.opendata.arcgis.com/datasets/dc20713282734a73abe990995de40497_68

>data("us_states") # from spData package
>ga <- us_states %>% filter(NAME == "Georgia")
>counties <- st_read("myfolder/counties.shp", quiet=T)
>roads <- st_read("myfolder/roads.shp") 

>proj <- "+proj=lcc +lat_1=31.41666666666667 +lat_2=34.28333333333333 +lat_0=0 +lon_0=-83.5 +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs"

>roads <- st_transform(roads, proj)
>ga <- st_transform(ga, proj)
>counties <- st_transform(counties, proj)

>roads <- st_crop(roads, ga)

>plot(st_geometry(ga))
>plot(st_geometry(counties), add = T, col = "red")
>plot(st_geometry(roads), add = T, col = "blue")


Using ggplot
>ggplot(ga) +  geom_sf()

with title
>ggplot(ga) + 
  geom_sf(fill = "beige") +  
  labs(title = "The fine state of Georgia") +  
  theme_minimal()

with more info
>ggplot() +
  geom_sf(data = counties, aes(fill = totpop10)) +
  geom_sf(data = roads, color = "orange") +
  labs(title = "All roads lead to the ATL", fill = "Population") +
  theme_minimal()

Using ggspatial, north arrow, scalebar
>library(ggspatial)
>ggplot() +
  geom_sf(data = counties, aes(fill = totpop10)) +
  geom_sf(data = roads, color = "orange") +
  labs(title = "All roads lead to the ATL", fill = "Population") +
  theme_minimal() +
  annotation_scale(location = "bl", width_hint = 0.5) +
  annotation_north_arrow(location = "tr", which_north = "true", style = north_arrow_fancy_orienteering())


Using tmap
>library(tmap)
>tmap_mode("plot") 
>qtm(roads)

choropleth quick thematic map
>qtm(counties, fill = "totpop10", fill.title = "Total population")

using tm shape
>tm_shape(counties) +
    tm_fill(col = "totpop10", convert2density = T, style = "jenks", 
    title = "Population (x100)") +
    tm_borders(alpha = 0.3) +
    tm_compass() +
    tm_scale_bar()


Save map
>save_tmap(tm, "./fig/my_awesome_map.png", width = 800, height = 1000)

View interactive map
>tmap_mode("view")
>tm