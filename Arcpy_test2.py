import arcpy
folder=r"C:\viu\giscoursework\531\wk9\Lab9_Data"
arcpy.env.workspace=folder+r"\NanaimoGDB.gdb"
arcpy.env.overwriteOutput=True
MyAprx=arcpy.mp.ArcGISProject(folder+r"\Assignment10\Assignment10.aprx")
MyMap=MyAprx.listMaps()[0]

lyr=arcpy.MakeFeatureLayer_management("Landuse","Water")
arcpy.SelectLayerByAttribute_management("Water","NEW_SELECTION","CATEGORY"+"='Waterbody'")
arcpy.CopyFeatures_management("Water","Waterbody")
reffc=r"\NanaimoGDB.gdb\Waterbody"
MyMap.addDataFromPath(folder+reffc)
MyAprx.save()
