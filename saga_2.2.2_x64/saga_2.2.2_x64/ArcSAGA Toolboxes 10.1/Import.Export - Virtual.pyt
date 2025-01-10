import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Virtual"
		self.alias = ""
		self.tools = [tool_0, tool_2, tool_4, tool_6]

class tool_0(object):
	def __init__(self):
		self.label = "Create Virtual Point Cloud Dataset"
		self.description = "<p>The module allows one to create a virtual point cloud dataset from a set of SAGA point cloud files. For a large number of files, it is advised to use an input file list, i.e. a text file with the full path to an input point cloud on each line.</p><p>A virtual point cloud dataset is a simple XML format with the file extension .spcvf, which describes a mosaic of individual point cloud files. Such a virtual point cloud dataset can be used for seamless data access with the 'Get Subset from Virtual Point Cloud' module.</p><p>All point cloud input datasets must share the same attribute table structure, NoData value and projection.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Files", name="FILES", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Input File List", name="INPUT_FILE_LIST", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Filename", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="File Paths", name="METHOD_PATHS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["absolute", "relative"]
		param.value = "relative"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_virtual', '0')
		Tool.Set_Option('FILES', parameters[0].valueAsText)
		Tool.Set_Option('INPUT_FILE_LIST', parameters[1].valueAsText)
		Tool.Set_Option('FILENAME', parameters[2].valueAsText)
		Tool.Set_Option('METHOD_PATHS', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Create Tileshape from Virtual Point Cloud"
		self.description = "<p>The module allows to create a polygon shapefile with the bounding boxes of a virtual point cloud dataset. Additionally, the header information of the chosen virtual point cloud dataset is reported (since SPCVFDataset version 1.1).</p><p>A virtual point cloud dataset is a simple XML format with the file extension .spcvf, which can be created with the 'Create Virtual Point Cloud Dataset' module.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Filename", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params  = [param]
		param = arcpy.Parameter(displayName="Tileshape", name="TILE_SHP", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_virtual', '2')
		Tool.Set_Option('FILENAME', parameters[0].valueAsText)
		Tool.Set_Output('TILE_SHP', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Get Grid from Virtual Point Cloud"
		self.description = "<p>The module allows one to retrieve a grid from a virtual point cloud dataset by applying the provided area-of-interest (AOI). The extent of the AOI can be provided either as polygon shapefile, grid or by coordinates. Optionally, an overlap can be added to the AOI. In case an overlap is used and the AOI is provided as polygon shapfile, only the bounding boxes of the polygons are used.</p><p>With polygon shapefiles additional functionality is available:</p><p>* in case one or more polygons are selected, only the selected polygons are used.</p><p>* in case the shapefile contains several polygons a grid dataset is outputted for each polygon. In case the 'Tilename' attribute is provided, the output files are named by this attribute. Otherwise the output file names are build from the lower left coordinate of each tile.</p><p>The derived datasets can be outputted either as grid list or written to an output directory. For the latter, you must provide a valid file path with the 'Optional Output Filepath' parameter.</p><p>Optionally, the query can be constrained by providing an attribute field and a value range that must be met.</p><p>A virtual point cloud dataset is a simple XML format with the file extension .spcvf, which can be created with the 'Create Virtual Point Cloud Dataset' module.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Filename", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params  = [param]
		param = arcpy.Parameter(displayName="Grid", name="GRID_OUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Optional Output Filepath", name="FILEPATH", direction="Input", parameterType="Optional", datatype="DEFolder")
		params += [param]
		param = arcpy.Parameter(displayName="Attribute Field to Grid", name="ATTR_FIELD_GRID", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="CELL_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Grid System Fit", name="GRID_SYSTEM_FIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nodes", "cells"]
		param.value = "cells"
		params += [param]
		param = arcpy.Parameter(displayName="Aggregation", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["lowest", "highest"]
		param.value = "highest"
		params += [param]
		param = arcpy.Parameter(displayName="Constrain Query", name="CONSTRAIN_QUERY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Attribute Field", name="ATTR_FIELD", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Value Range (Minimum)", name="VALUE_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Value Range (Maximum)", name="VALUE_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Shape", name="AOI_SHP", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Tilename", name="FIELD_TILENAME", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["AOI_SHP"]
		params += [param]
		param = arcpy.Parameter(displayName="Grid", name="AOI_GRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X-Extent (Minimum)", name="AOI_XRANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="X-Extent (Maximum)", name="AOI_XRANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y-Extent (Minimum)", name="AOI_YRANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y-Extent (Maximum)", name="AOI_YRANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Add Overlap", name="AOI_ADD_OVERLAP", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Overlap", name="OVERLAP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_virtual', '4')
		Tool.Set_Option('FILENAME', parameters[0].valueAsText)
		Tool.Set_Output('GRID_OUT', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('FILEPATH', parameters[2].valueAsText)
		Tool.Set_Option('ATTR_FIELD_GRID', parameters[3].valueAsText)
		Tool.Set_Option('CELL_SIZE', parameters[4].valueAsText)
		Tool.Set_Option('GRID_SYSTEM_FIT', parameters[5].valueAsText)
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Set_Option('CONSTRAIN_QUERY', parameters[7].valueAsText)
		Tool.Set_Option('ATTR_FIELD', parameters[8].valueAsText)
		Tool.Set_Option('VALUE_RANGE_MIN', parameters[9].valueAsText)
		Tool.Set_Option('VALUE_RANGE_MAX', parameters[10].valueAsText)
		Tool.Set_Input ('AOI_SHP', parameters[11].valueAsText, 'shapes')
		Tool.Set_Option('FIELD_TILENAME', parameters[12].valueAsText)
		Tool.Set_Input ('AOI_GRID', parameters[13].valueAsText, 'grid')
		Tool.Set_Option('AOI_XRANGE_MIN', parameters[14].valueAsText)
		Tool.Set_Option('AOI_XRANGE_MAX', parameters[15].valueAsText)
		Tool.Set_Option('AOI_YRANGE_MIN', parameters[16].valueAsText)
		Tool.Set_Option('AOI_YRANGE_MAX', parameters[17].valueAsText)
		Tool.Set_Option('AOI_ADD_OVERLAP', parameters[18].valueAsText)
		Tool.Set_Option('OVERLAP', parameters[19].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Remove Overlap from Virtual Point Cloud Tiles"
		self.description = "<p>The module allows to remove the overlap from point cloud tiles created from a virtual point cloud dataset. The tiles must have been created with an overlap and a spcvf tile info file must have been outputted too. The latter decribes the original bounding boxes of the tiles (i.e. without overlap) and is used by this module to remove the overlap.</p><p>A virtual point cloud dataset is a simple XML format with the file extension .spcvf, which can be created with the 'Create Virtual Point Cloud Dataset' module. Point cloud tiles with an overlap are usually created from such an virtual point cloud dataset with the 'Get Subset from Virtual Point Cloud' module.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Tile Info File", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params  = [param]
		param = arcpy.Parameter(displayName="Output Filepath", name="FILEPATH", direction="Input", parameterType="Optional", datatype="DEFolder")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_virtual', '6')
		Tool.Set_Option('FILENAME', parameters[0].valueAsText)
		Tool.Set_Option('FILEPATH', parameters[1].valueAsText)
		Tool.Run()
		return
