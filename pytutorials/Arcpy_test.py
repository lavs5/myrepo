import arcpy

arcpy.env.workspace=r"C:\viu\giscoursework\531\wk9\Lab9_Data\NanaimoGDB.gdb"
folder=r"C:\viu\giscoursework\531\wk9\Lab9_Data"
MyAprx=arcpy.mp.ArcGISProject(folder+r"\Assignment10\Assignment10.aprx")
MyMap=MyAprx.listMaps()[0]
#--------------------
index=0
fc=arcpy.ListFeatureClasses()
for f in fc:
    if arcpy.Describe(f).shapeType=="Polygon":
        index+=1
        if index==2:
            MyPoly=f
            print(MyPoly)

#--------------------

arcpy.AddField_management(MyPoly,"New","DOUBLE")
arcpy.CalculateField_management(MyPoly,"New","!shape.area@SQUAREMETERS!","PYTHON3")


#--------------------
infc=[]
fc=arcpy.ListFeatureClasses()
for f in fc:
    if arcpy.Describe(f).shapeType=="Polygon":
        infc.append(f)
#print(infc)
MyPoly=infc[1]
#print(MyPoly)
#--------------------
