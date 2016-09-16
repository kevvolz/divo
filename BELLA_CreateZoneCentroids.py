import arcpy
import ntpath
import os

zonepoly = arcpy.GetParameterAsText(0)
workspace = os.path.dirname(os.path.dirname(zonepoly))
pointsname = ntpath.basename(zonepoly) + "_Centroids"
zonecentroid = workspace + r"\ZonePoints\%s" %pointsname
problems = workspace + r"\ProblemCentroids"

centerlist = []
desc = arcpy.Describe(zonepoly)
zonedesc = desc.ShapeFieldName

Cursor = arcpy.SearchCursor
Cursor = arcpy.da.SearchCursor(zonepoly, "SHAPE@XY")
print "everything is set up. Adding features to list..."
for row in Cursor:
    centerlist.append(row[0])

point = arcpy.Point()
pointGeometryList = []

print "features added. Calculating geometries..."
for pt in centerlist:
    point.X = pt[0]
    point.Y = pt[1]
    pointGeometry = arcpy.PointGeometry(point)
    labels = pointGeometry.labelPoint
    newpoint = arcpy.Point(labels.X, labels.Y)
    newgeom = arcpy.PointGeometry(newpoint)
    pointGeometryList.append(newgeom)

print "Geometries calculated. Copying to output file..."
arcpy.CopyFeatures_management(pointGeometryList, zonecentroid)
arcpy.JoinField_management(zonecentroid, "OBJECTID", zonepoly, "OBJECTID", ["Respzone"])
del pointGeometryList

