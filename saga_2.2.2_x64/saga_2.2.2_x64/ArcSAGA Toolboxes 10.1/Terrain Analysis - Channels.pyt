import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Channels"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7]

class tool_0(object):
	def __init__(self):
		self.label = "Channel Network"
		self.description = "<p>This module derives a channel network based on gridded digital elevation data.</p><p>Use the initiation options to determine under which conditions channels shall start.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Flow Direction", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Network", name="CHNLNTWRK", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Direction", name="CHNLROUTE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Network", name="SHAPES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Initiation Grid", name="INIT_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Initiation Type", name="INIT_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Less than", "Equals", "Greater than"]
		param.value = "Greater than"
		params += [param]
		param = arcpy.Parameter(displayName="Initiation Threshold", name="INIT_VALUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Divergence", name="DIV_GRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tracing: Max. Divergence", name="DIV_CELLS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Tracing: Weight", name="TRACE_WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min. Segment Length", name="MINLEN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CHNLNTWRK', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CHNLROUTE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('SHAPES', parameters[4].valueAsText, 'shapes')
		Tool.Set_Input ('INIT_GRID', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('INIT_METHOD', parameters[6].valueAsText)
		Tool.Set_Option('INIT_VALUE', parameters[7].valueAsText)
		Tool.Set_Input ('DIV_GRID', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('DIV_CELLS', parameters[9].valueAsText)
		Tool.Set_Input ('TRACE_WEIGHT', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('MINLEN', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Watershed Basins"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Channel Network", name="CHANNELS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sink Route", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Watershed Basins", name="BASINS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min. Size", name="MINSIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '1')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CHANNELS', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('BASINS', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('MINSIZE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Watershed Basins (Extended)"
		self.description = "<p>Extended watershed basin analysis. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Drainage Network", name="CHANNELS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Basins", name="BASINS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Subbasins", name="SUBBASINS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Basins", name="V_BASINS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Subbasins", name="V_SUBBASINS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="River Heads", name="HEADS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="River Mouths", name="MOUTHS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Distances", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '2')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CHANNELS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('BASINS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SUBBASINS', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('V_BASINS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Output('V_SUBBASINS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Output('HEADS', parameters[6].valueAsText, 'shapes')
		Tool.Set_Output('MOUTHS', parameters[7].valueAsText, 'shapes')
		Tool.Set_Option('DISTANCE', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Vertical Distance to Channel Network"
		self.description = "<p>This module calculates the vertical distance to a channel network base level. The algorithm consists of two major steps:</p><p> 1. Interpolation of a channel network base level elevation</p><p> 2. Subtraction of this base level from the original elevations</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Channel Network", name="CHANNELS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Distance to Channel Network", name="DISTANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Network Base Level", name="BASELEVEL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tension Threshold [Percentage of Cell Size]", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Keep Base Level below Surface", name="NOUNDERGROUND", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '3')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CHANNELS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DISTANCE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('BASELEVEL', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[4].valueAsText)
		Tool.Set_Option('NOUNDERGROUND', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Overland Flow Distance to Channel Network"
		self.description = "<p>This module calculates overland flow distances to a channel network based on gridded digital elevation data and channel network information. The flow algorithm may be either Deterministic 8 (O'Callaghan & Mark 1984) or Multiple Flow Direction (Freeman 1991). Sediment Delivery Rates (SDR) according to Ali & De Boer (2010) can be computed optionally. </p><p></p><p>References:</p><p>- Ali, K. F., De Boer, D. H. (2010): Spatially distributed erosion and sediment yield modeling in the upper Indus River basin. Water Resources Research, 46(8), W08504. doi:10.1029/2009WR008762</p><p>- Freeman, G.T., 1991: Calculating catchment area with divergent flow based on a regular grid. Computers and Geosciences, 17:413-22.</p><p>- O'Callaghan, J.F., Mark, D.M., 1984: The extraction of drainage networks from digital elevation data. Computer Vision, Graphics and Image Processing, 28:323-344.</p><p>- Nobre, A.D., Cuartas, L.A., Hodnett, M., Renno, C.D., Rodrigues, G., Silveira, A., Waterloo, M., Saleska S. (2011): Height Above the Nearest Drainage - a hydrologically relevant new terrain model. Journal of Hydrology, Vol. 404, Issues 1-2, pp. 13-29, ISSN 0022-1694, 10.1016/j.jhydrol.2011.03.051. <a target=\"_blank\" href=\"http://www.sciencedirect.com/science/article/pii/S0022169411002599\">online</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Channel Network", name="CHANNELS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Preferred Routing", name="ROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Overland Flow Distance", name="DISTANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Overland Flow Distance", name="DISTVERT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Horizontal Overland Flow Distance", name="DISTHORZ", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Travel Time", name="TIME", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sediment Yield Delivery Ratio", name="SDR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fields", name="FIELDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fields Visited", name="PASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Algorithm", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["D8", "MFD"]
		param.value = "MFD"
		params += [param]
		param = arcpy.Parameter(displayName="Beta", name="FLOW_B", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Manning-Strickler Coefficient", name="FLOW_K", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="FLOW_K_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 20.000000
		params += [param]
		param = arcpy.Parameter(displayName="Flow Depth", name="FLOW_R", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="FLOW_R_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.050000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '4')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CHANNELS', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('ROUTE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DISTANCE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('DISTVERT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('DISTHORZ', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('TIME', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SDR', parameters[7].valueAsText, 'grid')
		Tool.Set_Input ('FIELDS', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('PASSES', parameters[9].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[10].valueAsText)
		Tool.Set_Option('FLOW_B', parameters[11].valueAsText)
		Tool.Set_Input ('FLOW_K', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('FLOW_K_DEFAULT', parameters[13].valueAsText)
		Tool.Set_Input ('FLOW_R', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('FLOW_R_DEFAULT', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Channel Network and Drainage Basins"
		self.description = "<p>Deterministic 8 based flow network analysis</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Flow Direction", name="DIRECTION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Connectivity", name="CONNECTION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Strahler Order", name="ORDER", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Drainage Basins", name="BASIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channels", name="SEGMENTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Drainage Basins", name="BASINS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Junctions", name="NODES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '5')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DIRECTION', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CONNECTION', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('ORDER', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('BASIN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('SEGMENTS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Output('BASINS', parameters[6].valueAsText, 'shapes')
		Tool.Set_Output('NODES', parameters[7].valueAsText, 'shapes')
		Tool.Set_Option('THRESHOLD', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Strahler Order"
		self.description = "<p>(c) 2004 by Victor Olaya. Strahler Order Calculation<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Strahler Order", name="STRAHLER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '6')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('STRAHLER', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Valley Depth"
		self.description = "<p>Valley depth is calculated here  vertical distance to a channel network base level. The algorithm consists of two major steps:</p><p> 1. Interpolation of a channel network base level elevation</p><p> 2. Subtraction of this base level from the original elevations</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Valley Depth", name="VALLEY_DEPTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Ridge Level", name="RIDGE_LEVEL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tension Threshold [Percentage of Cell Size]", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Keep Ridge Level above Surface", name="NOUNDERGROUND", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Ridge Detection Threshold", name="ORDER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_channels', '7')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VALLEY_DEPTH', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RIDGE_LEVEL', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[3].valueAsText)
		Tool.Set_Option('NOUNDERGROUND', parameters[4].valueAsText)
		Tool.Set_Option('ORDER', parameters[5].valueAsText)
		Tool.Run()
		return
