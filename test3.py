import arcpy
arcpy.env.workspace=r"C:\viu\giscoursework\531\wk9\Lab9_Data\NanaimoGDB.gdb"
folder=r"C:\viu\giscoursework\531\wk9\Lab9_Data"
MyAprx=arcpy.mp.ArcGISProject(folder+r"\Assignment10\Assignment10.aprx")
MyMap=MyAprx.listMaps()[0]
#--------------------
index=0
fc=arcpy.ListFeatureClasses()
print(len(fc))