import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Calculus"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17]

class tool_0(object):
	def __init__(self):
		self.label = "Grid Normalisation"
		self.description = "<p>Normalise the values of a grid. Rescales all grid values to fall in the range 'Minimum' to 'Maximum', usually 0 to 1. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Normalised Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Target Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RANGE_MIN', parameters[2].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Grid Calculator"
		self.description = "<p>The Grid Calculator calculates a new grid based on existing grids and a mathematical formula. The grid variables in the formula begin with the letter 'g' followed by a position index, which corresponds to the order of the grids in the input grid list (i.e.: g1, g2, g3, ... correspond to the first, second, third, ... grid in list). Grids from other systems than the default one can be addressed likewise using the letter 'h' (h1, h2, h3, ...), which correspond to the 'Grids from different Systems' list.</p><p>Example:  sin(g1) * g2 + h1</p><p>the same using indices: sin(g1) * g2 + g3</p><p></p><p>The following operators are available for the formula definition:</p><p>+ Addition</p><p>- Subtraction</p><p>* Multiplication</p><p>/ Division</p><p>^ power</p><p>abs(x)          - absolute value</p><p>sqr(x)          - square</p><p>sqrt(x)         - square root</p><p>ln(x)           - natural logarithm</p><p>log(x)          - base 10 logarithm</p><p>exp(x)          - exponential</p><p>pow(x, y)       - power with mantisse x and exponent y</p><p>sin(x)          - sine</p><p>cos(x)          - cosine</p><p>tan(x)          - tangent</p><p>asin(x)         - arcsine</p><p>acos(x)         - arccosine</p><p>atan(x)         - arctangent</p><p>atan2(x, y)     - arctangent of x/y</p><p>gt(x, y)        - the result is 1.0, if x is greater than y else 0.0</p><p>x > y           - the result is 1.0, if x is greater than y else 0.0</p><p>lt(x, y)        - the result is 1.0, if x is less than y, else 0.0</p><p>x < y           - the result is 1.0, if x is less than y, else 0.0</p><p>eq(x, y)        - the result is 1.0, if x equals y, else 0.0</p><p>x = y           - the result is 1.0, if x equals y, else 0.0</p><p>mod(x, y)       - returns the floating point remainder of x/y</p><p>ifelse(c, x, y) - if condition c is not 0.0 the result is x, else y</p><p>int(x)          - integer part of floating point value x</p><p>pi()            - returns the value of Pi</p><p>xpos(), ypos() - get the x/y coordinates of the current cell</p><p>row(), col() - get the current cell's column/row index</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Grids from different Systems", name="XGRIDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOLATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Formula", name="FORMULA", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "(g1 - g2) / (g1 + g2)"
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "Calculation"
		params += [param]
		param = arcpy.Parameter(displayName="Take Formula", name="FNAME", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Use NoData", name="USE_NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["bit", "unsigned 1 byte integer", "signed 1 byte integer", "unsigned 2 byte integer", "signed 2 byte integer", "unsigned 4 byte integer", "signed 4 byte integer", "4 byte floating point number", "8 byte floating point number"]
		param.value = "4 byte floating point number"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '1')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('XGRIDS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('INTERPOLATION', parameters[2].valueAsText)
		Tool.Set_Output('RESULT', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('FORMULA', parameters[4].valueAsText)
		Tool.Set_Option('NAME', parameters[5].valueAsText)
		Tool.Set_Option('FNAME', parameters[6].valueAsText)
		Tool.Set_Option('USE_NODATA', parameters[7].valueAsText)
		Tool.Set_Option('TYPE', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Grid Volume"
		self.description = "<p>Calculate the volume under the grid's surface. This is mainly useful for Digital Elevation Models (DEM).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Count Only Above Base Level", "Count Only Below Base Level", "Subtract Volumes Below Base Level", "Add Volumes Below Base Level"]
		param.value = "Count Only Above Base Level"
		params += [param]
		param = arcpy.Parameter(displayName="Base Level", name="LEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '2')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[1].valueAsText)
		Tool.Set_Option('LEVEL', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Grid Difference"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="A", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="B", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference (A - B)", name="C", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '3')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('C', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Function"
		self.description = "<p>Generate a grid based on a functional expression.</p><p>The function interpreter uses an expression parser that offers the folowing operators:</p><p></p><p>+ Addition</p><p>- Subtraction</p><p>* Multiplication</p><p>/ Division</p><p>^ power</p><p>sin(a)</p><p>cos(a)</p><p>tan(a)</p><p>asin(a)</p><p>acos(a)</p><p>atan(a)</p><p>atan2(a,b)</p><p>abs(a)</p><p>int(a)</p><p>sqrt(a)</p><p>int(a)</p><p>mod(a,b)</p><p>gt(a,b) returns 1 if a greater b</p><p>lt(a,b) returns 1 if a lower b</p><p>eq(a,b) returns 1 if a equal b</p><p>The Variablen are x and y</p><p>Example: sin(x*x+y*y)/(x*x+y*y)</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Function", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="xmin", name="XMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -5.000000
		params += [param]
		param = arcpy.Parameter(displayName="xmax", name="XMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="ymin", name="YMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -5.000000
		params += [param]
		param = arcpy.Parameter(displayName="ymax", name="YMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Formula", name="FORMUL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "sin(x*x + y*y)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '4')
		Tool.Set_Output('RESULT', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('XMIN', parameters[1].valueAsText)
		Tool.Set_Option('XMAX', parameters[2].valueAsText)
		Tool.Set_Option('YMIN', parameters[3].valueAsText)
		Tool.Set_Option('YMAX', parameters[4].valueAsText)
		Tool.Set_Option('FORMUL', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Geometric Figures"
		self.description = "<p>Construct grids from geometric figures (planes, cones).</p><p>(c) 2001 by Olaf Conrad, Goettingen</p><p>email: oconrad@gwdg.de<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Cell Count", name="CELL_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Cell Size", name="CELL_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Figure", name="FIGURE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Cone (up)", "Cone (down)", "Plane"]
		param.value = "Cone (up)"
		params += [param]
		param = arcpy.Parameter(displayName="Direction of Plane [Degree]", name="PLANE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 22.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '5')
		Tool.Set_Output('RESULT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('CELL_COUNT', parameters[1].valueAsText)
		Tool.Set_Option('CELL_SIZE', parameters[2].valueAsText)
		Tool.Set_Option('FIGURE', parameters[3].valueAsText)
		Tool.Set_Option('PLANE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Random Terrain"
		self.description = "<p>(c) 2004 by Victor Olaya. Random Terrain Generation<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Radius (cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 25
		params  = [param]
		param = arcpy.Parameter(displayName="Iterations", name="ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '6')
		Tool.Set_Option('RADIUS', parameters[0].valueAsText)
		Tool.Set_Option('ITERATIONS', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Random Field"
		self.description = "<p>Create a grid with pseudo-random numbers as grid cell values. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Target Grid System", name="DEFINITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["user defined", "grid or grid system"]
		param.value = "user defined"
		params  = [param]
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
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Uniform", "Gaussian"]
		param.value = "Gaussian"
		params += [param]
		param = arcpy.Parameter(displayName="Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '7')
		Tool.Set_Option('DEFINITION', parameters[0].valueAsText)
		Tool.Set_Option('USER_XMIN', parameters[1].valueAsText)
		Tool.Set_Option('USER_XMAX', parameters[2].valueAsText)
		Tool.Set_Option('USER_YMIN', parameters[3].valueAsText)
		Tool.Set_Option('USER_YMAX', parameters[4].valueAsText)
		Tool.Set_Option('USER_SIZE', parameters[5].valueAsText)
		Tool.Set_Option('USER_FITS', parameters[6].valueAsText)
		Tool.Set_Input ('TEMPLATE', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('OUT_GRID', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[9].valueAsText)
		Tool.Set_Option('RANGE_MIN', parameters[10].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[11].valueAsText)
		Tool.Set_Option('MEAN', parameters[12].valueAsText)
		Tool.Set_Option('STDDEV', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Grids Sum"
		self.description = "<p>Cellwise addition of grid values.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Sum", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '8')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Grids Product"
		self.description = "<p>Cellwise multiplication of grid values.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Product", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '9')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Grid Standardisation"
		self.description = "<p>Standardise the values of a grid. The standard score (z) is calculated as raw score (x) less arithmetic mean (m) divided by standard deviation (s).</p><p>z = (x - m) * s<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Standardised Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Stretch Factor", name="STRETCH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '10')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('STRETCH', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Fuzzify"
		self.description = "<p>Translates grid values into fuzzy set membership as preparation for fuzzy logic analysis.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Fuzzified Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="A", name="A", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="B", name="B", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="C", name="C", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="D", name="D", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Membership Function Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["linear", "sigmoidal", "j-shaped"]
		param.value = "linear"
		params += [param]
		param = arcpy.Parameter(displayName="Adjust to Grid", name="AUTOFIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '11')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('A', parameters[2].valueAsText)
		Tool.Set_Option('B', parameters[3].valueAsText)
		Tool.Set_Option('C', parameters[4].valueAsText)
		Tool.Set_Option('D', parameters[5].valueAsText)
		Tool.Set_Option('TYPE', parameters[6].valueAsText)
		Tool.Set_Option('AUTOFIT', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Fuzzy Intersection (AND)"
		self.description = "<p>Calculates the intersection (min operator) for each grid cell of the selected grids.</p><p> e-mail Gianluca Massei: g_massa@libero.it </p><p>e-mail Antonio Boggia: boggia@unipg.it </p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Intersection", name="AND", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operator Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["min(a, b) (non-interactive)", "a * b", "max(0, a + b - 1)"]
		param.value = "min(a, b) (non-interactive)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '12')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('AND', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Fuzzy Union (OR)"
		self.description = "<p>Calculates the union (max operator) for each grid cell of the selected grids.</p><p> e-mail Gianluca Massei: g_massa@libero.it </p><p>e-mail Antonio Boggia: boggia@unipg.it </p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Union", name="OR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operator Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["max(a, b) (non-interactive)", "a + b - a * b", "min(1, a + b)"]
		param.value = "max(a, b) (non-interactive)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '13')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OR', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Metric Conversions"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Converted Grid", name="CONV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Conversion", name="CONVERSION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians to degree", "degree to radians", "Celsius to Fahrenheit", "Fahrenheit to Celsius"]
		param.value = "radians to degree"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '14')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONV', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('CONVERSION', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Gradient Vector from Cartesian to Polar Coordinates"
		self.description = "<p>Converts gradient vector from directional components (Cartesian) to polar coordinates (direction or aspect angle and length or tangens of slope).</p><p>The module supports three conventions on how to measure and output the angle of direction:</p><p>(a) mathematical: direction angle is zero in East direction and the angle increases counterclockwise</p><p>(b) geographical: direction angle is zero in North direction and the angle increases clockwise</p><p>(c) zero direction and orientation are user defined</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="X Component", name="DX", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Y Component", name="DY", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Length", name="LEN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polar Angle Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Polar Coordinate System", name="SYSTEM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["mathematical", "geographical", "user defined"]
		param.value = "geographical"
		params += [param]
		param = arcpy.Parameter(displayName="User defined Zero Direction", name="SYSTEM_ZERO", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="User defined Orientation", name="SYSTEM_ORIENT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["clockwise", "counterclockwise"]
		param.value = "clockwise"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '15')
		Tool.Set_Input ('DX', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIR', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LEN', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('UNITS', parameters[4].valueAsText)
		Tool.Set_Option('SYSTEM', parameters[5].valueAsText)
		Tool.Set_Option('SYSTEM_ZERO', parameters[6].valueAsText)
		Tool.Set_Option('SYSTEM_ORIENT', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Gradient Vector from Polar to Cartesian Coordinates"
		self.description = "<p>Converts gradient vector from polar coordinates (direction or aspect angle and length or tangens of slope) to directional components (Cartesian).</p><p>The module supports three conventions on how the angle of direction can be supplied:</p><p>(a) mathematical: direction angle is zero in East direction and the angle increases counterclockwise</p><p>(b) geographical: direction angle is zero in North direction and the angle increases clockwise</p><p>(c) zero direction and orientation are user defined</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Direction", name="DIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Length", name="LEN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X Component", name="DX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Y Component", name="DY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polar Angle Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Polar Coordinate System", name="SYSTEM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["mathematical", "geographical", "user defined"]
		param.value = "geographical"
		params += [param]
		param = arcpy.Parameter(displayName="User defined Zero Direction", name="SYSTEM_ZERO", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="User defined Orientation", name="SYSTEM_ORIENT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["clockwise", "counterclockwise"]
		param.value = "clockwise"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '16')
		Tool.Set_Input ('DIR', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LEN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DX', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DY', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('UNITS', parameters[4].valueAsText)
		Tool.Set_Option('SYSTEM', parameters[5].valueAsText)
		Tool.Set_Option('SYSTEM_ZERO', parameters[6].valueAsText)
		Tool.Set_Option('SYSTEM_ORIENT', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Grid Division"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Dividend", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Divisor", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quotient", name="C", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '18')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('C', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return
