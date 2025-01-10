import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Images"
		self.alias = ""
		self.tools = [tool_0, tool_2, tool_3]

class tool_0(object):
	def __init__(self):
		self.label = "Export Image (bmp, jpg, pcx, png, tif)"
		self.description = "<p>The module allows one to save a grid as image.</p><p>Optionally, a shade grid can be overlayed and it's transparency and brightness can be adjusted.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Shade", name="SHADE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Image File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Create KML File", name="FILE_KML", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Colouring", name="COLOURING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["stretch to grid's standard deviation", "stretch to grid's value range", "stretch to specified value range", "lookup table", "rgb coded values"]
		param.value = "stretch to grid's standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Color Palette", name="COL_PALETTE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["DEFAULT", "DEFAULT_BRIGHT", "BLACK_WHITE", "BLACK_RED", "BLACK_GREEN", "BLACK_BLUE", "WHITE_RED", "WHITE_GREEN", "WHITE_BLUE", "YELLOW_RED", "YELLOW_GREEN", "YELLOW_BLUE", "RED_GREEN", "RED_BLUE", "GREEN_BLUE", "RED_GREY_BLUE", "RED_GREY_GREEN", "GREEN_GREY_BLUE", "RED_GREEN_BLUE", "RED_BLUE_GREEN", "GREEN_RED_BLUE", "RAINBOW", "NEON", "TOPOGRAPHY", "ASPECT_1", "ASPECT_2", "ASPECT_3"]
		param.value = "DEFAULT"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Colors", name="COL_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Revert Palette", name="COL_REVERT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stretch to Value Range (Minimum)", name="STRETCH_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stretch to Value Range (Maximum)", name="STRETCH_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lookup Table", name="LUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Shade Transparency [%]", name="SHADE_TRANS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 40.000000
		params += [param]
		param = arcpy.Parameter(displayName="Shade Brightness [%] (Minimum)", name="SHADE_BRIGHT_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Shade Brightness [%] (Maximum)", name="SHADE_BRIGHT_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid_image', '0')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SHADE', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('FILE', parameters[2].valueAsText)
		Tool.Set_Option('FILE_KML', parameters[3].valueAsText)
		Tool.Set_Option('COLOURING', parameters[4].valueAsText)
		Tool.Set_Option('COL_PALETTE', parameters[5].valueAsText)
		Tool.Set_Option('COL_COUNT', parameters[6].valueAsText)
		Tool.Set_Option('COL_REVERT', parameters[7].valueAsText)
		Tool.Set_Option('STDDEV', parameters[8].valueAsText)
		Tool.Set_Option('STRETCH_MIN', parameters[9].valueAsText)
		Tool.Set_Option('STRETCH_MAX', parameters[10].valueAsText)
		Tool.Set_Input ('LUT', parameters[11].valueAsText, 'table')
		Tool.Set_Option('SHADE_TRANS', parameters[12].valueAsText)
		Tool.Set_Option('SHADE_BRIGHT_MIN', parameters[13].valueAsText)
		Tool.Set_Option('SHADE_BRIGHT_MAX', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Export Grid to KML"
		self.description = "<p>Uses 'Export Image' tool to create the image file. Automatically projects raster to geographic coordinate system, if its projection is known and not geographic. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Shade", name="SHADE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Image File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["kml and image files", "kmz, kml and image files", "kmz file"]
		param.value = "kmz file"
		params += [param]
		param = arcpy.Parameter(displayName="Colouring", name="COLOURING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["stretch to grid's standard deviation", "stretch to grid's value range", "stretch to specified value range", "lookup table", "rgb coded values"]
		param.value = "stretch to grid's standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Color Palette", name="COL_PALETTE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["DEFAULT", "DEFAULT_BRIGHT", "BLACK_WHITE", "BLACK_RED", "BLACK_GREEN", "BLACK_BLUE", "WHITE_RED", "WHITE_GREEN", "WHITE_BLUE", "YELLOW_RED", "YELLOW_GREEN", "YELLOW_BLUE", "RED_GREEN", "RED_BLUE", "GREEN_BLUE", "RED_GREY_BLUE", "RED_GREY_GREEN", "GREEN_GREY_BLUE", "RED_GREEN_BLUE", "RED_BLUE_GREEN", "GREEN_RED_BLUE", "RAINBOW", "NEON", "TOPOGRAPHY", "ASPECT_1", "ASPECT_2", "ASPECT_3"]
		param.value = "DEFAULT"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Colors", name="COL_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Revert Palette", name="COL_REVERT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stretch to Value Range (Minimum)", name="STRETCH_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stretch to Value Range (Maximum)", name="STRETCH_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lookup Table", name="LUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Shade Brightness (Minimum)", name="SHADE_BRIGHT_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Shade Brightness (Maximum)", name="SHADE_BRIGHT_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid_image', '2')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SHADE', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('FILE', parameters[2].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[3].valueAsText)
		Tool.Set_Option('COLOURING', parameters[4].valueAsText)
		Tool.Set_Option('COL_PALETTE', parameters[5].valueAsText)
		Tool.Set_Option('COL_COUNT', parameters[6].valueAsText)
		Tool.Set_Option('COL_REVERT', parameters[7].valueAsText)
		Tool.Set_Option('STDDEV', parameters[8].valueAsText)
		Tool.Set_Option('STRETCH_MIN', parameters[9].valueAsText)
		Tool.Set_Option('STRETCH_MAX', parameters[10].valueAsText)
		Tool.Set_Input ('LUT', parameters[11].valueAsText, 'table')
		Tool.Set_Option('INTERPOL', parameters[12].valueAsText)
		Tool.Set_Option('SHADE_BRIGHT_MIN', parameters[13].valueAsText)
		Tool.Set_Option('SHADE_BRIGHT_MAX', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Import Grids from KML"
		self.description = "<p>Uses 'Import Image' tool to load the ground overlay image files associated with the kml. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="KML/KMZ File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid_image', '3')
		Tool.Set_Output('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Run()
		return
