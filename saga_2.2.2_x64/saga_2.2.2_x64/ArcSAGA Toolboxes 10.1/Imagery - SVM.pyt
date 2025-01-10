import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "SVM"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "SVM Classification"
		self.description = "<p>Support Vector Machine (SVM) based classification for grids.</p><p>Reference:</p><p>Chang, C.-C. / Lin, C.-J. (2011): A library for support vector machines. ACM Transactions on Intelligent Systems and Technology, vol.2/3, p.1-27. <a target=\"_blank\" href=\"http://www.csie.ntu.edu.tw/~cjlin/libsvm\">LIBSVM Homepage</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scaling", name="SCALING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "normalize (0-1)", "standardize"]
		param.value = "standardize"
		params += [param]
		param = arcpy.Parameter(displayName="Verbose Messages", name="MESSAGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Model Source", name="MODEL_SRC", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["create from training areas", "restore from file"]
		param.value = "create from training areas"
		params += [param]
		param = arcpy.Parameter(displayName="Restore Model from File", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="ROI", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="ROI_ID", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ROI"]
		params += [param]
		param = arcpy.Parameter(displayName="Store Model to File", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="SVM Type", name="SVM_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["C-SVC", "nu-SVC", "one-class SVM", "epsilon-SVR", "nu-SVR"]
		param.value = "C-SVC"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["linear", "polynomial", "radial basis function", "sigmoid"]
		param.value = "radial basis function"
		params += [param]
		param = arcpy.Parameter(displayName="Degree", name="DEGREE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Gamma", name="GAMMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="coef0", name="COEF0", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="C", name="COST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="nu-SVR", name="NU", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="SVR Epsilon", name="EPS_SVR", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Cache Size", name="CACHE_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Epsilon", name="EPS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.001000
		params += [param]
		param = arcpy.Parameter(displayName="Shrinking", name="SHRINKING", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Probability Estimates", name="PROBABILITY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation", name="CROSSVAL", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_svm', '0')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('CLASSES', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SCALING', parameters[2].valueAsText)
		Tool.Set_Option('MESSAGE', parameters[3].valueAsText)
		Tool.Set_Option('MODEL_SRC', parameters[4].valueAsText)
		Tool.Set_Option('MODEL_LOAD', parameters[5].valueAsText)
		Tool.Set_Input ('ROI', parameters[6].valueAsText, 'shapes')
		Tool.Set_Option('ROI_ID', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('SVM_TYPE', parameters[9].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[10].valueAsText)
		Tool.Set_Option('DEGREE', parameters[11].valueAsText)
		Tool.Set_Option('GAMMA', parameters[12].valueAsText)
		Tool.Set_Option('COEF0', parameters[13].valueAsText)
		Tool.Set_Option('COST', parameters[14].valueAsText)
		Tool.Set_Option('NU', parameters[15].valueAsText)
		Tool.Set_Option('EPS_SVR', parameters[16].valueAsText)
		Tool.Set_Option('CACHE_SIZE', parameters[17].valueAsText)
		Tool.Set_Option('EPS', parameters[18].valueAsText)
		Tool.Set_Option('SHRINKING', parameters[19].valueAsText)
		Tool.Set_Option('PROBABILITY', parameters[20].valueAsText)
		Tool.Set_Option('CROSSVAL', parameters[21].valueAsText)
		Tool.Run()
		return
