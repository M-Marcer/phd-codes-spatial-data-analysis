import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Segmentation"
		self.alias = ""
		self.tools = [tool_1, tool_2, tool_3]

class tool_1(object):
	def __init__(self):
		self.label = "Grid Skeletonization"
		self.description = "<p>Simple skeletonisation methods for grids.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Skeleton", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Skeleton", name="VECTOR", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Standard", "Hilditch's Algorithm", "Channel Skeleton"]
		param.value = "Standard"
		params += [param]
		param = arcpy.Parameter(displayName="Initialisation", name="INIT_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Less than", "Greater than"]
		param.value = "Greater than"
		params += [param]
		param = arcpy.Parameter(displayName="Threshold (Init.)", name="INIT_THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '1')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('VECTOR', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('INIT_METHOD', parameters[4].valueAsText)
		Tool.Set_Option('INIT_THRESHOLD', parameters[5].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Seed Generation"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Variance", name="VARIANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seeds Grid", name="SEED_GRID", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seed Points", name="SEED_POINTS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seed Type", name="SEED_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["minima of variance", "maxima of variance"]
		param.value = "minima of variance"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["band width smoothing", "band width search"]
		param.value = "band width smoothing"
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth (Cells)", name="BAND_WIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Normalize Features", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
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
		param.value = 5.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '2')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('VARIANCE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SEED_GRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SEED_POINTS', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('SEED_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Set_Option('BAND_WIDTH', parameters[6].valueAsText)
		Tool.Set_Option('NORMALIZE', parameters[7].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[9].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[10].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Seeded Region Growing"
		self.description = "<p></p><p>References:</p><p>Adams, R. & Bischof, L. (1994): Seeded Region Growing. IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol.16, No.6, p.641-647.</p><p></p><p>Bechtel, B., Ringeler, A. & Boehner, J. (2008): Segmentation for Object Extraction of Trees using MATLAB and SAGA. In: Boehner, J., Blaschke, T., Montanarella, L. [Eds.]: SAGA - Seconds Out. Hamburger Beitraege zur Physischen Geographie und Landschaftsoekologie, 19:59-70. <a href=\"http://downloads.sourceforge.net/saga-gis/hbpl19_01.pdf\">download</a></p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Seeds", name="SEEDS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Segments", name="SEGMENTS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Similarity", name="SIMILARITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seeds", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="NEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["4 (von Neumann)", "8 (Moore)"]
		param.value = "4 (von Neumann)"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["feature space and position", "feature space"]
		param.value = "feature space and position"
		params += [param]
		param = arcpy.Parameter(displayName="Variance in Feature Space", name="SIG_1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Variance in Position Space", name="SIG_2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Similarity Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Refresh", name="REFRESH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Leaf Size (for Speed Optimisation)", name="LEAFSIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 256
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '3')
		Tool.Set_Input ('SEEDS', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('FEATURES', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('SEGMENTS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SIMILARITY', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('TABLE', parameters[4].valueAsText, 'table')
		Tool.Set_Option('NORMALIZE', parameters[5].valueAsText)
		Tool.Set_Option('NEIGHBOUR', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Set_Option('SIG_1', parameters[8].valueAsText)
		Tool.Set_Option('SIG_2', parameters[9].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[10].valueAsText)
		Tool.Set_Option('REFRESH', parameters[11].valueAsText)
		Tool.Set_Option('LEAFSIZE', parameters[12].valueAsText)
		Tool.Run()
		return
