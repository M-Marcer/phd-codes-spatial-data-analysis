import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grid Tools"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_12, tool_13, tool_14]

class tool_0(object):
	def __init__(self):
		self.label = "Add Grid Values to Points"
		self.description = "<p>Spatial Join: Retrieves information from the selected grids at the positions of the points of the selected points layer and adds it to the resulting layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '0')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('GRIDS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('INTERPOL', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Add Grid Values to Shapes"
		self.description = "<p>Spatial Join: Retrieves information from the selected grids at the positions of the shapes of the selected shapes layer and adds it to the resulting shapes layer. For points this is similar to 'Add Grid Values to Points' module. For lines and polygons average values will be calculated from interfering grid cells. For polygons the 'Grid Statistics for Polygons' module offers more advanced options. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '1')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('GRIDS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('INTERPOL', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Grid Statistics for Polygons"
		self.description = "<p>Zonal grid statistics. For each polygon statistics based on all covered grid cells will be calculated.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard", "shape wise, supports overlapping polygons"]
		param.value = "standard"
		params += [param]
		param = arcpy.Parameter(displayName="Field Naming", name="NAMING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["grid number", "grid name"]
		param.value = "grid name"
		params += [param]
		param = arcpy.Parameter(displayName="Statistics", name="RESULT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Cells", name="COUNT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Mean", name="MEAN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Quantile", name="QUANTILE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '2')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('NAMING', parameters[3].valueAsText)
		Tool.Set_Output('RESULT', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('COUNT', parameters[5].valueAsText)
		Tool.Set_Option('MIN', parameters[6].valueAsText)
		Tool.Set_Option('MAX', parameters[7].valueAsText)
		Tool.Set_Option('RANGE', parameters[8].valueAsText)
		Tool.Set_Option('SUM', parameters[9].valueAsText)
		Tool.Set_Option('MEAN', parameters[10].valueAsText)
		Tool.Set_Option('VAR', parameters[11].valueAsText)
		Tool.Set_Option('STDDEV', parameters[12].valueAsText)
		Tool.Set_Option('QUANTILE', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Grid Values to Points"
		self.description = "<p>This module saves grid values to point (grid nodes) or polygon (grid cells) shapes. Optionally only points can be saved, which are contained by polygons of the specified shapes layer. In addition, it is possible to exclude all cells that are coded NoData in the first grid of the grid list.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Exclude NoData Cells", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nodes", "cells"]
		param.value = "nodes"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '3')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('SHAPES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('NODATA', parameters[3].valueAsText)
		Tool.Set_Option('TYPE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Grid Values to Points (randomly)"
		self.description = "<p>Extract randomly points from gridded data.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Frequency", name="FREQ", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '4')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('FREQ', parameters[1].valueAsText)
		Tool.Set_Output('POINTS', parameters[2].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Contour Lines from Grid"
		self.description = "<p>Derive contour lines (isolines) from grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Contour", name="CONTOUR", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vertex Type", name="VERTEX", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["x, y", "x, y, z"]
		param.value = "x, y"
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation Scale", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="LINE_PARTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Split Polygon Parts", name="POLY_PARTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Contour Value", name="ZMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Contour Value", name="ZMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Equidistance", name="ZSTEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '5')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONTOUR', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('POLYGONS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('VERTEX', parameters[3].valueAsText)
		Tool.Set_Option('SCALE', parameters[4].valueAsText)
		Tool.Set_Option('LINE_PARTS', parameters[5].valueAsText)
		Tool.Set_Option('POLY_PARTS', parameters[6].valueAsText)
		Tool.Set_Option('ZMIN', parameters[7].valueAsText)
		Tool.Set_Option('ZMAX', parameters[8].valueAsText)
		Tool.Set_Option('ZSTEP', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Vectorising Grid Classes"
		self.description = "<p>Vectorising grid classes.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Selection", name="CLASS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["one single class specified by class identifier", "all classes"]
		param.value = "all classes"
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="CLASS_ID", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Vectorised class as...", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["one single (multi-)polygon object", "each island as separated polygon"]
		param.value = "one single (multi-)polygon object"
		params += [param]
		param = arcpy.Parameter(displayName="Keep Vertices on Straight Lines", name="ALLVERTICES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '6')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('CLASS_ALL', parameters[2].valueAsText)
		Tool.Set_Option('CLASS_ID', parameters[3].valueAsText)
		Tool.Set_Option('SPLIT', parameters[4].valueAsText)
		Tool.Set_Option('ALLVERTICES', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Clip Grid with Polygon"
		self.description = "<p>Clips the input grid with a polygon shapefile. Select polygons from the shapefile prior to module execution in case you like to use only a subset from the shapefile for clipping.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Exclude No-Data Area", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '7')
		Tool.Set_Output('OUTPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('INPUT', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('POLYGONS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('NODATA', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Grid Statistics for Points"
		self.description = "<p>For each given point statistics based on all grid cells in the defined neighbourhood will be calculated.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["square", "circle"]
		param.value = "square"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Size", name="KERNEL_SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Field Naming", name="NAMING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["grid number", "grid name"]
		param.value = "grid name"
		params += [param]
		param = arcpy.Parameter(displayName="Statistics", name="RESULT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Cells", name="COUNT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Mean", name="MEAN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Quantile", name="QUANTILE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '8')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('KERNEL_TYPE', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_SIZE', parameters[3].valueAsText)
		Tool.Set_Option('NAMING', parameters[4].valueAsText)
		Tool.Set_Output('RESULT', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('COUNT', parameters[6].valueAsText)
		Tool.Set_Option('MIN', parameters[7].valueAsText)
		Tool.Set_Option('MAX', parameters[8].valueAsText)
		Tool.Set_Option('RANGE', parameters[9].valueAsText)
		Tool.Set_Option('SUM', parameters[10].valueAsText)
		Tool.Set_Option('MEAN', parameters[11].valueAsText)
		Tool.Set_Option('VAR', parameters[12].valueAsText)
		Tool.Set_Option('STDDEV', parameters[13].valueAsText)
		Tool.Set_Option('QUANTILE', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Local Minima and Maxima"
		self.description = "<p>Extracts local grid value minima and maxima of to vector points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Minima", name="MINIMA", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maxima", name="MAXIMA", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '9')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MINIMA', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('MAXIMA', parameters[2].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Gradient Vectors from Surface"
		self.description = "<p>Create lines indicating the gradient. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Surface", name="SURFACE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Gradient Vectors", name="VECTORS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Size Range (Minimum)", name="SIZE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		param = arcpy.Parameter(displayName="Size Range (Maximum)", name="SIZE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Aggregation", name="AGGR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "mean value"]
		param.value = "mean value"
		params += [param]
		param = arcpy.Parameter(displayName="Style", name="STYLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["simple line", "arrow", "arrow (centered to cell)"]
		param.value = "arrow (centered to cell)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '15')
		Tool.Set_Input ('SURFACE', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VECTORS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('STEP', parameters[2].valueAsText)
		Tool.Set_Option('SIZE_MIN', parameters[3].valueAsText)
		Tool.Set_Option('SIZE_MAX', parameters[4].valueAsText)
		Tool.Set_Option('AGGR', parameters[5].valueAsText)
		Tool.Set_Option('STYLE', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Gradient Vectors from Direction and Length"
		self.description = "<p>Create lines indicating the gradient. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Direction", name="DIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Length", name="LEN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Gradient Vectors", name="VECTORS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Size Range (Minimum)", name="SIZE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		param = arcpy.Parameter(displayName="Size Range (Maximum)", name="SIZE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Aggregation", name="AGGR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "mean value"]
		param.value = "mean value"
		params += [param]
		param = arcpy.Parameter(displayName="Style", name="STYLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["simple line", "arrow", "arrow (centered to cell)"]
		param.value = "arrow (centered to cell)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '16')
		Tool.Set_Input ('DIR', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LEN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('VECTORS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('SIZE_MIN', parameters[4].valueAsText)
		Tool.Set_Option('SIZE_MAX', parameters[5].valueAsText)
		Tool.Set_Option('AGGR', parameters[6].valueAsText)
		Tool.Set_Option('STYLE', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Gradient Vectors from Directional Components"
		self.description = "<p>Create lines indicating the gradient. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="X Component", name="X", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Y Component", name="Y", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Gradient Vectors", name="VECTORS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Size Range (Minimum)", name="SIZE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		param = arcpy.Parameter(displayName="Size Range (Maximum)", name="SIZE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Aggregation", name="AGGR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "mean value"]
		param.value = "mean value"
		params += [param]
		param = arcpy.Parameter(displayName="Style", name="STYLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["simple line", "arrow", "arrow (centered to cell)"]
		param.value = "arrow (centered to cell)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_grid', '17')
		Tool.Set_Input ('X', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('Y', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('VECTORS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('SIZE_MIN', parameters[4].valueAsText)
		Tool.Set_Option('SIZE_MAX', parameters[5].valueAsText)
		Tool.Set_Option('AGGR', parameters[6].valueAsText)
		Tool.Set_Option('STYLE', parameters[7].valueAsText)
		Tool.Run()
		return
