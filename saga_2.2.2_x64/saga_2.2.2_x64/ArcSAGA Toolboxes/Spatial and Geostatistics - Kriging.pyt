import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Kriging"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4]

class tool_0(object):
	def __init__(self):
		self.label = "Ordinary Kriging"
		self.description = "<p>Ordinary Kriging for grid interpolation from irregular sample points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Type of Quality Measure", name="TQUALITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard deviation", "variance"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Logarithmic Transformation", name="LOG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Kriging", name="BLOCK", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Size", name="DBLOCK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="VAR_MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lag Distance Classes", name="VAR_NCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Skip", name="VAR_NSKIP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Model", name="VAR_MODEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "a + b * x"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Prediction", name="PREDICTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quality Measure", name="VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "local"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "maximum number of nearest points"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="SEARCH_POINTS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 16
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="SEARCH_POINTS_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="SEARCH_DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all directions", "quadrants"]
		param.value = "all directions"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_kriging', '0')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TQUALITY', parameters[2].valueAsText)
		Tool.Set_Option('LOG', parameters[3].valueAsText)
		Tool.Set_Option('BLOCK', parameters[4].valueAsText)
		Tool.Set_Option('DBLOCK', parameters[5].valueAsText)
		Tool.Set_Option('VAR_MAXDIST', parameters[6].valueAsText)
		Tool.Set_Option('VAR_NCLASSES', parameters[7].valueAsText)
		Tool.Set_Option('VAR_NSKIP', parameters[8].valueAsText)
		Tool.Set_Option('VAR_MODEL', parameters[9].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[10].valueAsText)
		Tool.Set_Output('PREDICTION', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('VARIANCE', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('SEARCH_RANGE', parameters[13].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[14].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[15].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[16].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[17].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[18].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Simple Kriging"
		self.description = "<p>Simple Kriging for grid interpolation from irregular sample points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Type of Quality Measure", name="TQUALITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard deviation", "variance"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Logarithmic Transformation", name="LOG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Kriging", name="BLOCK", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Size", name="DBLOCK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="VAR_MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lag Distance Classes", name="VAR_NCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Skip", name="VAR_NSKIP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Model", name="VAR_MODEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "a + b * x"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Prediction", name="PREDICTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quality Measure", name="VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "local"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "maximum number of nearest points"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="SEARCH_POINTS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 16
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="SEARCH_POINTS_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="SEARCH_DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all directions", "quadrants"]
		param.value = "all directions"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_kriging', '1')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TQUALITY', parameters[2].valueAsText)
		Tool.Set_Option('LOG', parameters[3].valueAsText)
		Tool.Set_Option('BLOCK', parameters[4].valueAsText)
		Tool.Set_Option('DBLOCK', parameters[5].valueAsText)
		Tool.Set_Option('VAR_MAXDIST', parameters[6].valueAsText)
		Tool.Set_Option('VAR_NCLASSES', parameters[7].valueAsText)
		Tool.Set_Option('VAR_NSKIP', parameters[8].valueAsText)
		Tool.Set_Option('VAR_MODEL', parameters[9].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[10].valueAsText)
		Tool.Set_Output('PREDICTION', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('VARIANCE', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('SEARCH_RANGE', parameters[13].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[14].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[15].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[16].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[17].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[18].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Universal Kriging"
		self.description = "<p>Universal Kriging for grid interpolation from irregular sample points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Type of Quality Measure", name="TQUALITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard deviation", "variance"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Logarithmic Transformation", name="LOG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Kriging", name="BLOCK", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Size", name="DBLOCK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="VAR_MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lag Distance Classes", name="VAR_NCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Skip", name="VAR_NSKIP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Model", name="VAR_MODEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "a + b * x"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Prediction", name="PREDICTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quality Measure", name="VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "local"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "maximum number of nearest points"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="SEARCH_POINTS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 16
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="SEARCH_POINTS_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="SEARCH_DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all directions", "quadrants"]
		param.value = "all directions"
		params += [param]
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Grid Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Coordinates", name="COORDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_kriging', '2')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TQUALITY', parameters[2].valueAsText)
		Tool.Set_Option('LOG', parameters[3].valueAsText)
		Tool.Set_Option('BLOCK', parameters[4].valueAsText)
		Tool.Set_Option('DBLOCK', parameters[5].valueAsText)
		Tool.Set_Option('VAR_MAXDIST', parameters[6].valueAsText)
		Tool.Set_Option('VAR_NCLASSES', parameters[7].valueAsText)
		Tool.Set_Option('VAR_NSKIP', parameters[8].valueAsText)
		Tool.Set_Option('VAR_MODEL', parameters[9].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[10].valueAsText)
		Tool.Set_Output('PREDICTION', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('VARIANCE', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('SEARCH_RANGE', parameters[13].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[14].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[15].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[16].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[17].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[18].valueAsText)
		Tool.Set_Input ('PREDICTORS', parameters[19].valueAsText, 'grid_list')
		Tool.Set_Option('INTERPOL', parameters[20].valueAsText)
		Tool.Set_Option('COORDS', parameters[21].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Regression Kriging"
		self.description = "<p>Regression Kriging for grid interpolation from irregular sample points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Prediction", name="PREDICTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quality Measure", name="VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Type of Quality Measure", name="TQUALITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard deviation", "variance"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Logarithmic Transformation", name="LOG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Kriging", name="BLOCK", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Block Size", name="DBLOCK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="VAR_MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lag Distance Classes", name="VAR_NCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Skip", name="VAR_NSKIP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Variogram Model", name="VAR_MODEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "a + b * x"
		params += [param]
		param = arcpy.Parameter(displayName="Regression: Coefficients", name="INFO_COEFF", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Regression: Model", name="INFO_MODEL", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Regression: Steps", name="INFO_STEPS", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Include X Coordinate", name="COORD_X", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Include Y Coordinate", name="COORD_Y", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Intercept", name="INTERCEPT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["include all", "forward", "backward", "stepwise"]
		param.value = "stepwise"
		params += [param]
		param = arcpy.Parameter(displayName="Significance Level", name="P_VALUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Grid Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "local"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "maximum number of nearest points"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="SEARCH_POINTS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 16
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="SEARCH_POINTS_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="SEARCH_DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all directions", "quadrants"]
		param.value = "all directions"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_kriging', '3')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Input ('PREDICTORS', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('REGRESSION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('PREDICTION', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('RESIDUALS', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('VARIANCE', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('TQUALITY', parameters[7].valueAsText)
		Tool.Set_Option('LOG', parameters[8].valueAsText)
		Tool.Set_Option('BLOCK', parameters[9].valueAsText)
		Tool.Set_Option('DBLOCK', parameters[10].valueAsText)
		Tool.Set_Option('VAR_MAXDIST', parameters[11].valueAsText)
		Tool.Set_Option('VAR_NCLASSES', parameters[12].valueAsText)
		Tool.Set_Option('VAR_NSKIP', parameters[13].valueAsText)
		Tool.Set_Option('VAR_MODEL', parameters[14].valueAsText)
		Tool.Set_Output('INFO_COEFF', parameters[15].valueAsText, 'table')
		Tool.Set_Output('INFO_MODEL', parameters[16].valueAsText, 'table')
		Tool.Set_Output('INFO_STEPS', parameters[17].valueAsText, 'table')
		Tool.Set_Option('COORD_X', parameters[18].valueAsText)
		Tool.Set_Option('COORD_Y', parameters[19].valueAsText)
		Tool.Set_Option('INTERCEPT', parameters[20].valueAsText)
		Tool.Set_Option('METHOD', parameters[21].valueAsText)
		Tool.Set_Option('P_VALUE', parameters[22].valueAsText)
		Tool.Set_Option('INTERPOL', parameters[23].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[24].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[25].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[26].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[27].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[28].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[29].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Variogram (Dialog)"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Variogram", name="VARIOGRAM", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Logarithmic Transformation", name="LOG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="VAR_MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lag Distance Classes", name="VAR_NCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Skip", name="VAR_NSKIP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Model", name="VAR_MODEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "a + b * x"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_kriging', '4')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[1].valueAsText)
		Tool.Set_Output('VARIOGRAM', parameters[2].valueAsText, 'table')
		Tool.Set_Option('LOG', parameters[3].valueAsText)
		Tool.Set_Option('VAR_MAXDIST', parameters[4].valueAsText)
		Tool.Set_Option('VAR_NCLASSES', parameters[5].valueAsText)
		Tool.Set_Option('VAR_NSKIP', parameters[6].valueAsText)
		Tool.Set_Option('VAR_MODEL', parameters[7].valueAsText)
		Tool.Run()
		return
