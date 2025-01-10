import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Proj.4"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_5, tool_9, tool_13, tool_14, tool_15, tool_16, tool_17, tool_20, tool_21]

class tool_0(object):
	def __init__(self):
		self.label = "Set Coordinate Reference System"
		self.description = "<p>The module allows one to define the Coordinate Reference System (CRS) of the supplied data sets. The module applies no transformation to the data sets, it just updates their CRS metadata.</p><p>A complete and correct description of the CRS of a dataset is necessary in order to be able to actually apply a projection with one of the 'Coordinate Transformation' modules later.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Precise Datum Conversion", name="PRECISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '0')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('PRECISE', parameters[4].valueAsText)
		Tool.Set_Input ('GRIDS', parameters[5].valueAsText, 'grid_list')
		Tool.Set_Input ('SHAPES', parameters[6].valueAsText, 'shapes_list')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Coordinate Transformation (Shapes List)"
		self.description = "<p>Coordinate transformation for shapes.</p><p></p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is Rel. 4.8.0, 6 March 2012</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Precise Datum Conversion", name="PRECISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="TARGET", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '1')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('PRECISE', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'shapes_list')
		Tool.Set_Output('TARGET', parameters[6].valueAsText, 'shapes_list')
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Coordinate Transformation (Shapes)"
		self.description = "<p>Coordinate transformation for shapes.</p><p></p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is Rel. 4.8.0, 6 March 2012</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Precise Datum Conversion", name="PRECISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="TARGET", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '2')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('PRECISE', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'shapes')
		Tool.Set_Output('TARGET', parameters[6].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "[deprecated] Proj.4 (Command Line Arguments, Shapes)"
		self.description = "<p>Coordinate Transformation for Shapes.</p><p>Based on the PROJ.4 Cartographic Projections library originally written by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Source Projection Parameters", name="SOURCE_PROJ", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "+proj=tmerc +datum=potsdam +lon_0=9 +x_0=3500000"
		params  = [param]
		param = arcpy.Parameter(displayName="Target Projection Parameters", name="TARGET_PROJ", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "+proj=tmerc +datum=potsdam +lon_0=12 +x_0=4500000"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="TARGET", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '5')
		Tool.Set_Option('SOURCE_PROJ', parameters[0].valueAsText)
		Tool.Set_Option('TARGET_PROJ', parameters[1].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('TARGET', parameters[3].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "[deprecated] Proj.4 (Command Line Arguments, List of Shapes Layers)"
		self.description = "<p>Coordinate Transformation for Shapes.</p><p>Based on the PROJ.4 Cartographic Projections library originally written by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Source Projection Parameters", name="SOURCE_PROJ", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "+proj=tmerc +datum=potsdam +lon_0=9 +x_0=3500000"
		params  = [param]
		param = arcpy.Parameter(displayName="Target Projection Parameters", name="TARGET_PROJ", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "+proj=tmerc +datum=potsdam +lon_0=12 +x_0=4500000"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="TARGET", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '9')
		Tool.Set_Option('SOURCE_PROJ', parameters[0].valueAsText)
		Tool.Set_Option('TARGET_PROJ', parameters[1].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[2].valueAsText, 'shapes_list')
		Tool.Set_Output('TARGET', parameters[3].valueAsText, 'shapes_list')
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Change Longitudinal Range for Grids"
		self.description = "<p>Change the longitudinal range of grids using geographic coordinates, i.e. from 0 - 360 to -180 - 180 and vice versa.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["0 - 360 >> -180 - 180", "-180 - 180 >> 0 - 360"]
		param.value = "0 - 360 >> -180 - 180"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '13')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('DIRECTION', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Latitude/Longitude Graticule"
		self.description = "<p>Creates a longitude/latitude graticule for the extent and projection of the input shapes layer. </p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is Rel. 4.8.0, 6 March 2012</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Precise Datum Conversion", name="PRECISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Graticule", name="GRATICULE", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Frame Coordinates", name="COORDS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="XMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="XMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="YMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="YMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Interval", name="INTERVAL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["fixed interval", "fitted interval"]
		param.value = "fixed interval"
		params += [param]
		param = arcpy.Parameter(displayName="Fixed Interval (Degree)", name="FIXED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Intervals", name="FITTED", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Resolution (Degree)", name="RESOLUTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '14')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('PRECISE', parameters[4].valueAsText)
		Tool.Set_Output('GRATICULE', parameters[5].valueAsText, 'shapes')
		Tool.Set_Output('COORDS', parameters[6].valueAsText, 'shapes')
		Tool.Set_Option('XMIN', parameters[7].valueAsText)
		Tool.Set_Option('XMAX', parameters[8].valueAsText)
		Tool.Set_Option('YMIN', parameters[9].valueAsText)
		Tool.Set_Option('YMAX', parameters[10].valueAsText)
		Tool.Set_Option('INTERVAL', parameters[11].valueAsText)
		Tool.Set_Option('FIXED', parameters[12].valueAsText)
		Tool.Set_Option('FITTED', parameters[13].valueAsText)
		Tool.Set_Option('RESOLUTION', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Coordinate Reference System Picker"
		self.description = "<p>Define or pick a Coordinate Reference System (CRS). It is intended to call this tool only from other tools.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Precise Datum Conversion", name="PRECISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '15')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('PRECISE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Tissot's Indicatrix"
		self.description = "<p>Creates a shapes layer with Tissot's indicatrices for chosen projection.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is Rel. 4.8.0, 6 March 2012</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Precise Datum Conversion", name="PRECISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Indicatrix", name="TARGET", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number in Latitudinal Direction", name="NY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Number in Meridional Direction", name="NX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 11
		params += [param]
		param = arcpy.Parameter(displayName="Size", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '16')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('PRECISE', parameters[4].valueAsText)
		Tool.Set_Output('TARGET', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('NY', parameters[6].valueAsText)
		Tool.Set_Option('NX', parameters[7].valueAsText)
		Tool.Set_Option('SCALE', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Geographic Coordinate Grids"
		self.description = "<p>Creates for a given grid geographic coordinate information, i.e. two grids specifying the longitude and latitude for each cell. The coodinate system of the input grid has to be defined. </p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is Rel. 4.8.0, 6 March 2012</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Longitude", name="LON", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '17')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LON', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('LAT', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Geographic Distances"
		self.description = "<p>Calculates for all segments of the input lines the planar, great elliptic, and loxodrome distance and re-projects the latter two to the projection of the input lines. </p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is Rel. 4.8.0, 6 March 2012</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Segments", name="PLANAR", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Great Elliptic", name="ORTHODROME", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Loxodrome", name="LOXODROME", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Epsilon", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '20')
		Tool.Set_Input ('PLANAR', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('ORTHODROME', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('LOXODROME', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('EPSILON', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Geographic Distances (Pair of Coordinates)"
		self.description = "<p>Calculates for all segments of the input lines the planar, great elliptic, and loxodrome distance and re-projects the latter two to the projection of the input lines. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Precise Datum Conversion", name="PRECISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Geographic Distances", name="DISTANCES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X", name="COORD_X1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="COORD_Y1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.500000
		params += [param]
		param = arcpy.Parameter(displayName="X", name="COORD_X2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 116.500000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="COORD_Y2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.400000
		params += [param]
		param = arcpy.Parameter(displayName="Epsilon", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '21')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('PRECISE', parameters[4].valueAsText)
		Tool.Set_Output('DISTANCES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('COORD_X1', parameters[6].valueAsText)
		Tool.Set_Option('COORD_Y1', parameters[7].valueAsText)
		Tool.Set_Option('COORD_X2', parameters[8].valueAsText)
		Tool.Set_Option('COORD_Y2', parameters[9].valueAsText)
		Tool.Set_Option('EPSILON', parameters[10].valueAsText)
		Tool.Run()
		return
