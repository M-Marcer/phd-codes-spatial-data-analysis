import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Classification"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_4, tool_5, tool_6]

class tool_0(object):
	def __init__(self):
		self.label = "Supervised Classification for Grids"
		self.description = "<p>Supervised Classification<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalise", name="NORMALISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quality", name="QUALITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAINING", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAINING_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAINING"]
		params += [param]
		param = arcpy.Parameter(displayName="Load Statistics from File...", name="FILE_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Save Statistics to File...", name="FILE_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Binary Encoding", "Parallelepiped", "Minimum Distance", "Mahalanobis Distance", "Maximum Likelihood", "Spectral Angle Mapping", "Winner Takes All"]
		param.value = "Minimum Distance"
		params += [param]
		param = arcpy.Parameter(displayName="Distance Threshold", name="THRESHOLD_DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Angle Threshold (Degree)", name="THRESHOLD_ANGLE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Probability Threshold", name="THRESHOLD_PROB", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Probability Reference", name="RELATIVE_PROB", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["absolute", "relative"]
		param.value = "relative"
		params += [param]
		param = arcpy.Parameter(displayName="Binary Encoding", name="WTA_0", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Parallelepiped", name="WTA_1", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Distance", name="WTA_2", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mahalanobis Distance", name="WTA_3", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Likelihood", name="WTA_4", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Angle Mapping", name="WTA_5", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_classification', '0')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALISE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('QUALITY', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('TRAINING', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('TRAINING_CLASS', parameters[5].valueAsText)
		Tool.Set_Option('FILE_LOAD', parameters[6].valueAsText)
		Tool.Set_Option('FILE_SAVE', parameters[7].valueAsText)
		Tool.Set_Option('METHOD', parameters[8].valueAsText)
		Tool.Set_Option('THRESHOLD_DIST', parameters[9].valueAsText)
		Tool.Set_Option('THRESHOLD_ANGLE', parameters[10].valueAsText)
		Tool.Set_Option('THRESHOLD_PROB', parameters[11].valueAsText)
		Tool.Set_Option('RELATIVE_PROB', parameters[12].valueAsText)
		Tool.Set_Option('WTA_0', parameters[13].valueAsText)
		Tool.Set_Option('WTA_1', parameters[14].valueAsText)
		Tool.Set_Option('WTA_2', parameters[15].valueAsText)
		Tool.Set_Option('WTA_3', parameters[16].valueAsText)
		Tool.Set_Option('WTA_4', parameters[17].valueAsText)
		Tool.Set_Option('WTA_5', parameters[18].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Cluster Analysis for Grids"
		self.description = "<p>Cluster Analysis for grids.</p><p></p><p>References:</p><p></p><p>Iterative Minimum Distance:</p><p>- Forgy, E. (1965):</p><p>  'Cluster Analysis of multivariate data: efficiency vs. interpretability of classifications',</p><p>  Biometrics 21:768</p><p></p><p>Hill-Climbing:- Rubin, J. (1967):</p><p>  'Optimal Classification into Groups: An Approach for Solving the Taxonomy Problem',</p><p>  J. Theoretical Biology, 15:103-144</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Clusters", name="CLUSTER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Statistics", name="STATISTICS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Iterative Minimum Distance (Forgy 1965)", "Hill-Climbing (Rubin 1967)", "Combined Minimum Distance / Hillclimbing"]
		param.value = "Hill-Climbing (Rubin 1967)"
		params += [param]
		param = arcpy.Parameter(displayName="Clusters", name="NCLUSTER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Iterations", name="MAXITER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Normalise", name="NORMALISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Old Version", name="OLDVERSION", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Update View", name="UPDATEVIEW", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_classification', '1')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('CLUSTER', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('STATISTICS', parameters[2].valueAsText, 'table')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('NCLUSTER', parameters[4].valueAsText)
		Tool.Set_Option('MAXITER', parameters[5].valueAsText)
		Tool.Set_Option('NORMALISE', parameters[6].valueAsText)
		Tool.Set_Option('OLDVERSION', parameters[7].valueAsText)
		Tool.Set_Option('UPDATEVIEW', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Confusion Matrix (Two Grids)"
		self.description = "<p>Compares two classified grids and creates a confusion matrix and derived coefficients as well as the combinations of both classifications as new grid. Grid classes have to be defined with a look-up table and values of both grids must match each other for the subsequent comparison. A typical application is a change detection analysis based on land cover classification of satellite imagery. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classification 1", name="ONE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="ONE_LUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Value", name="ONE_LUT_MIN", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ONE_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Value (Maximum)", name="ONE_LUT_MAX", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ONE_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="ONE_LUT_NAM", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ONE_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Classification 2", name="TWO", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="TWO_LUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Value", name="TWO_LUT_MIN", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TWO_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Value (Maximum)", name="TWO_LUT_MAX", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TWO_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="TWO_LUT_NAM", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TWO_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Combined Classes", name="COMBINED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Report Unchanged Classes", name="NOCHANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Confusion Matrix", name="CONFUSION", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Output as...", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cells", "percent", "area"]
		param.value = "cells"
		params += [param]
		param = arcpy.Parameter(displayName="Class Values", name="CLASSES", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Summary", name="SUMMARY", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_classification', '2')
		Tool.Set_Input ('ONE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('ONE_LUT', parameters[1].valueAsText, 'table')
		Tool.Set_Option('ONE_LUT_MIN', parameters[2].valueAsText)
		Tool.Set_Option('ONE_LUT_MAX', parameters[3].valueAsText)
		Tool.Set_Option('ONE_LUT_NAM', parameters[4].valueAsText)
		Tool.Set_Input ('TWO', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('TWO_LUT', parameters[6].valueAsText, 'table')
		Tool.Set_Option('TWO_LUT_MIN', parameters[7].valueAsText)
		Tool.Set_Option('TWO_LUT_MAX', parameters[8].valueAsText)
		Tool.Set_Option('TWO_LUT_NAM', parameters[9].valueAsText)
		Tool.Set_Output('COMBINED', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('NOCHANGE', parameters[11].valueAsText)
		Tool.Set_Output('CONFUSION', parameters[12].valueAsText, 'table')
		Tool.Set_Option('OUTPUT', parameters[13].valueAsText)
		Tool.Set_Output('CLASSES', parameters[14].valueAsText, 'table')
		Tool.Set_Output('SUMMARY', parameters[15].valueAsText, 'table')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Supervised Classification for Shapes"
		self.description = "<p>Supervised classification for attribute data. To train the classifier choose an attribute that provides class identifiers for those records, for which the target class is known, and no data for all other records.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Normalise", name="NORMALISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Training Classes", name="TRAINING", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Load Statistics from File...", name="FILE_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Save Statistics to File...", name="FILE_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Binary Encoding", "Parallelepiped", "Minimum Distance", "Mahalanobis Distance", "Maximum Likelihood", "Spectral Angle Mapping", "Winner Takes All"]
		param.value = "Minimum Distance"
		params += [param]
		param = arcpy.Parameter(displayName="Distance Threshold", name="THRESHOLD_DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Angle Threshold (Degree)", name="THRESHOLD_ANGLE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Probability Threshold", name="THRESHOLD_PROB", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Probability Reference", name="RELATIVE_PROB", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["absolute", "relative"]
		param.value = "relative"
		params += [param]
		param = arcpy.Parameter(displayName="Binary Encoding", name="WTA_0", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Parallelepiped", name="WTA_1", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Distance", name="WTA_2", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mahalanobis Distance", name="WTA_3", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Likelihood", name="WTA_4", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Angle Mapping", name="WTA_5", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_classification', '4')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('CLASSES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('FEATURES', parameters[2].valueAsText)
		Tool.Set_Option('NORMALISE', parameters[3].valueAsText)
		Tool.Set_Option('TRAINING', parameters[4].valueAsText)
		Tool.Set_Option('FILE_LOAD', parameters[5].valueAsText)
		Tool.Set_Option('FILE_SAVE', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Set_Option('THRESHOLD_DIST', parameters[8].valueAsText)
		Tool.Set_Option('THRESHOLD_ANGLE', parameters[9].valueAsText)
		Tool.Set_Option('THRESHOLD_PROB', parameters[10].valueAsText)
		Tool.Set_Option('RELATIVE_PROB', parameters[11].valueAsText)
		Tool.Set_Option('WTA_0', parameters[12].valueAsText)
		Tool.Set_Option('WTA_1', parameters[13].valueAsText)
		Tool.Set_Option('WTA_2', parameters[14].valueAsText)
		Tool.Set_Option('WTA_3', parameters[15].valueAsText)
		Tool.Set_Option('WTA_4', parameters[16].valueAsText)
		Tool.Set_Option('WTA_5', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Supervised Classification for Tables"
		self.description = "<p>Supervised classification for attribute data. To train the classifier choose an attribute that provides class identifiers for those records, for which the target class is known, and no data for all other records.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Normalise", name="NORMALISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Training Classes", name="TRAINING", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Load Statistics from File...", name="FILE_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Save Statistics to File...", name="FILE_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Binary Encoding", "Parallelepiped", "Minimum Distance", "Mahalanobis Distance", "Maximum Likelihood", "Spectral Angle Mapping", "Winner Takes All"]
		param.value = "Minimum Distance"
		params += [param]
		param = arcpy.Parameter(displayName="Distance Threshold", name="THRESHOLD_DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Angle Threshold (Degree)", name="THRESHOLD_ANGLE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Probability Threshold", name="THRESHOLD_PROB", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Probability Reference", name="RELATIVE_PROB", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["absolute", "relative"]
		param.value = "relative"
		params += [param]
		param = arcpy.Parameter(displayName="Binary Encoding", name="WTA_0", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Parallelepiped", name="WTA_1", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Distance", name="WTA_2", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mahalanobis Distance", name="WTA_3", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Likelihood", name="WTA_4", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Angle Mapping", name="WTA_5", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_classification', '5')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Output('CLASSES', parameters[1].valueAsText, 'table')
		Tool.Set_Option('FEATURES', parameters[2].valueAsText)
		Tool.Set_Option('NORMALISE', parameters[3].valueAsText)
		Tool.Set_Option('TRAINING', parameters[4].valueAsText)
		Tool.Set_Option('FILE_LOAD', parameters[5].valueAsText)
		Tool.Set_Option('FILE_SAVE', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Set_Option('THRESHOLD_DIST', parameters[8].valueAsText)
		Tool.Set_Option('THRESHOLD_ANGLE', parameters[9].valueAsText)
		Tool.Set_Option('THRESHOLD_PROB', parameters[10].valueAsText)
		Tool.Set_Option('RELATIVE_PROB', parameters[11].valueAsText)
		Tool.Set_Option('WTA_0', parameters[12].valueAsText)
		Tool.Set_Option('WTA_1', parameters[13].valueAsText)
		Tool.Set_Option('WTA_2', parameters[14].valueAsText)
		Tool.Set_Option('WTA_3', parameters[15].valueAsText)
		Tool.Set_Option('WTA_4', parameters[16].valueAsText)
		Tool.Set_Option('WTA_5', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Confusion Matrix (Polygons / Grid)"
		self.description = "<p>Compares a classified polygons layer with grid classes and creates a confusion matrix and derived coefficients. Grid classes have to be defined with a look-up table and values must match those of the polygon classes for the subsequent comparison. This tool is typically used for a quality assessment of a supervised classification. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classification", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="GRID_LUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Value", name="GRID_LUT_MIN", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["GRID_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Value (Maximum)", name="GRID_LUT_MAX", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["GRID_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="GRID_LUT_NAM", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["GRID_LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Classes", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Confusion Matrix", name="CONFUSION", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Class Values", name="CLASSES", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Summary", name="SUMMARY", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_classification', '6')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRID_LUT', parameters[1].valueAsText, 'table')
		Tool.Set_Option('GRID_LUT_MIN', parameters[2].valueAsText)
		Tool.Set_Option('GRID_LUT_MAX', parameters[3].valueAsText)
		Tool.Set_Option('GRID_LUT_NAM', parameters[4].valueAsText)
		Tool.Set_Input ('POLYGONS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[6].valueAsText)
		Tool.Set_Output('CONFUSION', parameters[7].valueAsText, 'table')
		Tool.Set_Output('CLASSES', parameters[8].valueAsText, 'table')
		Tool.Set_Output('SUMMARY', parameters[9].valueAsText, 'table')
		Tool.Run()
		return
