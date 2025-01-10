import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Georeferencing"
		self.alias = ""
		self.tools = [tool_2, tool_5, tool_6]

class tool_2(object):
	def __init__(self):
		self.label = "Warping Shapes"
		self.description = "<p>Georeferencing of shapes layers. Either choose the attribute fields (x/y) with the projected coordinates for the reference points (origin) or supply a additional points layer with correspondend points in the target projection. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Reference Points (Origin)", name="REF_SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Reference Points (Projection)", name="REF_TARGET", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="x Position", name="XFIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["REF_SOURCE"]
		params += [param]
		param = arcpy.Parameter(displayName="y Position", name="YFIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["REF_SOURCE"]
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Automatic", "Triangulation", "Spline", "Affine", "1st Order Polynomial", "2nd Order Polynomial", "3rd Order Polynomial", "Polynomial, Order"]
		param.value = "Automatic"
		params += [param]
		param = arcpy.Parameter(displayName="Polynomial Order", name="ORDER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '2')
		Tool.Set_Input ('REF_SOURCE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('REF_TARGET', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('XFIELD', parameters[2].valueAsText)
		Tool.Set_Option('YFIELD', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('ORDER', parameters[5].valueAsText)
		Tool.Set_Input ('INPUT', parameters[6].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[7].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Define Georeference for Grids"
		self.description = "<p>This tool simply allows definition of grid's cellsize and position. It does not perform any kind of warping but might be helpful, if the grid has lost this information or is already aligned with the coordinate system. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Referenced Grids", name="REFERENCED", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Definition", name="DEFINITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cellsize and lower left center coordinates", "cellsize and lower left corner coordinates", "cellsize and upper left center coordinates", "cellsize and upper left corner coordinates", "lower left and upper right center coordinates", "lower left and upper right corner coordinates"]
		param.value = "cellsize and lower left center coordinates"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Left", name="XMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lower", name="YMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Right", name="XMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Upper", name="YMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '5')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('REFERENCED', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('DEFINITION', parameters[2].valueAsText)
		Tool.Set_Option('SIZE', parameters[3].valueAsText)
		Tool.Set_Option('XMIN', parameters[4].valueAsText)
		Tool.Set_Option('YMIN', parameters[5].valueAsText)
		Tool.Set_Option('XMAX', parameters[6].valueAsText)
		Tool.Set_Option('YMAX', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "World File from Flight and Camera Settings"
		self.description = "<p>Creates a world file (RST = rotation, scaling, translation) for georeferencing images by direct georeferencing. Direct georeferencing uses extrinsic (position, attitude) and intrinsic (focal length, physical pixel size) camera parameters.</p><p></p><p>References:</p><p>Baumker, M. / Heimes, F.J. (2001): New Calibration and Computing Method for Direct Georeferencing of Image and Scanner Data Using the Position and Angular Data of an Hybrid Inertial Navigation System. OEEPE Workshop, Integrated Sensor Orientation, Hannover 2001. <a target=\"_blank\" href=\"http://www.hochschule-bochum.de/fileadmin/media/fb_v/veroeffentlichungen/baeumker/baheimesoeepe.pdf\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Extent", name="EXTENT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="World File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Columns", name="NX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Number of Columns", name="NY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="X", name="X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Flying Height", name="Z", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Orientation", name="ORIENTATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["BLUH", "PATB"]
		param.value = "BLUH"
		params += [param]
		param = arcpy.Parameter(displayName="Omega [degree]", name="OMEGA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Phi [degree]", name="PHI", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Kappa [degree]", name="KAPPA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Kappa Offset [degree]", name="KAPPA_OFF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params += [param]
		param = arcpy.Parameter(displayName="Focal Length [mm]", name="CFL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 80.000000
		params += [param]
		param = arcpy.Parameter(displayName="CCD Physical Pixel Size [micron]", name="PXSIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.200000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '6')
		Tool.Set_Output('EXTENT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('NX', parameters[2].valueAsText)
		Tool.Set_Option('NY', parameters[3].valueAsText)
		Tool.Set_Option('X', parameters[4].valueAsText)
		Tool.Set_Option('Y', parameters[5].valueAsText)
		Tool.Set_Option('Z', parameters[6].valueAsText)
		Tool.Set_Option('ORIENTATION', parameters[7].valueAsText)
		Tool.Set_Option('OMEGA', parameters[8].valueAsText)
		Tool.Set_Option('PHI', parameters[9].valueAsText)
		Tool.Set_Option('KAPPA', parameters[10].valueAsText)
		Tool.Set_Option('KAPPA_OFF', parameters[11].valueAsText)
		Tool.Set_Option('CFL', parameters[12].valueAsText)
		Tool.Set_Option('PXSIZE', parameters[13].valueAsText)
		Tool.Run()
		return
