import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tool Chains"
		self.alias = ""
		self.tools = [tool_1, tool_2, tool_3, tool_4]

class tool_1(object):
	def __init__(self):
		self.label = "Local Climate Zone Classification"
		self.description = "<p>  Reference:</p><p>  Bechtel, B., Alexander, P. J., Böhner, J., Ching, J., Conrad, O., Feddema, J., Gerald, M., See, L., Stewart, I. (2015). Mapping local climate zones for a worldwide database of the form and function of cities. ISPRS International Journal of Geo-Information, 4(1), 199-219. doi:10.3390/ijgi4010199.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Training Areas", name="FILE_TRAINING", direction="Input", parameterType="Optional", datatype="DEFile")
		params  = [param]
		param = arcpy.Parameter(displayName="Random Forest Tree Count", name="RF_TREE_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 32
		params += [param]
		param = arcpy.Parameter(displayName="Majority Filter Radius", name="FILTER_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Class Definition File", name="FILE_CLASS_DEF", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Save LCZC as...", name="FILE_LCZC", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Save LCZC (Filtered) as...", name="FILE_LCZC_FILTERED", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="LCZC", name="LCZC", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LCZC (Filtered)", name="LCZC_FILTERED", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('toolchains', 'lczc')
		Tool.Set_Option('FILE_TRAINING', parameters[0].valueAsText)
		Tool.Set_Option('RF_TREE_COUNT', parameters[1].valueAsText)
		Tool.Set_Option('FILTER_RADIUS', parameters[2].valueAsText)
		Tool.Set_Option('FILE_CLASS_DEF', parameters[3].valueAsText)
		Tool.Set_Option('FILE_LCZC', parameters[4].valueAsText)
		Tool.Set_Option('FILE_LCZC_FILTERED', parameters[5].valueAsText)
		Tool.Set_Input ('FEATURES', parameters[6].valueAsText, 'grid_list')
		Tool.Set_Output('LCZC', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('LCZC_FILTERED', parameters[8].valueAsText, 'grid')
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Object Based Image Segmentation"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Objects", name="OBJECTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band Width", name="SEEDS_BAND_WIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Generalization", name="MAJORITY_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Number of Clusters", name="NCLUSTER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 12
		params += [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('toolchains', 'obia')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OBJECTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('SEEDS_BAND_WIDTH', parameters[2].valueAsText)
		Tool.Set_Option('MAJORITY_RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('NCLUSTER', parameters[4].valueAsText)
		Tool.Set_Option('NORMALIZE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Contour Lines from Points"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Contour Lines", name="CONTOUR", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Precision", name="CELL_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Equidistance", name="ZSTEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('toolchains', 'PointsToContour')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('CONTOUR', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[2].valueAsText)
		Tool.Set_Option('CELL_SIZE', parameters[3].valueAsText)
		Tool.Set_Option('ZSTEP', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Sieve and Clump"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classes", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sieve and Clump", name="FILTERED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sieving Threshold", name="SIEVE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Expansion Distance", name="EXPAND", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('toolchains', 'SieveAndClump')
		Tool.Set_Input ('CLASSES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('FILTERED', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SIEVE', parameters[2].valueAsText)
		Tool.Set_Option('EXPAND', parameters[3].valueAsText)
		Tool.Run()
		return
