import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grids"
		self.alias = ""
		self.tools = [tool_3, tool_4, tool_5, tool_7, tool_8, tool_9, tool_10]

class tool_3(object):
	def __init__(self):
		self.label = "RGB Composite"
		self.description = "<p>Create red-green-blue overlays of grids. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red", name="R_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Value Preparation", name="R_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["take original value (0 - 255)", "rescale to 0 - 255", "user defined", "percentiles", "standard deviation"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Minimum)", name="R_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Maximum)", name="R_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 255.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Minimum)", name="R_PERCTL_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Maximum)", name="R_PERCTL_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="R_STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="G_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value Preparation", name="G_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["take original value (0 - 255)", "rescale to 0 - 255", "user defined", "percentiles", "standard deviation"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Minimum)", name="G_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Maximum)", name="G_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 255.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Minimum)", name="G_PERCTL_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Maximum)", name="G_PERCTL_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="G_STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value Preparation", name="B_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["take original value (0 - 255)", "rescale to 0 - 255", "user defined", "percentiles", "standard deviation"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Minimum)", name="B_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Maximum)", name="B_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 255.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Minimum)", name="B_PERCTL_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Maximum)", name="B_PERCTL_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="B_STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Alpha", name="A_GRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value Preparation", name="A_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["take original value (0 - 255)", "rescale to 0 - 255", "user defined", "percentiles", "standard deviation"]
		param.value = "standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Minimum)", name="A_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Maximum)", name="A_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 255.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Minimum)", name="A_PERCTL_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Maximum)", name="A_PERCTL_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="A_STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Composite", name="RGB", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_visualisation', '3')
		Tool.Set_Input ('R_GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('R_METHOD', parameters[1].valueAsText)
		Tool.Set_Option('R_RANGE_MIN', parameters[2].valueAsText)
		Tool.Set_Option('R_RANGE_MAX', parameters[3].valueAsText)
		Tool.Set_Option('R_PERCTL_MIN', parameters[4].valueAsText)
		Tool.Set_Option('R_PERCTL_MAX', parameters[5].valueAsText)
		Tool.Set_Option('R_STDDEV', parameters[6].valueAsText)
		Tool.Set_Input ('G_GRID', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('G_METHOD', parameters[8].valueAsText)
		Tool.Set_Option('G_RANGE_MIN', parameters[9].valueAsText)
		Tool.Set_Option('G_RANGE_MAX', parameters[10].valueAsText)
		Tool.Set_Option('G_PERCTL_MIN', parameters[11].valueAsText)
		Tool.Set_Option('G_PERCTL_MAX', parameters[12].valueAsText)
		Tool.Set_Option('G_STDDEV', parameters[13].valueAsText)
		Tool.Set_Input ('B_GRID', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('B_METHOD', parameters[15].valueAsText)
		Tool.Set_Option('B_RANGE_MIN', parameters[16].valueAsText)
		Tool.Set_Option('B_RANGE_MAX', parameters[17].valueAsText)
		Tool.Set_Option('B_PERCTL_MIN', parameters[18].valueAsText)
		Tool.Set_Option('B_PERCTL_MAX', parameters[19].valueAsText)
		Tool.Set_Option('B_STDDEV', parameters[20].valueAsText)
		Tool.Set_Input ('A_GRID', parameters[21].valueAsText, 'grid')
		Tool.Set_Option('A_METHOD', parameters[22].valueAsText)
		Tool.Set_Option('A_RANGE_MIN', parameters[23].valueAsText)
		Tool.Set_Option('A_RANGE_MAX', parameters[24].valueAsText)
		Tool.Set_Option('A_PERCTL_MIN', parameters[25].valueAsText)
		Tool.Set_Option('A_PERCTL_MAX', parameters[26].valueAsText)
		Tool.Set_Option('A_STDDEV', parameters[27].valueAsText)
		Tool.Set_Output('RGB', parameters[28].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Create 3D Image"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Overlay Image", name="IMAGE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shapes to project", name="SHAPES", direction="Input", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Exaggeration", name="ZEXAGG", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Exaggeration [%]", name="ZEXAGG_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Image Rotation [Degree]", name="Z_ROTATE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Local Rotation [Degree]", name="X_ROTATE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Local Rotation Base Level", name="X_ROTATE_LEVEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Zero", "Mean Elevation"]
		param.value = "Mean Elevation"
		params += [param]
		param = arcpy.Parameter(displayName="Panorama Break [%]", name="PANBREAK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 70.000000
		params += [param]
		param = arcpy.Parameter(displayName="Projection", name="PROJECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Panorama", "Circular"]
		param.value = "Panorama"
		params += [param]
		param = arcpy.Parameter(displayName="3D Image Width", name="NX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="3D Image Height", name="NY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="3D Image", name="RGB", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Projected Height", name="RGB_Z", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_visualisation', '4')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('IMAGE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('SHAPES', parameters[2].valueAsText, 'shapes_list')
		Tool.Set_Option('ZEXAGG', parameters[3].valueAsText)
		Tool.Set_Option('ZEXAGG_MIN', parameters[4].valueAsText)
		Tool.Set_Option('Z_ROTATE', parameters[5].valueAsText)
		Tool.Set_Option('X_ROTATE', parameters[6].valueAsText)
		Tool.Set_Option('X_ROTATE_LEVEL', parameters[7].valueAsText)
		Tool.Set_Option('PANBREAK', parameters[8].valueAsText)
		Tool.Set_Option('PROJECTION', parameters[9].valueAsText)
		Tool.Set_Option('NX', parameters[10].valueAsText)
		Tool.Set_Option('NY', parameters[11].valueAsText)
		Tool.Set_Output('RGB', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('RGB_Z', parameters[13].valueAsText, 'grid')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Color Triangle Composite"
		self.description = "<p>Similar to 'RGB Composite', but the three colors representing intensity of each data set can be chosen by user. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="A", name="A_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Value Preparation", name="A_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["0 - 1", "Rescale to 0 - 1", "User defined rescale", "Percentiles", "Percentage of standard deviation"]
		param.value = "Percentage of standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Minimum)", name="A_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Maximum)", name="A_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Minimum)", name="A_PERCTL_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Maximum)", name="A_PERCTL_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentage of standard deviation", name="A_PERCENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 150.000000
		params += [param]
		param = arcpy.Parameter(displayName="B", name="B_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value Preparation", name="B_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["0 - 1", "Rescale to 0 - 1", "User defined rescale", "Percentiles", "Percentage of standard deviation"]
		param.value = "Percentage of standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Minimum)", name="B_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Maximum)", name="B_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Minimum)", name="B_PERCTL_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Maximum)", name="B_PERCTL_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentage of standard deviation", name="B_PERCENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 150.000000
		params += [param]
		param = arcpy.Parameter(displayName="C", name="C_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value Preparation", name="C_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["0 - 1.0", "Rescale to 0 - 1.0", "User defined rescale", "Percentiles", "Percentage of standard deviation"]
		param.value = "Percentage of standard deviation"
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Minimum)", name="C_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Rescale Range (Maximum)", name="C_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Minimum)", name="C_PERCTL_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles (Maximum)", name="C_PERCTL_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentage of standard deviation", name="C_PERCENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 150.000000
		params += [param]
		param = arcpy.Parameter(displayName="Composite", name="GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_visualisation', '5')
		Tool.Set_Input ('A_GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('A_METHOD', parameters[1].valueAsText)
		Tool.Set_Option('A_RANGE_MIN', parameters[2].valueAsText)
		Tool.Set_Option('A_RANGE_MAX', parameters[3].valueAsText)
		Tool.Set_Option('A_PERCTL_MIN', parameters[4].valueAsText)
		Tool.Set_Option('A_PERCTL_MAX', parameters[5].valueAsText)
		Tool.Set_Option('A_PERCENT', parameters[6].valueAsText)
		Tool.Set_Input ('B_GRID', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('B_METHOD', parameters[8].valueAsText)
		Tool.Set_Option('B_RANGE_MIN', parameters[9].valueAsText)
		Tool.Set_Option('B_RANGE_MAX', parameters[10].valueAsText)
		Tool.Set_Option('B_PERCTL_MIN', parameters[11].valueAsText)
		Tool.Set_Option('B_PERCTL_MAX', parameters[12].valueAsText)
		Tool.Set_Option('B_PERCENT', parameters[13].valueAsText)
		Tool.Set_Input ('C_GRID', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('C_METHOD', parameters[15].valueAsText)
		Tool.Set_Option('C_RANGE_MIN', parameters[16].valueAsText)
		Tool.Set_Option('C_RANGE_MAX', parameters[17].valueAsText)
		Tool.Set_Option('C_PERCTL_MIN', parameters[18].valueAsText)
		Tool.Set_Option('C_PERCTL_MAX', parameters[19].valueAsText)
		Tool.Set_Option('C_PERCENT', parameters[20].valueAsText)
		Tool.Set_Output('GRID', parameters[21].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Aspect-Slope Grid"
		self.description = "<p>This module creates an aspect-slope map which shows both the aspect and the slope of the terrain. Aspect is symbolized by different hues, while slope is mapped with saturation.</p><p></p><p>References:</p><p>Brewer, C.A. & Marlow, K.A. (1993): Color Representation of Aspect and Slope simultaneously. Proceedings, Eleventh International Symposium on Computer-Assisted Cartography (Auto-Carto-11), Minneapolis, October/November 1993, pp. 328-337.</p><p><a href=\"http://www.personal.psu.edu/cab38/Terrain/AutoCarto.html\">http://www.personal.psu.edu/cab38/Terrain/AutoCarto.html</a></p><p></p><p></p><p><a href=\"http://blogs.esri.com/esri/arcgis/2008/05/23/aspect-slope-map/\">http://blogs.esri.com/esri/arcgis/2008/05/23/aspect-slope-map/</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Aspect-Slope", name="ASPECT_SLOPE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lookup Table", name="LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_visualisation', '7')
		Tool.Set_Input ('ASPECT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SLOPE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ASPECT_SLOPE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LUT', parameters[3].valueAsText, 'table')
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Terrain Map View"
		self.description = "<p>This module allows one to create different terrain visualisations from an elevation dataset:</p><p></p><p>* Topography: a simple map with an analytical hillshading of the terrain</p><p></p><p>* Morphology: a map which visualizes the terrain by combining positive and negative openess (Yokoyama et al. 2002) with terrain slope in a single map. In contrast to conventional shading methods this has the advantage of being independent from the direction of the light source.</p><p></p><p>References:</p><p>Yokoyama, R. / Shirasawa, M. / Pike, R.J. (2002): Visualizing topography by openness: A new application of image processing to digital elevation models. Photogrammetric Engineering and Remote Sensing, Vol.68, pp.251-266. <a target=\"_blank\" href=\"http://info.asprs.org/publications/pers/2002journal/march/2002_mar_257-265.pdf\">online at ASPRS</a>.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Shade", name="SHADE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Openness", name="OPENNESS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Contours", name="CONTOURS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Topography", "Morphology"]
		param.value = "Topography"
		params += [param]
		param = arcpy.Parameter(displayName="Radial Limit", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Contour Lines", name="CONTOUR_LINES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Equidistance", name="EQUIDISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_visualisation', '8')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SHADE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('OPENNESS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CONTOURS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Set_Option('RADIUS', parameters[6].valueAsText)
		Tool.Set_Option('CONTOUR_LINES', parameters[7].valueAsText)
		Tool.Set_Option('EQUIDISTANCE', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Split RGB Composite"
		self.description = "<p>Split red-green-blue channels of an rgb coded grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="RGB Composite", name="RGB", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Red", name="R", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="G", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Alpha", name="A", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Ignore No Data", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_visualisation', '9')
		Tool.Set_Input ('RGB', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('R', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('G', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('B', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('A', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('NODATA', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Select Look-up Table for Grid Visualization"
		self.description = "<p>Select a look-up table for visual classification of a grid. Useful in combination with tool chains. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="LUT", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_visualisation', '10')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LUT', parameters[1].valueAsText, 'table')
		Tool.Run()
		return
