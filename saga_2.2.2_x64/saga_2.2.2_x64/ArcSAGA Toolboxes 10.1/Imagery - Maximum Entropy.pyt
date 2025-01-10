import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Maximum Entropy"
		self.alias = ""
		self.tools = [tool_0, tool_1]

class tool_0(object):
	def __init__(self):
		self.label = "Maximum Entropy Classifcation"
		self.description = "<p></p><p>References:</p><p>- Yoshimasa Tsuruoka: A simple C++ library for maximum entropy classification.  <a target=\"_blank\" href=\"http://www.logos.t.u-tokyo.ac.jp/~tsuruoka/maxent/\">online</a>.</p><p>- Dekang Lin: A MaxEnt Package in C++.  <a target=\"_blank\" href=\"http://webdocs.cs.ualberta.ca/~lindek/downloads.htm\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Training Areas", name="TRAINING", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Class Name", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAINING"]
		params += [param]
		param = arcpy.Parameter(displayName="Numerical Features", name="FEATURES_NUM", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Categorical Features", name="FEATURES_CAT", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Classes", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Probability", name="PROB", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Probabilities", name="PROBS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Create Propabilities", name="PROBS_CREATE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Yoshimasa Tsuruoka", "Dekang Lin"]
		param.value = "Yoshimasa Tsuruoka"
		params += [param]
		param = arcpy.Parameter(displayName="Load from File...", name="YT_FILE_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Save to File...", name="YT_FILE_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Regularization", name="YT_REGUL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "L1", "L2"]
		param.value = "L1"
		params += [param]
		param = arcpy.Parameter(displayName="Regularization Factor", name="YT_REGUL_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Real-valued Numerical Features", name="YT_NUMASREAL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Alpha", name="DL_ALPHA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="DL_THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Iterations", name="DL_ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Number of Numeric Value Classes", name="NUM_CLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 32
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Probability", name="PROB_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_maxent', '0')
		Tool.Set_Input ('TRAINING', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Input ('FEATURES_NUM', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('FEATURES_CAT', parameters[3].valueAsText, 'grid_list')
		Tool.Set_Output('CLASSES', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('PROB', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('PROBS', parameters[6].valueAsText, 'grid_list')
		Tool.Set_Option('PROBS_CREATE', parameters[7].valueAsText)
		Tool.Set_Option('METHOD', parameters[8].valueAsText)
		Tool.Set_Option('YT_FILE_LOAD', parameters[9].valueAsText)
		Tool.Set_Option('YT_FILE_SAVE', parameters[10].valueAsText)
		Tool.Set_Option('YT_REGUL', parameters[11].valueAsText)
		Tool.Set_Option('YT_REGUL_VAL', parameters[12].valueAsText)
		Tool.Set_Option('YT_NUMASREAL', parameters[13].valueAsText)
		Tool.Set_Option('DL_ALPHA', parameters[14].valueAsText)
		Tool.Set_Option('DL_THRESHOLD', parameters[15].valueAsText)
		Tool.Set_Option('DL_ITERATIONS', parameters[16].valueAsText)
		Tool.Set_Option('NUM_CLASSES', parameters[17].valueAsText)
		Tool.Set_Option('PROB_MIN', parameters[18].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Maximum Entropy Presence Prediction"
		self.description = "<p></p><p>References:</p><p>- Yoshimasa Tsuruoka: A simple C++ library for maximum entropy classification.  <a target=\"_blank\" href=\"http://www.logos.t.u-tokyo.ac.jp/~tsuruoka/maxent/\">online</a>.</p><p>- Dekang Lin: A MaxEnt Package in C++.  <a target=\"_blank\" href=\"http://webdocs.cs.ualberta.ca/~lindek/downloads.htm\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Presence Data", name="PRESENCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Numerical Features", name="FEATURES_NUM", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Categorical Features", name="FEATURES_CAT", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Presence Prediction", name="PREDICTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Presence Probability", name="PROBABILITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Background Sample Density [Percent]", name="BACKGROUND", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Yoshimasa Tsuruoka", "Dekang Lin"]
		param.value = "Yoshimasa Tsuruoka"
		params += [param]
		param = arcpy.Parameter(displayName="Load from File...", name="YT_FILE_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Save to File...", name="YT_FILE_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Regularization", name="YT_REGUL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "L1", "L2"]
		param.value = "L1"
		params += [param]
		param = arcpy.Parameter(displayName="Regularization Factor", name="YT_REGUL_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Real-valued Numerical Features", name="YT_NUMASREAL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Alpha", name="DL_ALPHA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="DL_THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Iterations", name="DL_ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Number of Numeric Value Classes", name="NUM_CLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 32
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_maxent', '1')
		Tool.Set_Input ('PRESENCE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('FEATURES_NUM', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('FEATURES_CAT', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('PREDICTION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('PROBABILITY', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('BACKGROUND', parameters[5].valueAsText)
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Set_Option('YT_FILE_LOAD', parameters[7].valueAsText)
		Tool.Set_Option('YT_FILE_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('YT_REGUL', parameters[9].valueAsText)
		Tool.Set_Option('YT_REGUL_VAL', parameters[10].valueAsText)
		Tool.Set_Option('YT_NUMASREAL', parameters[11].valueAsText)
		Tool.Set_Option('DL_ALPHA', parameters[12].valueAsText)
		Tool.Set_Option('DL_THRESHOLD', parameters[13].valueAsText)
		Tool.Set_Option('DL_ITERATIONS', parameters[14].valueAsText)
		Tool.Set_Option('NUM_CLASSES', parameters[15].valueAsText)
		Tool.Run()
		return
