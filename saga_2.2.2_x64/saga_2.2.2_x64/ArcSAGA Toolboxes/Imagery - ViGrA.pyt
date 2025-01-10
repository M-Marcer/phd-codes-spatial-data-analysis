import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "ViGrA"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10]

class tool_0(object):
	def __init__(self):
		self.label = "Smoothing (ViGrA)"
		self.description = "<p>Based on the example code \"smooth.cxx\" by Ullrich Koethe.</p><p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Type of smoothing", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["exponential", "nonlinear", "gaussian"]
		param.value = "exponential"
		params += [param]
		param = arcpy.Parameter(displayName="Size of smoothing filter", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Edge threshold for nonlinear smoothing", name="EDGE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Option('SCALE', parameters[3].valueAsText)
		Tool.Set_Option('EDGE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Edge Detection (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Edges", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Detector type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Canny", "Shen-Castan"]
		param.value = "Canny"
		params += [param]
		param = arcpy.Parameter(displayName="Operator scale", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Gradient threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '1')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Option('SCALE', parameters[3].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Morphological Filter (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Dilation", "Erosion", "Median", "User defined rank"]
		param.value = "Dilation"
		params += [param]
		param = arcpy.Parameter(displayName="Radius (cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="User defined rank", name="RANK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Values (0-255)", name="RESCALE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '2')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('RANK', parameters[4].valueAsText)
		Tool.Set_Option('RESCALE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Distance (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Distance", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Type of distance calculation", name="NORM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Chessboard", "Manhattan", "Euclidean"]
		param.value = "Chessboard"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '3')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('NORM', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Watershed Segmentation (ViGrA)"
		self.description = "<p>Note that the watershed algorithm usually results in an oversegmentation (i.e., too many regions), but its boundary localization is quite good.</p><p>Based on the example code \"watershed.cxx\" by Ullrich Koethe.</p><p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Segmentation", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Width of gradient filter", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="RGB coded data", name="RGB", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Edges", name="EDGES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '4')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SCALE', parameters[2].valueAsText)
		Tool.Set_Option('RGB', parameters[3].valueAsText)
		Tool.Set_Option('EDGES', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Fourier Transform (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Real", name="REAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Imaginary", name="IMAG", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Centered", name="CENTER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '5')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('REAL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('IMAG', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CENTER', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Fourier Transform Inverse (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Real", name="REAL", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Imaginary", name="IMAG", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Centered", name="CENTER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '6')
		Tool.Set_Input ('REAL', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('IMAG', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CENTER', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Fourier Transform (Real, ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '7')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Fourier Filter (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Size of smoothing filter", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.900000
		params += [param]
		param = arcpy.Parameter(displayName="Filter", name="FILTER", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["gaussian", "power of distance", "include range", "exclude range"]
		param.value = "gaussian"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '8')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SCALE', parameters[2].valueAsText)
		Tool.Set_Option('POWER', parameters[3].valueAsText)
		Tool.Set_Option('RANGE_MIN', parameters[4].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[5].valueAsText)
		Tool.Set_Option('FILTER', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Random Forest Classification (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Random Forest Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Prediction Probability", name="PROBABILITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Feature Probabilities", name="BPROBABILITIES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Feature Probabilities", name="PROBABILITIES", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAINING", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Label Field", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAINING"]
		params += [param]
		param = arcpy.Parameter(displayName="Use Label as Identifier", name="LABEL_AS_ID", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Redundancy Feature Selection", name="DO_MRMR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Number of Features", name="mRMR_NFEATURES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 50
		params += [param]
		param = arcpy.Parameter(displayName="Discretization", name="mRMR_DISCRETIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Discretization Threshold", name="mRMR_THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Selection Method", name="mRMR_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Mutual Information Difference (MID)", "Mutual Information Quotient (MIQ)"]
		param.value = "Mutual Information Difference (MID)"
		params += [param]
		param = arcpy.Parameter(displayName="Import from File", name="RF_IMPORT", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Export to File", name="RF_EXPORT", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Tree Count", name="RF_TREE_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 32
		params += [param]
		param = arcpy.Parameter(displayName="Samples per Tree", name="RF_TREE_SAMPLES", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Sample with Replacement", name="RF_REPLACE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Node Split Size", name="RF_SPLIT_MIN_SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Features per Node", name="RF_NODE_FEATURES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["logarithmic", "square root", "all"]
		param.value = "square root"
		params += [param]
		param = arcpy.Parameter(displayName="Stratification", name="RF_STRATIFICATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "equal", "proportional"]
		param.value = "none"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '9')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('CLASSES', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('PROBABILITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('BPROBABILITIES', parameters[3].valueAsText)
		Tool.Set_Output('PROBABILITIES', parameters[4].valueAsText, 'grid_list')
		Tool.Set_Input ('TRAINING', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[6].valueAsText)
		Tool.Set_Option('LABEL_AS_ID', parameters[7].valueAsText)
		Tool.Set_Option('DO_MRMR', parameters[8].valueAsText)
		Tool.Set_Option('mRMR_NFEATURES', parameters[9].valueAsText)
		Tool.Set_Option('mRMR_DISCRETIZE', parameters[10].valueAsText)
		Tool.Set_Option('mRMR_THRESHOLD', parameters[11].valueAsText)
		Tool.Set_Option('mRMR_METHOD', parameters[12].valueAsText)
		Tool.Set_Option('RF_IMPORT', parameters[13].valueAsText)
		Tool.Set_Option('RF_EXPORT', parameters[14].valueAsText)
		Tool.Set_Option('RF_TREE_COUNT', parameters[15].valueAsText)
		Tool.Set_Option('RF_TREE_SAMPLES', parameters[16].valueAsText)
		Tool.Set_Option('RF_REPLACE', parameters[17].valueAsText)
		Tool.Set_Option('RF_SPLIT_MIN_SIZE', parameters[18].valueAsText)
		Tool.Set_Option('RF_NODE_FEATURES', parameters[19].valueAsText)
		Tool.Set_Option('RF_STRATIFICATION', parameters[20].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Random Forest Presence Prediction (ViGrA)"
		self.description = "<p>References:</p><p>ViGrA - Vision with Generic Algorithms</p><p><a target=\"_blank\" href=\"http://hci.iwr.uni-heidelberg.de/vigra\">http://hci.iwr.uni-heidelberg.de</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Presence Prediction", name="PREDICTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Presence Probability", name="PROBABILITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Presence Data", name="PRESENCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Background Sample Density [Percent]", name="BACKGROUND", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Redundancy Feature Selection", name="DO_MRMR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Number of Features", name="mRMR_NFEATURES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 50
		params += [param]
		param = arcpy.Parameter(displayName="Discretization", name="mRMR_DISCRETIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Discretization Threshold", name="mRMR_THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Selection Method", name="mRMR_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Mutual Information Difference (MID)", "Mutual Information Quotient (MIQ)"]
		param.value = "Mutual Information Difference (MID)"
		params += [param]
		param = arcpy.Parameter(displayName="Import from File", name="RF_IMPORT", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Export to File", name="RF_EXPORT", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Tree Count", name="RF_TREE_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 32
		params += [param]
		param = arcpy.Parameter(displayName="Samples per Tree", name="RF_TREE_SAMPLES", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Sample with Replacement", name="RF_REPLACE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Node Split Size", name="RF_SPLIT_MIN_SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Features per Node", name="RF_NODE_FEATURES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["logarithmic", "square root", "all"]
		param.value = "square root"
		params += [param]
		param = arcpy.Parameter(displayName="Stratification", name="RF_STRATIFICATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "equal", "proportional"]
		param.value = "none"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_vigra', '10')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('PREDICTION', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('PROBABILITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('PRESENCE', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('BACKGROUND', parameters[4].valueAsText)
		Tool.Set_Option('DO_MRMR', parameters[5].valueAsText)
		Tool.Set_Option('mRMR_NFEATURES', parameters[6].valueAsText)
		Tool.Set_Option('mRMR_DISCRETIZE', parameters[7].valueAsText)
		Tool.Set_Option('mRMR_THRESHOLD', parameters[8].valueAsText)
		Tool.Set_Option('mRMR_METHOD', parameters[9].valueAsText)
		Tool.Set_Option('RF_IMPORT', parameters[10].valueAsText)
		Tool.Set_Option('RF_EXPORT', parameters[11].valueAsText)
		Tool.Set_Option('RF_TREE_COUNT', parameters[12].valueAsText)
		Tool.Set_Option('RF_TREE_SAMPLES', parameters[13].valueAsText)
		Tool.Set_Option('RF_REPLACE', parameters[14].valueAsText)
		Tool.Set_Option('RF_SPLIT_MIN_SIZE', parameters[15].valueAsText)
		Tool.Set_Option('RF_NODE_FEATURES', parameters[16].valueAsText)
		Tool.Set_Option('RF_STRATIFICATION', parameters[17].valueAsText)
		Tool.Run()
		return
