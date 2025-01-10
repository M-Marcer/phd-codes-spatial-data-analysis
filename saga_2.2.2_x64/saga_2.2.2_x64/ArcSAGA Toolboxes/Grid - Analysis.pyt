import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Analysis"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18, tool_19]

class tool_0(object):
	def __init__(self):
		self.label = "Accumulated Cost (Isotropic)"
		self.description = "<p>(c) 2004 by Victor Olaya. Calculate Accumulated Cost (Isotropic)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Cost Grid", name="COST", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Destination Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Cost", name="ACCCOST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Closest Point", name="CLOSESTPT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for different route", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '0')
		Tool.Set_Input ('COST', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('POINTS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ACCCOST', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLOSESTPT', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Accumulated Cost (Anisotropic)"
		self.description = "<p>(c) 2004 by Victor Olaya. Calculate Accumulated Cost (Anisotropic)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Cost Grid", name="COST", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Direction of max cost", name="DIRECTION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Destination Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Cost", name="ACCCOST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="k factor", name="K", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for different route", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '1')
		Tool.Set_Input ('COST', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DIRECTION', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('POINTS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('ACCCOST', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('K', parameters[4].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Least Cost Paths"
		self.description = "<p>This module allows one to compute least cost path profile(s). It takes an accumulated cost surface grid and a point shapefile as input. Each point in the shapefile represents a source for which the least cost path is calculated.</p><p>In case the point shapefile has more than one source point defined, a separate least cost path is calculated for each point. The module outputs a point and a line shapefile for each least cost path.</p><p> The module allows for optional input grids. The cell values of these grids along the least cost path are written to the outputs as additional table fields.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Source Point(s)", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Accumulated cost", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Values", name="VALUES", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Profile (points)", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Profile (lines)", name="LINE", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '5')
		Tool.Set_Input ('SOURCE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('DEM', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('VALUES', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('POINTS', parameters[3].valueAsText, 'shapes_list')
		Tool.Set_Output('LINE', parameters[4].valueAsText, 'shapes_list')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Change Vector Analysis"
		self.description = "<p>This module performs a change vector analysis (CVA) for the given input features. Input features are supplied as grid lists for initial and final state. In both lists features have to be given in the same order. Distance is measured as Euclidean distance in features space. When analyzing two features direction is calculated as angle (radians) by default. Otherwise direction is coded as the quadrant it points to in terms of feature space. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Initial State", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Final State", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DIST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Angle Calculation", name="ANGLE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Output of Change Vector", name="C_OUT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Change Vector", name="C", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '6')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('DIST', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DIR', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('ANGLE', parameters[4].valueAsText)
		Tool.Set_Option('C_OUT', parameters[5].valueAsText)
		Tool.Set_Output('C', parameters[6].valueAsText, 'grid_list')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Covered Distance"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Covered Distance", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '7')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Pattern Analysis"
		self.description = "<p>(c) 2004 by Victor Olaya. Pattern Analysis<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Relative Richness", name="RELATIVE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Diversity", name="DIVERSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dominance", name="DOMINANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Different Classes", name="NDC", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Center Versus Neighbours", name="CVN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Size of Analysis Window", name="WINSIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["3 X 3", "5 X 5", "7 X 7"]
		param.value = "3 X 3"
		params += [param]
		param = arcpy.Parameter(displayName="Max. Number of Classes", name="MAXNUMCLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '8')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RELATIVE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIVERSITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DOMINANCE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('NDC', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('CVN', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('WINSIZE', parameters[7].valueAsText)
		Tool.Set_Option('MAXNUMCLASS', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Layer of extreme value"
		self.description = "<p>It creates a new grid containing the ID of the grid with the maximum (minimum) value.</p><p>Copyright 2005 Victor Olaya: e-mail: volaya@ya.com<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="CRITERIA", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Maximum", "Minimum"]
		param.value = "Maximum"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '9')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('CRITERIA', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Analytical Hierarchy Process"
		self.description = "<p>(c) 2004 by Victor Olaya. Analytical Hierarchy Process<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Pairwise Comparisons Table ", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Output Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '10')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TABLE', parameters[1].valueAsText, 'table')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Ordered Weighted Averaging (OWA)"
		self.description = "<p>(c) 2006 by Victor Olaya. Ordered Weighted Averaging (OWA)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		param = arcpy.Parameter(displayName="Output Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '11')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('WEIGHTS', parameters[1].valueAsText)
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Aggregation Index"
		self.description = "<p>(c) 2004 by Victor Olaya. Aggregation Index</p><p>References:</p><p>1. Hong S. He, et al. An aggregation index to quantify spatial patterns of landscapes, Landscape Ecology 15, 591-601,2000</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Max. Number of Classes", name="MAXNUMCLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '12')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('MAXNUMCLASS', parameters[1].valueAsText)
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'table')
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Cross-Classification and Tabulation"
		self.description = "<p>(c) 2004 by Victor Olaya. Cross-Classification and Tabulation<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid 1", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Input Grid 2", name="INPUT2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Classification Grid", name="RESULTGRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Tabulation Table", name="RESULTTABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Max. Number of Classes", name="MAXNUMCLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '13')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('INPUT2', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULTGRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('RESULTTABLE', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MAXNUMCLASS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Soil Texture Classification"
		self.description = "<p>Derive soil texture classes with USDA scheme from sand, silt and clay contents.</p><p></p><p>  1 - Clay</p><p>  2 - Silty Clay</p><p>  3 - Silty Clay Loam</p><p>  4 - Sandy Clay</p><p>  5 - Sandy Clay Loam</p><p>  6 - Clay Loam</p><p>  7 - Silt</p><p>  8 - Silt Loam</p><p>  9 - Loam</p><p> 10 - Sand</p><p> 11 - Loamy Sand</p><p> 12 - Sandy Loam</p><p></p><p>Reference:</p><p><a target=\"_blank\" href=\"http://soils.usda.gov/technical/aids/investigations/texture/\">USDA NRCS Soils Website</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Sand", name="SAND", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Silt", name="SILT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Clay", name="CLAY", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Texture", name="TEXTURE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '14')
		Tool.Set_Input ('SAND', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SILT', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('CLAY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('TEXTURE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('SUM', parameters[4].valueAsText, 'grid')
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Fragmentation (Standard)"
		self.description = "<p>Grid based fragmentation analysis after Riitters et al. (2000).</p><p></p><p>(1) interior, if Density = 1.0</p><p>(2) undetermined, if Density > 0.6 and Density = Connectivity</p><p>(3) perforated, if Density > 0.6 and Density - Connectivity > 0</p><p>(4) edge, if Density > 0.6 and Density - Connectivity < 0</p><p>(5) transitional, if 0.4 < Density < 0.6</p><p>(6) patch, if Density < 0.4</p><p></p><p></p><p>References:</p><p>Riitters, K., Wickham, J., O'Neill, R., Jones, B., Smith, E. (2000): </p><p>Global-scale patterns of forest fragmentation. Conservation Ecology 4(2): 3</p><p><a href=\"http://www.ecologyandsociety.org/vol4/iss2/art3/\">http://www.ecologyandsociety.org/vol4/iss2/art3/</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Density [Percent]", name="DENSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity [Percent]", name="CONNECTIVITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Summary", name="FRAGSTATS", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="CLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Minimum)", name="NEIGHBORHOOD_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Maximum)", name="NEIGHBORHOOD_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Level Aggregation", name="AGGREGATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["average", "multiplicative"]
		param.value = "average"
		params += [param]
		param = arcpy.Parameter(displayName="Add Border", name="BORDER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Weighting", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density [Percent]", name="DENSITY_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density for Interior Forest [Percent]", name="DENSITY_INT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood Type", name="CIRCULAR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["square", "circle"]
		param.value = "circle"
		params += [param]
		param = arcpy.Parameter(displayName="Include diagonal neighbour relations", name="DIAGONAL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '15')
		Tool.Set_Input ('CLASSES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DENSITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CONNECTIVITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('FRAGSTATS', parameters[4].valueAsText, 'table')
		Tool.Set_Option('CLASS', parameters[5].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MIN', parameters[6].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MAX', parameters[7].valueAsText)
		Tool.Set_Option('AGGREGATION', parameters[8].valueAsText)
		Tool.Set_Option('BORDER', parameters[9].valueAsText)
		Tool.Set_Option('WEIGHT', parameters[10].valueAsText)
		Tool.Set_Option('DENSITY_MIN', parameters[11].valueAsText)
		Tool.Set_Option('DENSITY_INT', parameters[12].valueAsText)
		Tool.Set_Option('CIRCULAR', parameters[13].valueAsText)
		Tool.Set_Option('DIAGONAL', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Fragmentation (Alternative)"
		self.description = "<p></p><p>(1) interior, if Density = 1.0</p><p>(2) undetermined, if Density > 0.6 and Density = Connectivity</p><p>(3) perforated, if Density > 0.6 and Density - Connectivity > 0</p><p>(4) edge, if Density > 0.6 and Density - Connectivity < 0</p><p>(5) transitional, if 0.4 < Density < 0.6</p><p>(6) patch, if Density < 0.4</p><p></p><p></p><p>References:</p><p>Riitters, K., Wickham, J., O'Neill, R., Jones, B., Smith, E. (2000): </p><p>Global-scale patterns of forest fragmentation. Conservation Ecology 4(2): 3</p><p><a href=\"http://www.ecologyandsociety.org/vol4/iss2/art3/\">http://www.ecologyandsociety.org/vol4/iss2/art3/</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Density [Percent]", name="DENSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity [Percent]", name="CONNECTIVITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Summary", name="FRAGSTATS", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="CLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Minimum)", name="NEIGHBORHOOD_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Maximum)", name="NEIGHBORHOOD_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Level Aggregation", name="AGGREGATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["average", "multiplicative"]
		param.value = "average"
		params += [param]
		param = arcpy.Parameter(displayName="Add Border", name="BORDER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Weighting", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density [Percent]", name="DENSITY_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density for Interior Forest [Percent]", name="DENSITY_INT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance Increment", name="LEVEL_GROW", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Density from Neighbourhood", name="DENSITY_MEAN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '16')
		Tool.Set_Input ('CLASSES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DENSITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CONNECTIVITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('FRAGSTATS', parameters[4].valueAsText, 'table')
		Tool.Set_Option('CLASS', parameters[5].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MIN', parameters[6].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MAX', parameters[7].valueAsText)
		Tool.Set_Option('AGGREGATION', parameters[8].valueAsText)
		Tool.Set_Option('BORDER', parameters[9].valueAsText)
		Tool.Set_Option('WEIGHT', parameters[10].valueAsText)
		Tool.Set_Option('DENSITY_MIN', parameters[11].valueAsText)
		Tool.Set_Option('DENSITY_INT', parameters[12].valueAsText)
		Tool.Set_Option('LEVEL_GROW', parameters[13].valueAsText)
		Tool.Set_Option('DENSITY_MEAN', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Fragmentation Classes from Density and Connectivity"
		self.description = "<p></p><p>(1) interior, if Density = 1.0</p><p>(2) undetermined, if Density > 0.6 and Density = Connectivity</p><p>(3) perforated, if Density > 0.6 and Density - Connectivity > 0</p><p>(4) edge, if Density > 0.6 and Density - Connectivity < 0</p><p>(5) transitional, if 0.4 < Density < 0.6</p><p>(6) patch, if Density < 0.4</p><p></p><p></p><p>References:</p><p>Riitters, K., Wickham, J., O'Neill, R., Jones, B., Smith, E. (2000): </p><p>Global-scale patterns of forest fragmentation. Conservation Ecology 4(2): 3</p><p><a href=\"http://www.ecologyandsociety.org/vol4/iss2/art3/\">http://www.ecologyandsociety.org/vol4/iss2/art3/</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Density [Percent]", name="DENSITY", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Connectivity [Percent]", name="CONNECTIVITY", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Add Border", name="BORDER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Weighting", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density [Percent]", name="DENSITY_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density for Interior Forest [Percent]", name="DENSITY_INT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '17')
		Tool.Set_Input ('DENSITY', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CONNECTIVITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('BORDER', parameters[3].valueAsText)
		Tool.Set_Option('WEIGHT', parameters[4].valueAsText)
		Tool.Set_Option('DENSITY_MIN', parameters[5].valueAsText)
		Tool.Set_Option('DENSITY_INT', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Accumulation Functions"
		self.description = "<p>Provides \"accumulation functions\" that can be used to e.g. move material over a \"local drain direction\" (LDD) network. The LDD net is computed for the supplied surface by MFD and D8 flow-routing algorithms. It is possible to switch from MFD to D8 as soon as a threshold is exceeded.</p><p>The input to each cell on the grid can be supplied from e.g. time series and the material can be moved over the net in several ways. All of these, except the \"accuflux\" operation, compute both the flux and the state for a given cell. For time series modelling (batch processing), the state of each cell at time t can be initialized with the previous state t - 1.</p><p>The capacity, fraction, threshold and trigger operations compute the fluxes and cell states at time t + 1 according to cell-specific parameters that control the way the flux is computed. The capacity function limits the cell-to-cell flux by a (channel) capacity control; the fraction function transports only a given proportion of material from cell to cell, the threshold function transports material only once a given threshold has been exceeded, and the trigger function transports nothing until a trigger value has been exceeded (at which point all accumulated material in the state of the cell is discharged to its downstream neighbour(s)).</p><p></p><p>The following operations are supported:</p><p></p><p> * ACCUFLUX: The accuflux function computes the new state of the attributes for the cell as the sum of the input cell values plus the cumulative sum of all upstream elements draining through the cell.</p><p></p><p> * ACCUCAPACITYFLUX / STATE: The operation modifies the accumulation of flow over the network by a limiting transport capacity given in absolute values.</p><p></p><p> * ACCUFRACTIONFLUX / STATE: The operation limits the flow over the network by a parameter which controls the proportion (0-1) of the material that can flow through each cell.</p><p></p><p> * ACCUTHRESHOLDFLUX / STATE: The operation modifies the accummulation of flow over the network by limiting transport to values greater than a minimum threshold value per cell. No flow occurs if the threshold is not exceeded.</p><p></p><p> * ACCUTRIGGERFLUX / STATE: The operation only allows transport (flux) to occur if a trigger value is exceeded, otherwise no transport occurs and storage accumulates.</p><p></p><p>References:</p><p>BURROUGH, P.A. (1998): Dynamic Modelling and Geocomputation.- In: LONGLEY, P.A., BROOKS, S.M., MCDONNELL, R. & B. MACMILLAN [Eds.]: Geocomputation: A Primer. John Wiley & Sons, pp. 165-191.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Surface", name="SURFACE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State t", name="STATE_IN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation Control", name="CONTROL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Linear Flow Control Grid", name="CTRL_LINEAR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flux", name="FLUX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State t + 1", name="STATE_OUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation", name="OPERATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["accuflux", "accucapacityflux / state", "accufractionflux / state", "accuthresholdflux / state", "accutriggerflux / state"]
		param.value = "accuflux"
		params += [param]
		param = arcpy.Parameter(displayName="Switch to Linear Flow", name="LINEAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Linear Flow", name="THRES_LINEAR", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '18')
		Tool.Set_Input ('SURFACE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('INPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('STATE_IN', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('CONTROL', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('CTRL_LINEAR', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('FLUX', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('STATE_OUT', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('OPERATION', parameters[7].valueAsText)
		Tool.Set_Option('LINEAR', parameters[8].valueAsText)
		Tool.Set_Option('THRES_LINEAR', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "IMCORR - Feature Tracking"
		self.description = "<p>The module performs an image correlation based on two raster data sets.</p><p>Additionally, two DTMs can be given and used to optain 3D displacement vectors.</p><p></p><p>This is a SAGA implementation of the standalone IMCORR software provided by the National Snow and Ice Data Center in Boulder, Colorado / US.</p><p></p><p>The standalone software and documentation is available from:</p><p><a href=\"http://nsidc.org/data/velmap/imcorr.html\">http://nsidc.org/data/velmap/imcorr.html</a></p><p></p><p>References:</p><p>Scambos, T. A., Dutkiewicz, M. J., Wilson, J. C., and R. A. Bindschadler (1992): Application of image cross-correlation to the measurement of glacier velocity using satellite image data. Remote Sensing Environ., 42(3), 177-186.</p><p></p><p>Fahnestock, M. A., Scambos, T.A., and R. A. Bindschadler (1992): Semi-automated ice velocity determination from satellite imagery. Eos, 73, 493.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid 1", name="GRID_1", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Grid 2", name="GRID_2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DTM 1", name="DTM_1", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DTM 2", name="DTM_2", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Correlated Points", name="CORRPOINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Displacement Vector", name="CORRLINES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Chip Size (Cells)", name="SEARCH_CHIPSIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["16x16", "32x32", "64x64", "128x128", "256x256"]
		param.value = "64x64"
		params += [param]
		param = arcpy.Parameter(displayName="Reference Chip Size (Cells)", name="REF_CHIPSIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["16x16", "32x32", "64x64", "128x128"]
		param.value = "32x32"
		params += [param]
		param = arcpy.Parameter(displayName="Grid Spacing (Map Units)", name="GRID_SPACING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '19')
		Tool.Set_Input ('GRID_1', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRID_2', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('DTM_1', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('DTM_2', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CORRPOINTS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Output('CORRLINES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('SEARCH_CHIPSIZE', parameters[6].valueAsText)
		Tool.Set_Option('REF_CHIPSIZE', parameters[7].valueAsText)
		Tool.Set_Option('GRID_SPACING', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Soil Texture Classification for Tables"
		self.description = "<p>Derive soil texture classes with USDA scheme from sand, silt and clay contents.</p><p></p><p>  1 - Clay</p><p>  2 - Silty Clay</p><p>  3 - Silty Clay Loam</p><p>  4 - Sandy Clay</p><p>  5 - Sandy Clay Loam</p><p>  6 - Clay Loam</p><p>  7 - Silt</p><p>  8 - Silt Loam</p><p>  9 - Loam</p><p> 10 - Sand</p><p> 11 - Loamy Sand</p><p> 12 - Sandy Loam</p><p></p><p>Reference:</p><p><a target=\"_blank\" href=\"http://soils.usda.gov/technical/aids/investigations/texture/\">USDA NRCS Soils Website</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Sand", name="SAND", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Silt", name="SILT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Clay", name="CLAY", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Texture", name="TEXTURE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '20')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('SAND', parameters[1].valueAsText)
		Tool.Set_Option('SILT', parameters[2].valueAsText)
		Tool.Set_Option('CLAY', parameters[3].valueAsText)
		Tool.Set_Option('TEXTURE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Diversity of Categories"
		self.description = "<p>Grid based analysis of diversity. It is assumed that the input grid provides a classification (i.e. not a contiuous field). For each cell it counts the number of different categories (classes) as well as the connectivity within the chosen search window. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Categories", name="CATEGORIES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Categories", name="DIVERSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Average Size", name="SIZE_MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Skewness", name="SIZE_SKEW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity", name="CONNECTIVITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Mode", name="SEARCH_MODE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Neighbourhood", name="NB_CASE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rook's case", "Queen's case"]
		param.value = "Queen's case"
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
		param.value = 0.700000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '21')
		Tool.Set_Input ('CATEGORIES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DIVERSITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SIZE_MEAN', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SIZE_SKEW', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CONNECTIVITY', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('SEARCH_MODE', parameters[5].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[6].valueAsText)
		Tool.Set_Option('NB_CASE', parameters[7].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[9].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[10].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[11].valueAsText)
		Tool.Run()
		return
