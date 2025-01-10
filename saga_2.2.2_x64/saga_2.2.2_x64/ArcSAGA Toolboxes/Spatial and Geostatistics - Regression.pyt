import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Regression"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_14, tool_15]

class tool_0(object):
	def __init__(self):
		self.label = "Regression Analysis (Points and Predictor Grid)"
		self.description = "<p>Regression analysis of point attributes with a grid as predictor. The regression function is used to create a new grid with regression based values. </p><p></p><p>Reference:</p><p>- Bahrenberg, G., Giese, E., Nipper, J. (1990): 'Statistische Methoden in der Geographie 1 - Univariate und bivariate Statistik', Stuttgart, 233p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Predictor", name="PREDICTOR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUAL", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Grid Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Regression Function", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Y = a + b * X (linear)", "Y = a + b / X", "Y = a / (b - X)", "Y = a * X^b (power)", "Y = a e^(b * X) (exponential)", "Y = a + b * ln(X) (logarithmic)"]
		param.value = "Y = a + b * X (linear)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '0')
		Tool.Set_Input ('PREDICTOR', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[2].valueAsText)
		Tool.Set_Output('REGRESSION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('RESIDUAL', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('INTERPOL', parameters[5].valueAsText)
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Multiple Regression Analysis (Points and Predictor Grids)"
		self.description = "<p>Linear regression analysis of point attributes with multiple grids. Details of the regression/correlation analysis will be saved to a table. The regression function is used to create a new grid with regression based values. The multiple regression analysis uses a forward selection procedure. </p><p></p><p>Reference:</p><p>- Bahrenberg, G., Giese, E., Nipper, J. (1992): 'Statistische Methoden in der Geographie 2 - Multivariate Statistik', Stuttgart, 415p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Details: Coefficients", name="INFO_COEFF", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Details: Model", name="INFO_MODEL", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Details: Steps", name="INFO_STEPS", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regression with Residual Correction", name="REGRESCORR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Grid Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
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
		param = arcpy.Parameter(displayName="Cross Validation", name="CROSSVAL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "leave one out", "2-fold", "k-fold"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Subsamples", name="CROSSVAL_K", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Residual Interpolation", name="RESIDUAL_COR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Multleve B-Spline Interpolation", "Inverse Distance Weighted"]
		param.value = "Multleve B-Spline Interpolation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '1')
		Tool.Set_Input ('PREDICTORS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[2].valueAsText)
		Tool.Set_Output('INFO_COEFF', parameters[3].valueAsText, 'table')
		Tool.Set_Output('INFO_MODEL', parameters[4].valueAsText, 'table')
		Tool.Set_Output('INFO_STEPS', parameters[5].valueAsText, 'table')
		Tool.Set_Output('RESIDUALS', parameters[6].valueAsText, 'shapes')
		Tool.Set_Output('REGRESSION', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('REGRESCORR', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('INTERPOL', parameters[9].valueAsText)
		Tool.Set_Option('COORD_X', parameters[10].valueAsText)
		Tool.Set_Option('COORD_Y', parameters[11].valueAsText)
		Tool.Set_Option('INTERCEPT', parameters[12].valueAsText)
		Tool.Set_Option('METHOD', parameters[13].valueAsText)
		Tool.Set_Option('P_VALUE', parameters[14].valueAsText)
		Tool.Set_Option('CROSSVAL', parameters[15].valueAsText)
		Tool.Set_Option('CROSSVAL_K', parameters[16].valueAsText)
		Tool.Set_Option('RESIDUAL_COR', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Polynomial Regression"
		self.description = "<p>Reference:</p><p> - Lloyd, C. (2010): Spatial Data Analysis - An Introduction for GIS Users. Oxford, 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polynom", name="POLYNOM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["simple planar surface", "bi-linear saddle", "quadratic surface", "cubic surface", "user defined"]
		param.value = "simple planar surface"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum X Order", name="XORDER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Y Order", name="YORDER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Total Order", name="TORDER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '2')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[1].valueAsText)
		Tool.Set_Output('RESIDUALS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('POLYNOM', parameters[3].valueAsText)
		Tool.Set_Option('XORDER', parameters[4].valueAsText)
		Tool.Set_Option('YORDER', parameters[5].valueAsText)
		Tool.Set_Option('TORDER', parameters[6].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[7].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[8].valueAsText, 'grid')
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "GWR for Single Predictor (Gridded Model Output)"
		self.description = "<p>Reference:</p><p>- Fotheringham, S.A., Brunsdon, C., Charlton, M. (2002):  Geographically Weighted Regression: the analysis of spatially varying relationships. John Wiley & Sons.  <a target=\"_blank\" href=\"http://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.2003.tb01114.x/abstract\">online</a>.</p><p></p><p>- Fotheringham, S.A., Charlton, M., Brunsdon, C. (1998):  Geographically weighted regression: a natural evolution of the expansion method for spatial data analysis.  Environment and Planning A 30(11), 1905–1927.  <a target=\"_blank\" href=\"http://www.envplan.com/abstract.cgi?id=a301905\">online</a>.</p><p></p><p>- Lloyd, C. (2010):  Spatial Data Analysis - An Introduction for GIS Users. Oxford, 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="DEPENDENT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Predictor", name="PREDICTOR", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Intercept", name="INTERCEPT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quality", name="QUALITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "global"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "all points within search distance"
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
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '3')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('DEPENDENT', parameters[1].valueAsText)
		Tool.Set_Option('PREDICTOR', parameters[2].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[3].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('INTERCEPT', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('QUALITY', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('DW_WEIGHTING', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[9].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[10].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[11].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[12].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[13].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[14].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[15].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[16].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "GWR for Single Predictor Grid"
		self.description = "<p>Geographically Weighted Regression for a single predictor supplied as grid, to which the regression model is applied. Further details can be stored optionally.</p><p>Reference:</p><p>- Fotheringham, S.A., Brunsdon, C., Charlton, M. (2002):  Geographically Weighted Regression: the analysis of spatially varying relationships. John Wiley & Sons.  <a target=\"_blank\" href=\"http://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.2003.tb01114.x/abstract\">online</a>.</p><p></p><p>- Fotheringham, S.A., Charlton, M., Brunsdon, C. (1998):  Geographically weighted regression: a natural evolution of the expansion method for spatial data analysis.  Environment and Planning A 30(11), 1905–1927.  <a target=\"_blank\" href=\"http://www.envplan.com/abstract.cgi?id=a301905\">online</a>.</p><p></p><p>- Lloyd, C. (2010):  Spatial Data Analysis - An Introduction for GIS Users. Oxford, 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="DEPENDENT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Predictor", name="PREDICTOR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coefficient of Determination", name="QUALITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Intercept", name="INTERCEPT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "global"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "all points within search distance"
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
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '4')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('DEPENDENT', parameters[1].valueAsText)
		Tool.Set_Output('RESIDUALS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Input ('PREDICTOR', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('REGRESSION', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('QUALITY', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('INTERCEPT', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('DW_WEIGHTING', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[9].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[10].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[11].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[12].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[13].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[14].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[15].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[16].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "GWR for Multiple Predictors (Gridded Model Output)"
		self.description = "<p>Geographically Weighted Regression for multiple predictors. Predictors have to be supplied as attributes of ingoing points data. Regression model parameters are generated as continuous fields, i.e. as grids.</p><p>Reference:</p><p>- Fotheringham, S.A., Brunsdon, C., Charlton, M. (2002):  Geographically Weighted Regression: the analysis of spatially varying relationships. John Wiley & Sons.  <a target=\"_blank\" href=\"http://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.2003.tb01114.x/abstract\">online</a>.</p><p></p><p>- Fotheringham, S.A., Charlton, M., Brunsdon, C. (1998):  Geographically weighted regression: a natural evolution of the expansion method for spatial data analysis.  Environment and Planning A 30(11), 1905–1927.  <a target=\"_blank\" href=\"http://www.envplan.com/abstract.cgi?id=a301905\">online</a>.</p><p></p><p>- Lloyd, C. (2010):  Spatial Data Analysis - An Introduction for GIS Users. Oxford, 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="DEPENDENT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Quality", name="QUALITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Intercept", name="INTERCEPT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slopes", name="SLOPES", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "global"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "all points within search distance"
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
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '5')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('DEPENDENT', parameters[1].valueAsText)
		Tool.Set_Option('PREDICTORS', parameters[2].valueAsText)
		Tool.Set_Output('REGRESSION', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('TARGET_USER_SIZE', parameters[4].valueAsText)
		Tool.Set_Output('QUALITY', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('INTERCEPT', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SLOPES', parameters[7].valueAsText, 'grid_list')
		Tool.Set_Option('DW_WEIGHTING', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[9].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[10].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[11].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[12].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[13].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[14].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[15].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[16].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "GWR for Multiple Predictor Grids"
		self.description = "<p>References:</p><p>- Fotheringham, S.A., Brunsdon, C., Charlton, M. (2002):  Geographically Weighted Regression: the analysis of spatially varying relationships. John Wiley & Sons.  <a target=\"_blank\" href=\"http://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.2003.tb01114.x/abstract\">online</a>.</p><p></p><p>- Fotheringham, S.A., Charlton, M., Brunsdon, C. (1998):  Geographically weighted regression: a natural evolution of the expansion method for spatial data analysis.  Environment and Planning A 30(11), 1905–1927.  <a target=\"_blank\" href=\"http://www.envplan.com/abstract.cgi?id=a301905\">online</a>.</p><p></p><p>- Lloyd, C. (2010):  Spatial Data Analysis - An Introduction for GIS Users. Oxford, 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="DEPENDENT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coefficient of Determination", name="QUALITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regression Parameters", name="MODEL", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Output of Regression Parameters", name="MODEL_OUT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Model Resolution", name="RESOLUTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["same as predictors", "user defined"]
		param.value = "user defined"
		params += [param]
		param = arcpy.Parameter(displayName="Resolution", name="RESOLUTION_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "global"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "all points within search distance"
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
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '6')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('DEPENDENT', parameters[1].valueAsText)
		Tool.Set_Output('RESIDUALS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Input ('PREDICTORS', parameters[3].valueAsText, 'grid_list')
		Tool.Set_Output('REGRESSION', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('QUALITY', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('MODEL', parameters[6].valueAsText, 'grid_list')
		Tool.Set_Option('MODEL_OUT', parameters[7].valueAsText)
		Tool.Set_Option('RESOLUTION', parameters[8].valueAsText)
		Tool.Set_Option('RESOLUTION_VAL', parameters[9].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[10].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[11].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[12].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[13].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[14].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[15].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[16].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[17].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[18].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[19].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "GWR for Multiple Predictors"
		self.description = "<p>Geographically Weighted Regression for multiple predictors. Regression details are stored in a copy of input points.</p><p>Reference:</p><p>- Fotheringham, S.A., Brunsdon, C., Charlton, M. (2002):  Geographically Weighted Regression: the analysis of spatially varying relationships. John Wiley & Sons.  <a target=\"_blank\" href=\"http://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.2003.tb01114.x/abstract\">online</a>.</p><p></p><p>- Fotheringham, S.A., Charlton, M., Brunsdon, C. (1998):  Geographically weighted regression: a natural evolution of the expansion method for spatial data analysis.  Environment and Planning A 30(11), 1905–1927.  <a target=\"_blank\" href=\"http://www.envplan.com/abstract.cgi?id=a301905\">online</a>.</p><p></p><p>- Lloyd, C. (2010):  Spatial Data Analysis - An Introduction for GIS Users. Oxford, 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="DEPENDENT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "global"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "all points within search distance"
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
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '7')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('DEPENDENT', parameters[1].valueAsText)
		Tool.Set_Option('PREDICTORS', parameters[2].valueAsText)
		Tool.Set_Output('REGRESSION', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('DW_WEIGHTING', parameters[4].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[6].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[7].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[8].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[9].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[10].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[11].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[12].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Multiple Regression Analysis (Grid and Predictor Grids)"
		self.description = "<p>Linear regression analysis of one grid as dependent and multiple grids as indepentent (predictor) variables. Details of the regression/correlation analysis will be saved to a table. Optionally the regression model is used to create a new grid with regression based values. The multiple regression analysis uses a forward selection procedure. </p><p></p><p>Reference:</p><p>- Bahrenberg, G., Giese, E., Nipper, J. (1992): 'Statistische Methoden in der Geographie 2 - Multivariate Statistik', Stuttgart, 415p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Dependent Variable", name="DEPENDENT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Details: Coefficients", name="INFO_COEFF", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Details: Model", name="INFO_MODEL", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Details: Steps", name="INFO_STEPS", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Grid Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Include X Coordinate", name="COORD_X", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Include Y Coordinate", name="COORD_Y", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["include all", "forward", "backward", "stepwise"]
		param.value = "stepwise"
		params += [param]
		param = arcpy.Parameter(displayName="Significance Level", name="P_VALUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation", name="CROSSVAL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "leave one out", "2-fold", "k-fold"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Subsamples", name="CROSSVAL_K", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '8')
		Tool.Set_Input ('DEPENDENT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('PREDICTORS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('REGRESSION', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('RESIDUALS', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('INFO_COEFF', parameters[4].valueAsText, 'table')
		Tool.Set_Output('INFO_MODEL', parameters[5].valueAsText, 'table')
		Tool.Set_Output('INFO_STEPS', parameters[6].valueAsText, 'table')
		Tool.Set_Option('INTERPOL', parameters[7].valueAsText)
		Tool.Set_Option('COORD_X', parameters[8].valueAsText)
		Tool.Set_Option('COORD_Y', parameters[9].valueAsText)
		Tool.Set_Option('METHOD', parameters[10].valueAsText)
		Tool.Set_Option('P_VALUE', parameters[11].valueAsText)
		Tool.Set_Option('CROSSVAL', parameters[12].valueAsText)
		Tool.Set_Option('CROSSVAL_K', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Polynomial Trend from Grids"
		self.description = "<p>Fits for each cell a polynomial trend function. Outputs are the polynomial coefficients for the polynomial trend function of chosen order. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Dependent Variables", name="Y_GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Polynomial Coefficients", name="COEFF", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Coefficient of Determination", name="R2", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polynomial Order", name="ORDER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Get Independent Variable from ...", name="XSOURCE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["list order", "table", "grid list"]
		param.value = "list order"
		params += [param]
		param = arcpy.Parameter(displayName="Independent Variable (per Grid)", name="X_TABLE", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		param = arcpy.Parameter(displayName="Independent Variable (per Grid and Cell)", name="X_GRIDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '9')
		Tool.Set_Input ('Y_GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('COEFF', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('R2', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('ORDER', parameters[3].valueAsText)
		Tool.Set_Option('XSOURCE', parameters[4].valueAsText)
		Tool.Set_Option('X_TABLE', parameters[5].valueAsText)
		Tool.Set_Input ('X_GRIDS', parameters[6].valueAsText, 'grid_list')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Trend Analysis"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="X Values", name="FIELD_X", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Y Values", name="FIELD_Y", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Formula", name="FORMULA", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "m * x + b"
		params += [param]
		param = arcpy.Parameter(displayName="Pre-defined Formulas", name="FORMULAS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Linear: a + b * x", "Quadric: a + b * x + c * x^2", "Cubic: a + b * x + c * x^2 + d * x^3", "Logarithmic: a + b * ln(x)", "Power: a + b * x^c", "a + b / x", "a + b * (1 - exp(-x / c))", "a + b * (1 - exp(-(x / c)^2))"]
		param.value = "Linear: a + b * x"
		params += [param]
		param = arcpy.Parameter(displayName="Table (with Trend)", name="TREND", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '10')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('FIELD_X', parameters[1].valueAsText)
		Tool.Set_Option('FIELD_Y', parameters[2].valueAsText)
		Tool.Set_Option('FORMULA', parameters[3].valueAsText)
		Tool.Set_Option('FORMULAS', parameters[4].valueAsText)
		Tool.Set_Output('TREND', parameters[5].valueAsText, 'table')
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Trend Analysis (Shapes)"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="TABLE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="X Values", name="FIELD_X", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Y Values", name="FIELD_Y", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Formula", name="FORMULA", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "m * x + b"
		params += [param]
		param = arcpy.Parameter(displayName="Pre-defined Formulas", name="FORMULAS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Linear: a + b * x", "Quadric: a + b * x + c * x^2", "Cubic: a + b * x + c * x^2 + d * x^3", "Logarithmic: a + b * ln(x)", "Power: a + b * x^c", "a + b / x", "a + b * (1 - exp(-x / c))", "a + b * (1 - exp(-(x / c)^2))"]
		param.value = "Linear: a + b * x"
		params += [param]
		param = arcpy.Parameter(displayName="Table (with Trend)", name="TREND", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '11')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD_X', parameters[1].valueAsText)
		Tool.Set_Option('FIELD_Y', parameters[2].valueAsText)
		Tool.Set_Option('FORMULA', parameters[3].valueAsText)
		Tool.Set_Option('FORMULAS', parameters[4].valueAsText)
		Tool.Set_Output('TREND', parameters[5].valueAsText, 'table')
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "GWR for Grid Downscaling"
		self.description = "<p>References:</p><p>- Fotheringham, S.A., Brunsdon, C., Charlton, M. (2002): Geographically Weighted Regression: the analysis of spatially varying relationships. John Wiley & Sons. <a target=\"_blank\" href=\"http://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.2003.tb01114.x/abstract\">online</a>.</p><p></p><p>- Fotheringham, S.A., Charlton, M., Brunsdon, C. (1998): Geographically weighted regression: a natural evolution of the expansion method for spatial data analysis. Environment and Planning A 30(11), 1905–1927. <a target=\"_blank\" href=\"http://www.envplan.com/abstract.cgi?id=a301905\">online</a>.</p><p></p><p>- Lloyd, C. (2010): Spatial Data Analysis - An Introduction for GIS Users. Oxford, 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regression with Residual Correction", name="REG_RESCORR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="DEPENDENT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coefficient of Determination", name="QUALITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regression Parameters", name="MODEL", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Output of Model Parameters", name="MODEL_OUT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "local"
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance [Cells]", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 7.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '14')
		Tool.Set_Input ('PREDICTORS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('REGRESSION', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('REG_RESCORR', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('DEPENDENT', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('QUALITY', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('RESIDUALS', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('MODEL', parameters[6].valueAsText, 'grid_list')
		Tool.Set_Option('MODEL_OUT', parameters[7].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[8].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[9].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[10].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[11].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[12].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Zonal Multiple Regression Analysis (Points and Predictor Grids)"
		self.description = "<p>Linear regression analysis of point attributes using multiple predictor grids. Details of the regression/correlation analysis will be saved to a table. The regression function is used to create a new grid with regression based values. The multiple regression analysis uses a forward selection procedure. Each polygon in the zones layer is processed as individual zone. </p><p>Reference:</p><p>- Bahrenberg, G., Giese, E., Nipper, J. (1992): 'Statistische Methoden in der Geographie 2 - Multivariate Statistik', Stuttgart, 415p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Predictors", name="PREDICTORS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Zones", name="ZONES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dependent Variable", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Residuals", name="RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRESSION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Grid Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbor", "Bilinear Interpolation", "Inverse Distance Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
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
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_regression', '15')
		Tool.Set_Input ('PREDICTORS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('ZONES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Input ('POINTS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[3].valueAsText)
		Tool.Set_Output('RESIDUALS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Output('REGRESSION', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('INTERPOL', parameters[6].valueAsText)
		Tool.Set_Option('COORD_X', parameters[7].valueAsText)
		Tool.Set_Option('COORD_Y', parameters[8].valueAsText)
		Tool.Set_Option('INTERCEPT', parameters[9].valueAsText)
		Tool.Set_Option('METHOD', parameters[10].valueAsText)
		Tool.Set_Option('P_VALUE', parameters[11].valueAsText)
		Tool.Run()
		return
