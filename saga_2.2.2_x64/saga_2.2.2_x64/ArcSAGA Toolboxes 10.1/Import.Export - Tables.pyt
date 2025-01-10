import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tables"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2]

class tool_0(object):
	def __init__(self):
		self.label = "Export Text Table"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Save Headline", name="HEADLINE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Strings in Quota", name="STRQUOTA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Separator", name="SEPARATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["tabulator", ";", ",", "space", "other"]
		param.value = "tabulator"
		params += [param]
		param = arcpy.Parameter(displayName="other", name="SEP_OTHER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "*"
		params += [param]
		param = arcpy.Parameter(displayName="File", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_table', '0')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('HEADLINE', parameters[1].valueAsText)
		Tool.Set_Option('STRQUOTA', parameters[2].valueAsText)
		Tool.Set_Option('SEPARATOR', parameters[3].valueAsText)
		Tool.Set_Option('SEP_OTHER', parameters[4].valueAsText)
		Tool.Set_Option('FILENAME', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Import Text Table"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="File contains headline", name="HEADLINE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Separator", name="SEPARATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["tabulator", ";", ",", "space", "other"]
		param.value = "tabulator"
		params += [param]
		param = arcpy.Parameter(displayName="Separator (other)", name="SEP_OTHER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "*"
		params += [param]
		param = arcpy.Parameter(displayName="File", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_table', '1')
		Tool.Set_Output('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('HEADLINE', parameters[1].valueAsText)
		Tool.Set_Option('SEPARATOR', parameters[2].valueAsText)
		Tool.Set_Option('SEP_OTHER', parameters[3].valueAsText)
		Tool.Set_Option('FILENAME', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Import Text Table with Numbers only"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Skip Lines", name="SKIP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Headline", name="HEADLINE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Separator", name="SEPARATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["tabulator", ";", ",", "space", "other"]
		param.value = "tabulator"
		params += [param]
		param = arcpy.Parameter(displayName="other", name="SEP_OTHER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "*"
		params += [param]
		param = arcpy.Parameter(displayName="File", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_table', '2')
		Tool.Set_Output('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('SKIP', parameters[1].valueAsText)
		Tool.Set_Option('HEADLINE', parameters[2].valueAsText)
		Tool.Set_Option('SEPARATOR', parameters[3].valueAsText)
		Tool.Set_Option('SEP_OTHER', parameters[4].valueAsText)
		Tool.Set_Option('FILENAME', parameters[5].valueAsText)
		Tool.Run()
		return
