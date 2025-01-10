import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Transects"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Transect through polygon shapefile"
		self.description = "<p>Transect for lines and polygon shapefiles</p><p></p><p>The goal of this module is to create a transect along a line through a polygon map.</p><p>Eg</p><p></p><p>|____ST1_____!_ST2_!__ST1__!_______ST#_____|</p><p></p><p>(Soil type 1 etc...)</p><p></p><p>This is done by creating a table with the ID of each line, the distance </p><p>to the starting point and the different transects:</p><p></p><p><pre>|  line_id  |  start  |  end  |  code/field  |</p><p>|    0      |    0    |  124  |     ST1      |</p><p>|    0      |   124   |  300  |     ST2      |</p><p>|    0      |   300   | 1223  |     ST1      |</p><p>|    0      |  1223   | 2504  |     ST3      |</p><p>|    1      |    0    |  200  |     ST4      |</p><p>|   ...     |   ...   |  ...  |     ...      |</pre></p><p></p><p></p><p>The module requires an input shape with all the line transects [Transect_Line] </p><p>and a polygon theme [Theme]. You also have to select which field you want to have in </p><p>the resulting table [Transect_Result]. This can be an ID of the polygon theme if you </p><p>want to link the tables later on, or any other field [Theme_Field].</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Line Transect(s)", name="TRANSECT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Theme", name="THEME", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Theme Field", name="THEME_FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["THEME"]
		params += [param]
		param = arcpy.Parameter(displayName="Result table", name="TRANSECT_RESULT", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_transect', '0')
		Tool.Set_Input ('TRANSECT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('THEME', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('THEME_FIELD', parameters[2].valueAsText)
		Tool.Set_Output('TRANSECT_RESULT', parameters[3].valueAsText, 'table')
		Tool.Run()
		return
