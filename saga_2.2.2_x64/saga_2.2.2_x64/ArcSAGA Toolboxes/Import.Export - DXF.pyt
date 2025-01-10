import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "DXF"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Import DXF Files"
		self.description = "<p>This module imports DXF files using the free \"dxflib\" library. Get more information about this library from the RibbonSoft homepage at:</p><p><a href=\"http://www.ribbonsoft.com/dxflib.html\">http://www.ribbonsoft.com/dxflib.html</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Import Filter", name="FILTER", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all entities", "only entities with layer definition", "only entities without layer definition"]
		param.value = "only entities with layer definition"
		params += [param]
		param = arcpy.Parameter(displayName="Circle Point Distance [Degree]", name="DCIRCLE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_shapes_dxf', '0')
		Tool.Set_Output('SHAPES', parameters[0].valueAsText, 'shapes_list')
		Tool.Set_Output('TABLES', parameters[1].valueAsText, 'shapes_list')
		Tool.Set_Option('FILE', parameters[2].valueAsText)
		Tool.Set_Option('FILTER', parameters[3].valueAsText)
		Tool.Set_Option('DCIRCLE', parameters[4].valueAsText)
		Tool.Run()
		return
