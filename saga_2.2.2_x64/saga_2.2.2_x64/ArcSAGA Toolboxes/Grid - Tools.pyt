import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tools"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_15, tool_17, tool_18, tool_19, tool_20, tool_21, tool_22, tool_24, tool_25, tool_26, tool_27, tool_28, tool_29, tool_30, tool_32]

class tool_0(object):
	def __init__(self):
		self.label = "Resampling"
		self.description = "<p>Resampling of grids.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Preserve Data Type", name="KEEP_TYPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Upscaling Method", name="SCALE_UP", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation", "Mean Value", "Mean Value (cell area weighted)", "Minimum Value", "Maximum Value", "Majority"]
		param.value = "Mean Value (cell area weighted)"
		params += [param]
		param = arcpy.Parameter(displayName="Downscaling Method", name="SCALE_DOWN", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('KEEP_TYPE', parameters[2].valueAsText)
		Tool.Set_Option('SCALE_UP', parameters[3].valueAsText)
		Tool.Set_Option('SCALE_DOWN', parameters[4].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Aggregate"
		self.description = "<p>Resamples a raster layer to a lower resolution, aggregatingthe values of a group of cells. This should be used in any case in which and a normalresampling will result in wrong values in the resulting layer, such as, for instance,the number of elements of a given class in each cell.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Aggregation Size", name="SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["sum", "minimum", "maximum"]
		param.value = "sum"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '1')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('SIZE', parameters[1].valueAsText)
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Mosaicking"
		self.description = "<p>Mosaicking several grids to a single new one. Formerly known as 'Merge Grids'.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Preferred data storage type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 bit", "1 byte unsigned integer", "1 byte signed integer", "2 byte unsigned integer", "2 byte signed integer", "4 byte unsigned integer", "4 byte signed integer", "4 byte floating point", "8 byte floating point"]
		param.value = "4 byte floating point"
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "Nearest Neighbor"
		params += [param]
		param = arcpy.Parameter(displayName="Overlapping Areas", name="OVERLAP", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["first", "last", "minimum", "maximum", "mean", "blend boundary", "feathering"]
		param.value = "last"
		params += [param]
		param = arcpy.Parameter(displayName="Blending Distance", name="BLEND_DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Match", name="MATCH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "regression"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '3')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('TYPE', parameters[1].valueAsText)
		Tool.Set_Option('INTERPOL', parameters[2].valueAsText)
		Tool.Set_Option('OVERLAP', parameters[3].valueAsText)
		Tool.Set_Option('BLEND_DIST', parameters[4].valueAsText)
		Tool.Set_Option('MATCH', parameters[5].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[6].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Constant Grid"
		self.description = "<p>Constant grid creation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Name", name="NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "Constant Grid"
		params  = [param]
		param = arcpy.Parameter(displayName="Constant Value", name="CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["bit", "unsigned 1 byte integer", "signed 1 byte integer", "unsigned 2 byte integer", "signed 2 byte integer", "unsigned 8 byte integer", "signed 8 byte integer", "4 byte floating point number", "8 byte floating point number"]
		param.value = "4 byte floating point number"
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid System", name="DEFINITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["user defined", "grid or grid system"]
		param.value = "user defined"
		params += [param]
		param = arcpy.Parameter(displayName="Left", name="USER_XMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Right", name="USER_XMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bottom", name="USER_YMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Top", name="USER_YMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Columns", name="USER_COLS", direction="Input", parameterType="Required", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Rows", name="USER_ROWS", direction="Input", parameterType="Required", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Fit", name="USER_FITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nodes", "cells"]
		param.value = "nodes"
		params += [param]
		param = arcpy.Parameter(displayName="Target System", name="TEMPLATE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '4')
		Tool.Set_Option('NAME', parameters[0].valueAsText)
		Tool.Set_Option('CONST', parameters[1].valueAsText)
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Option('DEFINITION', parameters[3].valueAsText)
		Tool.Set_Option('USER_XMIN', parameters[4].valueAsText)
		Tool.Set_Option('USER_XMAX', parameters[5].valueAsText)
		Tool.Set_Option('USER_YMIN', parameters[6].valueAsText)
		Tool.Set_Option('USER_YMAX', parameters[7].valueAsText)
		Tool.Set_Option('USER_SIZE', parameters[8].valueAsText)
		Tool.Set_Option('USER_FITS', parameters[9].valueAsText)
		Tool.Set_Input ('TEMPLATE', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('OUT_GRID', parameters[11].valueAsText, 'grid')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Patching"
		self.description = "<p>Fill gaps of a grid with data from another grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="ORIGINAL", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Patch Grid", name="ADDITIONAL", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Completed Grid", name="COMPLETED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation Method", name="INTERPOLATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '5')
		Tool.Set_Input ('ORIGINAL', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('ADDITIONAL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('COMPLETED', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('INTERPOLATION', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Close One Cell Gaps"
		self.description = "<p>Closes one cell gaps using the mean value of the surrounding cell values. If the target is not set, the changes will be stored to the original grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Changed Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '6')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Close Gaps"
		self.description = "<p>Close gaps of a grid data set (i.e. eliminate no data values). If the target is not set, the changes will be stored to the original grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mask", name="MASK", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Changed Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tension Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '7')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Grid Buffer"
		self.description = "<p>The module allows one to buffer features. The features must be encoded by values greater zero. With the buffer distance method 'cell value', the buffer distance must be encoded in the features grid. The output buffer grid is encoded as follows: one inside the buffer, two at feature locations.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features Grid", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Buffer Grid", name="BUFFER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Distance", name="BUFFERTYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Fixed", "Cell value"]
		param.value = "Fixed"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '8')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('BUFFER', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('DIST', parameters[2].valueAsText)
		Tool.Set_Option('BUFFERTYPE', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Threshold Buffer"
		self.description = "<p>(c) 2004 by Victor Olaya. Threshold Buffer Creation<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features Grid", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Value Grid", name="VALUE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Grid", name="THRESHOLDGRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Grid", name="BUFFER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Type", name="THRESHOLDTYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Absolute", "Relative from cell value"]
		param.value = "Absolute"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '9')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('VALUE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('THRESHOLDGRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('BUFFER', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[4].valueAsText)
		Tool.Set_Option('THRESHOLDTYPE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Grid Proximity Buffer"
		self.description = "<p>This module calculates the euclidian distance within a buffer distance from all NoData cells to the nearest valid neighbour in a source grid. Additionally, the source cells define the zones that will be used in the euclidean allocation calculations. Cell values in the source grid are treated as IDs (integer) and used in the allocation grid to identify the grid value of the closest source cell. If a cell is at an equal distance to two or more sources, the cell is assigned to the source that is first encountered in the modules scanning process. The buffer grid is a reclassification of the distance grid using a user specified equidistance to create a set of discrete distance buffers from source features. The buffer zones are coded with the maximum distance value of the corresponding buffer interval. The output value type for the distance grid is floating-point. The output values for the allocation and buffer grid are of type integer. The duration of module execution is dependent on the number of source cells and the buffer distance.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Source Grid", name="SOURCE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Distance Grid", name="DISTANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Allocation Grid", name="ALLOC", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Grid", name="BUFFER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Buffer distance", name="DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 500.000000
		params += [param]
		param = arcpy.Parameter(displayName="Equidistance", name="IVAL", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '10')
		Tool.Set_Input ('SOURCE', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DISTANCE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ALLOC', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('BUFFER', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('DIST', parameters[4].valueAsText)
		Tool.Set_Option('IVAL', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Change Data Storage"
		self.description = "<p>Changes a grid's data storage type, offset and scaling, e.g. from 4 byte floating point to 2 byte signed integer. This might be useful to increase precision or to save memory. If the target is not set, the original grid's storage type will be changed.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Converted Grid", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Data storage type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["bit", "unsigned 1 byte integer", "signed 1 byte integer", "unsigned 2 byte integer", "signed 2 byte integer", "unsigned 4 byte integer", "signed 4 byte integer", "4 byte floating point number", "8 byte floating point number"]
		param.value = "4 byte floating point number"
		params += [param]
		param = arcpy.Parameter(displayName="Offset", name="OFFSET", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '11')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Option('OFFSET', parameters[3].valueAsText)
		Tool.Set_Option('SCALE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Change Grid Values"
		self.description = "<p>Changes values of a grid according to the rules of a user defined lookup table. Values or value ranges that are not listed in the lookup table remain unchanged. If the target is not set, the changes will be stored to the original grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID_IN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Changed Grid", name="GRID_OUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Replace Condition", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Grid value equals low value", "Low value < grid value < high value", "Low value <= grid value < high value"]
		param.value = "Grid value equals low value"
		params += [param]
		param = arcpy.Parameter(displayName="Lookup Table", name="LOOKUP", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '12')
		Tool.Set_Input ('GRID_IN', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('GRID_OUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('LOOKUP', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Reclassify Grid Values"
		self.description = "<p>The module can be used to reclassify the values of a grid. It provides three different options:</p><p>(a) reclassification of single values</p><p>(b) reclassification of a range of values</p><p>(c) reclassification of value ranges specified in a lookup table</p><p></p><p>In addition to these methods, two special cases (NoData values and values not included in the reclassification setup) are supported.</p><p>With reclassification mode (a) and (b), the 'NoData option' is evaluated before the 'Method' settings. In reclassification mode (c) the option is evaluated only if the NoData value is not included in the lookup table.</p><p>The 'other values' option is always evaluated after checking the 'Method' settings.</p><p></p><p>The module allows one to define the NoData value of the output grid (header): by default, the output grid gets assigned the NoData value of the input grid. But it is also possible to assign a user defined NoData value.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Reclassified Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["single", "range", "simple table", "user supplied table"]
		param.value = "single"
		params += [param]
		param = arcpy.Parameter(displayName="old value", name="OLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="new value", name="NEW", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="operator", name="SOPERATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["=", "<", "<=", ">=", ">"]
		param.value = "="
		params += [param]
		param = arcpy.Parameter(displayName="minimum value", name="MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="maximum value", name="MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="new value", name="RNEW", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="operator", name="ROPERATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<=", "<"]
		param.value = "<="
		params += [param]
		param = arcpy.Parameter(displayName="Lookup Table", name="RETAB", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		param = arcpy.Parameter(displayName="operator", name="TOPERATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["min <= value < max", "min <= value <= max", "min < value <= max", "min < value < max"]
		param.value = "min <= value < max"
		params += [param]
		param = arcpy.Parameter(displayName="Lookup Table", name="RETAB_2", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="minimum value", name="F_MIN", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["RETAB_2"]
		params += [param]
		param = arcpy.Parameter(displayName="maximum value", name="F_MAX", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["RETAB_2"]
		params += [param]
		param = arcpy.Parameter(displayName="new value", name="F_CODE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["RETAB_2"]
		params += [param]
		param = arcpy.Parameter(displayName="no data values", name="NODATAOPT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="new value", name="NODATA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="other values", name="OTHEROPT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="new value", name="OTHERS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Assign ...", name="RESULT_NODATA_CHOICE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["NoData value of input grid", "user defined NoData value"]
		param.value = "NoData value of input grid"
		params += [param]
		param = arcpy.Parameter(displayName="NoData Value", name="RESULT_NODATA_VALUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -99999.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '15')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('OLD', parameters[3].valueAsText)
		Tool.Set_Option('NEW', parameters[4].valueAsText)
		Tool.Set_Option('SOPERATOR', parameters[5].valueAsText)
		Tool.Set_Option('MIN', parameters[6].valueAsText)
		Tool.Set_Option('MAX', parameters[7].valueAsText)
		Tool.Set_Option('RNEW', parameters[8].valueAsText)
		Tool.Set_Option('ROPERATOR', parameters[9].valueAsText)
		Tool.Set_Option('RETAB', parameters[10].valueAsText)
		Tool.Set_Option('TOPERATOR', parameters[11].valueAsText)
		Tool.Set_Input ('RETAB_2', parameters[12].valueAsText, 'table')
		Tool.Set_Option('F_MIN', parameters[13].valueAsText)
		Tool.Set_Option('F_MAX', parameters[14].valueAsText)
		Tool.Set_Option('F_CODE', parameters[15].valueAsText)
		Tool.Set_Option('NODATAOPT', parameters[16].valueAsText)
		Tool.Set_Option('NODATA', parameters[17].valueAsText)
		Tool.Set_Option('OTHEROPT', parameters[18].valueAsText)
		Tool.Set_Option('OTHERS', parameters[19].valueAsText)
		Tool.Set_Option('RESULT_NODATA_CHOICE', parameters[20].valueAsText)
		Tool.Set_Option('RESULT_NODATA_VALUE', parameters[21].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Crop to Data"
		self.description = "<p>Crop grids to valid data cells<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Cropped Grids", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '17')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid_list')
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Invert Data/No-Data"
		self.description = "<p>(c) 2005 Victor Olaya.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '18')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Grid Orientation"
		self.description = "<p>Copy, mirror (horizontally or vertically) and invert grid values. If the target is not set, the changes will be stored to the original grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Changed Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Copy", "Flip", "Mirror", "Invert"]
		param.value = "Copy"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '19')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Combine Grids"
		self.description = "<p>(c) 2005 by Victor Olaya.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid 1", name="GRID1", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Grid 2", name="GRID2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LookUp Table", name="LOOKUP", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '20')
		Tool.Set_Input ('GRID1', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRID2', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('LOOKUP', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Grid Cell Index"
		self.description = "<p>Creates an index grid according to the cell values either in ascending or descending order.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Index", name="INDEX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sorting Order", name="ORDER", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["ascending", "descending"]
		param.value = "ascending"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '21')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('INDEX', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('ORDER', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "Grids from classified grid and table"
		self.description = "<p>Creates several grids using a classified grid and a table with data values for each class.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="ID_FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Classes", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '22')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('ID_FIELD', parameters[1].valueAsText)
		Tool.Set_Input ('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('GRIDS', parameters[3].valueAsText, 'grid_list')
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Grid Masking"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mask", name="MASK", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Masked Grid", name="MASKED", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '24')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MASKED', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Close Gaps with Spline"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mask", name="MASK", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Only Process Gaps with Less Cells", name="MAXGAPCELLS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Closed Gaps Grid", name="CLOSED", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Points", name="MAXPOINTS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points for Local Interpolation", name="LOCALPOINTS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Extended Neighourhood", name="EXTENDED", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="NEIGHBOURS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Neumann", "Moore"]
		param.value = "Neumann"
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Relaxation", name="RELAXATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '25')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MAXGAPCELLS', parameters[2].valueAsText)
		Tool.Set_Output('CLOSED', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('MAXPOINTS', parameters[4].valueAsText)
		Tool.Set_Option('LOCALPOINTS', parameters[5].valueAsText)
		Tool.Set_Option('EXTENDED', parameters[6].valueAsText)
		Tool.Set_Option('NEIGHBOURS', parameters[7].valueAsText)
		Tool.Set_Option('RADIUS', parameters[8].valueAsText)
		Tool.Set_Option('RELAXATION', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_26(object):
	def __init__(self):
		self.label = "Proximity Grid"
		self.description = "<p>Calculates a grid with euclidean distance to feature cells (not no-data cells).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Distance", name="DISTANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIRECTION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Allocation", name="ALLOCATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '26')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DISTANCE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIRECTION', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('ALLOCATION', parameters[3].valueAsText, 'grid')
		Tool.Run()
		return


class tool_27(object):
	def __init__(self):
		self.label = "Tiling"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Tiles", name="TILES", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Overlapping Cells", name="OVERLAP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Add Cells", name="OVERLAP_SYM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["symmetric", "bottom / left", "top / right"]
		param.value = "symmetric"
		params += [param]
		param = arcpy.Parameter(displayName="Tile Size Definition", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of grid cells per tile", "coordinates (offset, range, cell size, tile size)"]
		param.value = "number of grid cells per tile"
		params += [param]
		param = arcpy.Parameter(displayName="Save Tiles to Disk", name="SAVE_TILES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Base Name", name="TILE_BASENAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Output Directory", name="TILE_PATH", direction="Input", parameterType="Optional", datatype="DEFolder")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Column Cells", name="NX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Number of Row Cells", name="NY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Offset and Range (X) (Minimum)", name="XRANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Offset and Range (X) (Maximum)", name="XRANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Offset and Range (Y) (Minimum)", name="YRANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Offset and Range (Y) (Maximum)", name="YRANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cell Size", name="DCELL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Tile Size (X)", name="DX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Tile Size (Y)", name="DY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '27')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TILES', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('OVERLAP', parameters[2].valueAsText)
		Tool.Set_Option('OVERLAP_SYM', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('SAVE_TILES', parameters[5].valueAsText)
		Tool.Set_Option('TILE_BASENAME', parameters[6].valueAsText)
		Tool.Set_Option('TILE_PATH', parameters[7].valueAsText)
		Tool.Set_Option('NX', parameters[8].valueAsText)
		Tool.Set_Option('NY', parameters[9].valueAsText)
		Tool.Set_Option('XRANGE_MIN', parameters[10].valueAsText)
		Tool.Set_Option('XRANGE_MAX', parameters[11].valueAsText)
		Tool.Set_Option('YRANGE_MIN', parameters[12].valueAsText)
		Tool.Set_Option('YRANGE_MAX', parameters[13].valueAsText)
		Tool.Set_Option('DCELL', parameters[14].valueAsText)
		Tool.Set_Option('DX', parameters[15].valueAsText)
		Tool.Set_Option('DY', parameters[16].valueAsText)
		Tool.Run()
		return


class tool_28(object):
	def __init__(self):
		self.label = "Shrink and Expand"
		self.description = "<p>Regions with valid data in the input grid can be shrinked or expanded by a certain amount (radius). Shrinking just sets the border of regions with valid data to NoData, expanding sets NoData cells along the border of regions with valid data to a new valid value, computed by the method selected (min, max, mean, majority).</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Result Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation", name="OPERATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["shrink", "expand", "shrink and expand", "expand and shrink"]
		param.value = "expand and shrink"
		params += [param]
		param = arcpy.Parameter(displayName="Search Mode", name="CIRCLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="EXPAND", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["minimum", "maximum", "mean", "majority"]
		param.value = "majority"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '28')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('OPERATION', parameters[2].valueAsText)
		Tool.Set_Option('CIRCLE', parameters[3].valueAsText)
		Tool.Set_Option('RADIUS', parameters[4].valueAsText)
		Tool.Set_Option('EXPAND', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_29(object):
	def __init__(self):
		self.label = "Close Gaps with Stepwise Resampling"
		self.description = "<p>Close gaps of a grid data set (i.e. eliminate no data values). If the target is not set, the changes will be stored to the original grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mask", name="MASK", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOLATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Grow Factor", name="GROW", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Use Pyramids", name="PYRAMIDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Start Size", name="START", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["grid cell size", "user defined size"]
		param.value = "grid cell size"
		params += [param]
		param = arcpy.Parameter(displayName="User Defined Size", name="START_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '29')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('INTERPOLATION', parameters[3].valueAsText)
		Tool.Set_Option('GROW', parameters[4].valueAsText)
		Tool.Set_Option('PYRAMIDS', parameters[5].valueAsText)
		Tool.Set_Option('START', parameters[6].valueAsText)
		Tool.Set_Option('START_SIZE', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_30(object):
	def __init__(self):
		self.label = "Transpose Grids"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Transposed Grids", name="TRANSPOSED", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Mirror Horizontally", name="MIRROR_X", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mirror Vertically", name="MIRROR_Y", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '30')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('TRANSPOSED', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('MIRROR_X', parameters[2].valueAsText)
		Tool.Set_Option('MIRROR_Y', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_32(object):
	def __init__(self):
		self.label = "Select Grid from List"
		self.description = "<p>Main use of this tool is to support tool chain development, allowing to pick a single grid from a grid list. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid List", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Index", name="INDEX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_tools', '32')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('GRID', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('INDEX', parameters[2].valueAsText)
		Tool.Run()
		return
