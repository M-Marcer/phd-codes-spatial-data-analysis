import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Hydrology"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_4, tool_6, tool_7, tool_10, tool_13, tool_14, tool_15, tool_18, tool_19, tool_20, tool_21, tool_22, tool_23, tool_24, tool_25]

class tool_0(object):
	def __init__(self):
		self.label = "Flow Accumulation (Top-Down)"
		self.description = "<p>Top-down processing of cells for calculation of flow accumulation and related parameters. This set of algorithms processes a DEM downwards from the highest to the lowest cell.</p><p></p><p>References:</p><p></p><p>Deterministic 8</p><p>- O'Callaghan, J.F. / Mark, D.M. (1984):</p><p>    'The extraction of drainage networks from digital elevation data',</p><p>    Computer Vision, Graphics and Image Processing, 28:323-344</p><p></p><p>Rho 8:</p><p>- Fairfield, J. / Leymarie, P. (1991):</p><p>    'Drainage networks from grid digital elevation models',</p><p>    Water Resources Research, 27:709-717</p><p></p><p>Braunschweiger Reliefmodell:</p><p>- Bauer, J. / Rohdenburg, H. / Bork, H.-R. (1985):</p><p>    'Ein Digitales Reliefmodell als Vorraussetzung fuer ein deterministisches Modell der Wasser- und Stoff-Fluesse',</p><p>    Landschaftsgenese und Landschaftsoekologie, H.10, Parameteraufbereitung fuer deterministische Gebiets-Wassermodelle,</p><p>    Grundlagenarbeiten zu Analyse von Agrar-Oekosystemen, (Eds.: Bork, H.-R. / Rohdenburg, H.), p.1-15</p><p></p><p>Deterministic Infinity:</p><p>- Tarboton, D.G. (1997):</p><p>    'A new method for the determination of flow directions and upslope areas in grid digital elevation models',</p><p>    Water Resources Research, Vol.33, No.2, p.309-319</p><p></p><p>Multiple Flow Direction:</p><p>- Freeman, G.T. (1991):</p><p>    'Calculating catchment area with divergent flow based on a regular grid',</p><p>    Computers and Geosciences, 17:413-22</p><p></p><p>- Quinn, P.F. / Beven, K.J. / Chevallier, P. / Planchon, O. (1991):</p><p>    'The prediction of hillslope flow paths for distributed hydrological modelling using digital terrain models',</p><p>    Hydrological Processes, 5:59-79</p><p></p><p>Triangular Multiple Flow Direction</p><p>- Seibert, J. / McGlynn, B. (2007):</p><p>    'A new triangular multiple flow direction algorithm for computing upslope areas from gridded digital elevation models',</p><p>    Water Resources Research, Vol. 43, W04501</p><p>    C++ Implementation into SAGA by Thomas Grabs, Copyrights (c) 2007</p><p>    Contact: thomas.grabs@natgeo.su.se, jan.seibert@natgeo.su.se </p><p></p><p>Multiple Flow Direction based on Maximum Downslope Gradient:</p><p>- Qin, C. Z. / Zhu, A. X. / Pei, T. / Li, B. L. / Scholten, T. / Behrens, T. / & Zhou, C. H. (2011):</p><p>    'An approach to computing topographic wetness index based on maximum downslope gradient',</p><p>    Precision Agriculture, 12(1), 32-43.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weight", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="CAREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input for Mean over Catchment Calculation", name="VAL_INPUT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean over Catchment", name="VAL_MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Material", name="MATERIAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulation Target", name="TARGET", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total accumulated Material", name="ACCU_TOT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material from Left Side", name="ACCU_LEFT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material from Right Side", name="ACCU_RIGHT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation Unit", name="CAREA_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of cells", "cell area"]
		param.value = "cell area"
		params += [param]
		param = arcpy.Parameter(displayName="Flow Path Length", name="FLOWLEN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Linear Flow Threshold Grid", name="LINEAR_VAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Direction", name="LINEAR_DIR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Braunschweiger Reliefmodell", "Deterministic Infinity", "Multiple Flow Direction", "Multiple Triangular Flow Directon", "Multiple Maximum Downslope Gradient Based Flow Directon"]
		param.value = "Multiple Flow Direction"
		params += [param]
		param = arcpy.Parameter(displayName="Thresholded Linear Flow", name="LINEAR_DO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Linear Flow Threshold", name="LINEAR_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 500
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Suppress Negative Flow Accumulation Values", name="WEIGHT_GT_0", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHT', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CAREA', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('VAL_INPUT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('VAL_MEAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('MATERIAL', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('TARGET', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ACCU_TOT', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ACCU_LEFT', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ACCU_RIGHT', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('STEP', parameters[11].valueAsText)
		Tool.Set_Option('CAREA_UNIT', parameters[12].valueAsText)
		Tool.Set_Output('FLOWLEN', parameters[13].valueAsText, 'grid')
		Tool.Set_Input ('LINEAR_VAL', parameters[14].valueAsText, 'grid')
		Tool.Set_Input ('LINEAR_DIR', parameters[15].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[16].valueAsText)
		Tool.Set_Option('LINEAR_DO', parameters[17].valueAsText)
		Tool.Set_Option('LINEAR_MIN', parameters[18].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[19].valueAsText)
		Tool.Set_Option('WEIGHT_GT_0', parameters[20].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Flow Accumulation (Recursive)"
		self.description = "<p>Recursive upward processing of cells for calculation of flow accumulation and related parameters. This set of algorithms processes recursively all upwards connected cells until each cell of the DEM has been processed.</p><p></p><p>References:</p><p></p><p>Deterministic 8</p><p>- O'Callaghan, J.F. / Mark, D.M. (1984):</p><p>    'The extraction of drainage networks from digital elevation data',</p><p>    Computer Vision, Graphics and Image Processing, 28:323-344</p><p></p><p>Rho 8:</p><p>- Fairfield, J. / Leymarie, P. (1991):</p><p>    'Drainage networks from grid digital elevation models',</p><p>    Water Resources Research, 27:709-717</p><p></p><p>Deterministic Infinity:</p><p>- Tarboton, D.G. (1997):</p><p>    'A new method for the determination of flow directions and upslope areas in grid digital elevation models',</p><p>    Water Resources Research, Vol.33, No.2, p.309-319</p><p></p><p>Multiple m_Flow Direction:</p><p>- Freeman, G.T. (1991):</p><p>    'Calculating catchment area with divergent flow based on a regular grid',</p><p>    Computers and Geosciences, 17:413-22</p><p></p><p>- Quinn, P.F. / Beven, K.J. / Chevallier, P. / Planchon, O. (1991):</p><p>    'The prediction of hillslope flow paths for distributed hydrological modelling using digital terrain models',</p><p>    Hydrological Processes, 5:59-79</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weight", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="CAREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input for Mean over Catchment Calculation", name="VAL_INPUT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean over Catchment", name="VAL_MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Material", name="MATERIAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulation Target", name="TARGET", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total accumulated Material", name="ACCU_TOT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material from Left Side", name="ACCU_LEFT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material from Right Side", name="ACCU_RIGHT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation Unit", name="CAREA_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of cells", "cell area"]
		param.value = "cell area"
		params += [param]
		param = arcpy.Parameter(displayName="Target Areas", name="TARGETS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Path Length", name="FLOWLEN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Deterministic Infinity", "Multiple m_Flow Direction"]
		param.value = "Multiple m_Flow Direction"
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Suppress Negative Flow Accumulation Values", name="WEIGHT_GT_0", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '1')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHT', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CAREA', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('VAL_INPUT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('VAL_MEAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('MATERIAL', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('TARGET', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ACCU_TOT', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ACCU_LEFT', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ACCU_RIGHT', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('STEP', parameters[11].valueAsText)
		Tool.Set_Option('CAREA_UNIT', parameters[12].valueAsText)
		Tool.Set_Input ('TARGETS', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('FLOWLEN', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[15].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[16].valueAsText)
		Tool.Set_Option('WEIGHT_GT_0', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Flow Accumulation (Flow Tracing)"
		self.description = "<p>Flow tracing algorithms for calculations of flow accumulation and related parameters. These algorithms trace the flow of each cell in a DEM separately until it finally leaves the DEM or ends in a sink.</p><p></p><p>References:</p><p></p><p>Rho 8 (this implementation adopted the original algorithm only for the flow routing and will give quite different results):</p><p>- Fairfield, J. / Leymarie, P. (1991):</p><p>    'Drainage networks from grid digital elevation models',</p><p>    Water Resources Research, 27:709-717</p><p></p><p>Kinematic Routing Algorithm:</p><p>- Lea, N.L. (1992):</p><p>    'An aspect driven kinematic routing algorithm',</p><p>    in: Parsons, A.J., Abrahams, A.D. (Eds.), 'Overland Flow: hydraulics and erosion mechanics', London, 147-175</p><p></p><p>DEMON:</p><p>- Costa-Cabral, M. / Burges, S.J. (1994):</p><p>    'Digital Elevation Model Networks (DEMON): a model of flow over hillslopes for computation of contributing and dispersal areas',</p><p>    Water Resources Research, 30:1681-1692</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weight", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="CAREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input for Mean over Catchment Calculation", name="VAL_INPUT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean over Catchment", name="VAL_MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Material", name="MATERIAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulation Target", name="TARGET", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total accumulated Material", name="ACCU_TOT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material from Left Side", name="ACCU_LEFT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material from Right Side", name="ACCU_RIGHT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation Unit", name="CAREA_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of cells", "cell area"]
		param.value = "cell area"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rho 8", "Kinematic Routing Algorithm", "DEMON"]
		param.value = "Kinematic Routing Algorithm"
		params += [param]
		param = arcpy.Parameter(displayName="DEMON - Min. DQV", name="MINDQV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Flow Correction", name="CORRECT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '2')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHT', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CAREA', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('VAL_INPUT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('VAL_MEAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('MATERIAL', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('TARGET', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ACCU_TOT', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ACCU_LEFT', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ACCU_RIGHT', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('STEP', parameters[11].valueAsText)
		Tool.Set_Option('CAREA_UNIT', parameters[12].valueAsText)
		Tool.Set_Option('METHOD', parameters[13].valueAsText)
		Tool.Set_Option('MINDQV', parameters[14].valueAsText)
		Tool.Set_Option('CORRECT', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Upslope Area"
		self.description = "<p>This module allows you to specify target cells, for which the upslope contributing area shall be identified. The result will give for each cell the percentage of its flow that reaches the target cell(s).</p><p></p><p>References:</p><p></p><p>Deterministic 8</p><p>- O'Callaghan, J.F. / Mark, D.M. (1984):</p><p>    'The extraction of drainage networks from digital elevation data',</p><p>    Computer Vision, Graphics and Image Processing, 28:323-344</p><p></p><p>Deterministic Infinity:</p><p>- Tarboton, D.G. (1997):</p><p>    'A new method for the determination of flow directions and upslope areas in grid digital elevation models',</p><p>    Water Resources Research, Vol.33, No.2, p.309-319</p><p></p><p>Multiple Flow Direction:</p><p>- Freeman, G.T. (1991):</p><p>    'Calculating catchment area with divergent flow based on a regular grid',</p><p>    Computers and Geosciences, 17:413-22</p><p></p><p>- Quinn, P.F. / Beven, K.J. / Chevallier, P. / Planchon, O. (1991):</p><p>    'The prediction of hillslope flow paths for distributed hydrological modelling using digital terrain models',</p><p>    Hydrological Processes, 5:59-79</p><p></p><p>_______</p><p></p><p>This version uses all valid cells (not 'no data' values) of a given target grid to determine the contributing area. In case no target grid is provided as input, the specified x/y coordinates are used as target point.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Target Area", name="TARGET", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Target X coordinate", name="TARGET_PT_X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Y coordinate", name="TARGET_PT_Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Area", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Deterministic Infinity", "Multiple Flow Direction"]
		param.value = "Multiple Flow Direction"
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '4')
		Tool.Set_Input ('TARGET', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('TARGET_PT_X', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_PT_Y', parameters[2].valueAsText)
		Tool.Set_Input ('ELEVATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Set_Option('CONVERGE', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Flow Path Length"
		self.description = "<p>This module calculates the average flow path length starting from the seeds, that are given by the optional 'Seeds' grid and optionally from cells without upslope contributing areas (i.e. summits, ridges). Seeds will be all grid cells, that are not 'no data' values. If seeds are not given, only summits and ridges as given by the flow routing will be taken into account. Available flow routing methods are based on the 'Deterministic 8 (D8)' (Callaghan and Mark 1984) and the 'Multiple Flow Direction (FD8)' (Freeman 1991, Quinn et al. 1991) algorithms.</p><p></p><p>References:</p><p></p><p>Deterministic 8</p><p>- O'Callaghan, J.F. / Mark, D.M. (1984):</p><p>    'The extraction of drainage networks from digital elevation data',</p><p>    Computer Vision, Graphics and Image Processing, 28:323-344</p><p></p><p>- Freeman, G.T. (1991):</p><p>    'Calculating catchment area with divergent flow based on a regular grid',</p><p>    Computers and Geosciences, 17:413-22</p><p></p><p>- Quinn, P.F. / Beven, K.J. / Chevallier, P. / Planchon, O. (1991):</p><p>    'The prediction of hillslope flow paths for distributed hydrological modelling using digital terrain models',</p><p>    Hydrological Processes, 5:59-79</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Seeds", name="SEED", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Path Length", name="LENGTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seeds Only", name="SEEDS_ONLY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Flow Routing Algorithm", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8 (D8)", "Multiple Flow Direction (FD8)"]
		param.value = "Multiple Flow Direction (FD8)"
		params += [param]
		param = arcpy.Parameter(displayName="Convergence (FD8)", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '6')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SEED', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('LENGTH', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('SEEDS_ONLY', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Slope Length"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope Length", name="LENGTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '7')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LENGTH', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Cell Balance"
		self.description = "<p>(c) 2004 by Victor Olaya. Cell Balance Calculation</p><p>References:</p><p> 1. Olaya, V. Hidrologia computacional y modelos digitales del terreno. Alqua. 536 pp. 2004<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="WEIGHTS_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cell Balance", name="BALANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Multiple Flow Direction"]
		param.value = "Deterministic 8"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '10')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHTS', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('WEIGHTS_DEFAULT', parameters[2].valueAsText)
		Tool.Set_Output('BALANCE', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Edge Contamination"
		self.description = "<p>This tool uses flow directions to estimate possible contamination effects moving from outside of the grid passing the edge into its interior. This means that derived contributing area values might be underestimated for the marked cells. Cells not contamined will be marked as no data. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Edge Contamination", name="CONTAMINATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["single flow direction", "multiple flow direction"]
		param.value = "single flow direction"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '13')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONTAMINATION', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "SAGA Wetness Index"
		self.description = "<p>The 'SAGA Wetness Index' is, as the name says, similar to the 'Topographic Wetness Index' (TWI), but it is based on a modified catchment area calculation ('Modified Catchment Area'), which does not think of the flow as very thin film. As result it predicts for cells situated in valley floors with a small vertical distance to a channel a more realistic, higher potential soil moisture compared to the standard TWI calculation.</p><p></p><p>References</p><p>- Boehner, J., Koethe, R. Conrad, O., Gross, J., Ringeler, A., Selige, T. (2002): Soil Regionalisation by Means of Terrain Analysis and Process Parameterisation. In: Micheli, E., Nachtergaele, F., Montanarella, L. [Ed.]: Soil Classification 2001. European Soil Bureau, Research Report No. 7, EUR 20398 EN, Luxembourg. pp.213-222.</p><p></p><p>- Boehner, J. and Selige, T. (2006): Spatial prediction of soil attributes using terrain analysis and climate regionalisation. In: Boehner, J., McCloy, K.R., Strobl, J. [Ed.]: SAGA - Analysis and Modelling Applications, Goettinger Geographische Abhandlungen, Goettingen: 13-28. (<a target=\"_blank\" href=\"http://downloads.sourceforge.net/saga-gis/gga115_02.pdf\">pdf</a>)</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Catchment area", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Catchment slope", name="SLOPE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Modified Catchment Area", name="AREA_MOD", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="TWI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Suction", name="SUCTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Type of Area", name="AREA_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["absolute catchment area", "square root of catchment area", "specific catchment area"]
		param.value = "square root of catchment area"
		params += [param]
		param = arcpy.Parameter(displayName="Type of Slope", name="SLOPE_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local slope", "catchment slope"]
		param.value = "catchment slope"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Slope", name="SLOPE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Offset Slope", name="SLOPE_OFF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Weighting", name="SLOPE_WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '15')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('AREA_MOD', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('TWI', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('SUCTION', parameters[6].valueAsText)
		Tool.Set_Option('AREA_TYPE', parameters[7].valueAsText)
		Tool.Set_Option('SLOPE_TYPE', parameters[8].valueAsText)
		Tool.Set_Option('SLOPE_MIN', parameters[9].valueAsText)
		Tool.Set_Option('SLOPE_OFF', parameters[10].valueAsText)
		Tool.Set_Option('SLOPE_WEIGHT', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Lake Flood"
		self.description = "<p>This module can be used to flood a digital elevation model from seed points. Seed points have to be coded either with local water depth or absolute water level.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="ELEV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Seeds", name="SEEDS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Absolute Water Levels", name="LEVEL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Lake", name="OUTDEPTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Surface", name="OUTLEVEL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '16')
		Tool.Set_Input ('ELEV', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SEEDS', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('LEVEL', parameters[2].valueAsText)
		Tool.Set_Output('OUTDEPTH', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('OUTLEVEL', parameters[4].valueAsText, 'grid')
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Flow Width and Specific Catchment Area"
		self.description = "<p>Flow width and specific catchment area (SCA) calculation.</p><p></p><p>References:</p><p>Gruber, S., Peckham, S. (2008): Land-Surface Parameters and Objects in Hydrology. In: Hengl, T. and Reuter, H.I. [Eds.]: Geomorphometry: Concepts, Software, Applications. Developments in Soil Science, Elsevier, 33:293-308.</p><p></p><p>Quinn, P.F., Beven, K.J., Chevallier, P., Planchon, O. (1991): The prediction of hillslope flow paths for distributed hydrological modelling using digital terrain models. Hydrological Processes, 5:59-79</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Flow Width", name="WIDTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Catchment Area (TCA)", name="TCA", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Specific Catchment Area (SCA)", name="SCA", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Multiple Flow Direction (Quinn et al. 1991)", "Aspect"]
		param.value = "Aspect"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '19')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('WIDTH', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('TCA', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SCA', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Topographic Wetness Index (TWI)"
		self.description = "<p>Calculation of the slope and specific catchment area (SCA) based Topographic Wetness Index (TWI)</p><p></p><p>References:</p><p></p><p>Beven, K.J., Kirkby, M.J. (1979):</p><p>A physically-based variable contributing area model of basin hydrology'</p><p>Hydrology Science Bulletin 24(1), p.43-69</p><p></p><p>Boehner, J., Selige, T. (2006):</p><p>Spatial Prediction of Soil Attributes Using Terrain Analysis and Climate Regionalisation'</p><p>In: Boehner, J., McCloy, K.R., Strobl, J.: 'SAGA - Analysis and Modelling Applications', Goettinger Geographische Abhandlungen, Vol.115, p.13-27</p><p></p><p>Moore, I.D., Grayson, R.B., Ladson, A.R. (1991):</p><p>'Digital terrain modelling: a review of hydrogical, geomorphological, and biological applications'</p><p>Hydrological Processes, Vol.5, No.1</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transmissivity", name="TRANS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="TWI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Area Conversion", name="CONV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no conversion (areas already given as specific catchment area)", "1 / cell size (pseudo specific catchment area)"]
		param.value = "no conversion (areas already given as specific catchment area)"
		params += [param]
		param = arcpy.Parameter(displayName="Method (TWI)", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Standard", "TOPMODEL"]
		param.value = "Standard"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '20')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('TRANS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('TWI', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('CONV', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Stream Power Index"
		self.description = "<p>Calculation of stream power index based on slope and specific catchment area (SCA).</p><p>SPI = SCA * tan(Slope)</p><p></p><p>References:</p><p></p><p>Moore, I.D., Grayson, R.B., Ladson, A.R. (1991):</p><p>'Digital terrain modelling: a review of hydrogical, geomorphological, and biological applications'</p><p>Hydrological Processes, Vol.5, No.1</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Stream Power Index", name="SPI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Area Conversion", name="CONV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no conversion (areas already given as specific catchment area)", "1 / cell size (pseudo specific catchment area)"]
		param.value = "no conversion (areas already given as specific catchment area)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '21')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SPI', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CONV', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "LS Factor"
		self.description = "<p>Calculation of slope length (LS) factor as used by the Universal Soil Loss Equation (USLE), based on slope and specific catchment area (SCA, as substitute for slope length). </p><p>References:</p><p></p><p>Boehner, J., Selige, T. (2006):</p><p>Spatial Prediction of Soil Attributes Using Terrain Analysis and Climate Regionalisation'</p><p>In: Boehner, J., McCloy, K.R., Strobl, J.: 'SAGA - Analysis and Modelling Applications', Goettinger Geographische Abhandlungen, Vol.115, p.13-27</p><p></p><p>Desmet & Govers (1996):</p><p>'A GIS Procedure for Automatically Calculating the USLE LS Factor on Topographically Complex Landscape Units'</p><p>Journal of Soil and Water Conservation, 51(5):427.433</p><p></p><p>Kinnell, P.I.A. (2005):</p><p>'Alternative Approaches for Determining the USLE-M Slope Length Factor for Grid Cells.'</p><p><a href=\"http://soil.scijournals.org/cgi/content/full/69/3/674\">http://soil.scijournals.org/cgi/content/full/69/3/674</a></p><p></p><p>Moore, I.D., Grayson, R.B., Ladson, A.R. (1991):</p><p>'Digital terrain modelling: a review of hydrogical, geomorphological, and biological applications'</p><p>Hydrological Processes, Vol.5, No.1</p><p></p><p>Wischmeier, W.H., Smith, D.D. (1978):</p><p>'Predicting rainfall erosion losses - A guide to conservation planning'</p><p>Agriculture Handbook No. 537: US Department of Agriculture, Washington DC.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LS Factor", name="LS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Area to Length Conversion", name="CONV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no conversion (areas already given as specific catchment area)", "1 / cell size (specific catchment area)", "square root (catchment length)"]
		param.value = "no conversion (areas already given as specific catchment area)"
		params += [param]
		param = arcpy.Parameter(displayName="Method (LS)", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Moore et al. 1991", "Desmet & Govers 1996", "Boehner & Selige 2006"]
		param.value = "Moore et al. 1991"
		params += [param]
		param = arcpy.Parameter(displayName="Rill/Interrill Erosivity", name="EROSIVITY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stability", name="STABILITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["stable", "instable (thawing)"]
		param.value = "stable"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '22')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('LS', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CONV', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('EROSIVITY', parameters[5].valueAsText)
		Tool.Set_Option('STABILITY', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "Melton Ruggedness Number"
		self.description = "<p>Melton ruggedness number (MNR) is a simple flow accumulation related index, calculated as difference between maximum and minimum elevation in catchment area divided by square root of catchment area size. The calculation is performed for each grid cell, therefore minimum elevation is same as elevation at cell's position. Due to the discrete character of a single maximum elevation, flow calculation is simply done with Deterministic 8. </p><p></p><p>References:</p><p>Marchi, L. &  Fontana, G.D. (2005): GIS morphometric indicators for the analysis of sediment dynamics in mountain basins. Environ. Geol. 48:218-228, DOI 10.1007/s00254-005-1292-4.</p><p></p><p>Melton M.A. (1965): The geomorphic and paleoclimatic significance of alluvial deposits in Southern Arizona. J. Geol. 73:1-38.</p><p></p><p>O'Callaghan, J.F. / Mark, D.M. (1984): The extraction of drainage networks from digital elevation data. Computer Vision, Graphics and Image Processing 28:323-344.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Height", name="ZMAX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Melton Ruggedness Number", name="MRN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '23')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ZMAX', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('MRN', parameters[3].valueAsText, 'grid')
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "TCI Low"
		self.description = "<p>Terrain Classification Index for Lowlands (TCI Low).</p><p></p><p>Reference:</p><p>Bock, M., Boehner, J., Conrad, O., Koethe, R., Ringeler, A. (2007): Methods for creating Functional Soil Databases and applying Digital Soil Mapping with SAGA GIS. In: Hengl, T., Panagos, P., Jones, A., Toth, G. [Eds.]: Status and prospect of soil information in south-eastern Europe: soil databases, projects and applications. EUR 22646 EN Scientific and Technical Research series, Office for Official Publications of the European Communities, Luxemburg, p.149-162. <a target=\"_blank\" href=\"http://eusoils.jrc.ec.europa.eu/ESDB_Archive/eusoils_docs/esb_rr/EUR22646EN.pdf\">online</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Vertical Distance to Channel Network", name="DISTANCE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="TWI", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="TCI Low", name="TCILOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '24')
		Tool.Set_Input ('DISTANCE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('TWI', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('TCILOW', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "LS-Factor, Field Based"
		self.description = "<p>Calculation of slope length (LS) factor as used for the Universal Soil Loss Equation (USLE), based on slope and (specific) catchment area, latter as substitute for slope length. This tool takes only a Digital Elevation Model (DEM) as input and derives catchment areas according to Freeman (1991). Optionally field polygons can be supplied. Is this the case, calculations will be performed field by field, i.e. catchment area calculation is restricted to each field's area. </p><p>References:</p><p></p><p>Boehner, J., Selige, T. (2006): Spatial Prediction of Soil Attributes Using Terrain Analysis and Climate Regionalisation. In: Boehner, J., McCloy, K.R., Strobl, J.: 'SAGA - Analysis and Modelling Applications', Goettinger Geographische Abhandlungen, 115, 13-27.</p><p></p><p>Desmet, P.J.J., Govers, G. (1996): A GIS Procedure for Automatically Calculating the USLE LS Factor on Topographically Complex Landscape Units. Journal of Soil and Water Conservation, 51(5), 427-433.</p><p></p><p>Freeman, G.T. (1991): Calculating catchment area with divergent flow based on a regular grid. Computers and Geosciences, 17:413-22</p><p></p><p>Kinnell, P.I.A. (2005): Alternative Approaches for Determining the USLE-M Slope Length Factor for Grid Cells. <a href=\"online\">https://www.soils.org/publications/sssaj/abstracts/69/3/0674</a></p><p></p><p>Moore, I.D., Grayson, R.B., Ladson, A.R. (1991): Digital terrain modelling: a review of hydrogical, geomorphological, and biological applications. Hydrological Processes, 5(1).</p><p></p><p>Moore, I.D., Nieber, J.L. (1991): Landscape assessment of soil erosion and nonpoint source pollution. J. Minnesota Acad. Sci., 55, 18-25.</p><p></p><p>Wischmeier, W.H., Smith, D.D. (1978): Predicting rainfall erosion losses - A guide to conservation planning. Agriculture Handbook No. 537: US Department of Agriculture, Washington DC.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Fields", name="FIELDS", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Field Statistics", name="STATISTICS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Length Factor", name="UPSLOPE_AREA", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Effective Flow Length", name="UPSLOPE_LENGTH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Slope", name="UPSLOPE_SLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LS Factor", name="LS_FACTOR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sediment Balance", name="BALANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LS Calculation", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Moore & Nieber 1989", "Desmet & Govers 1996", "Wischmeier & Smith 1978"]
		param.value = "Moore & Nieber 1989"
		params += [param]
		param = arcpy.Parameter(displayName="Type of Slope", name="METHOD_SLOPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local slope", "distance weighted average catchment slope"]
		param.value = "local slope"
		params += [param]
		param = arcpy.Parameter(displayName="Specific Catchment Area", name="METHOD_AREA", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["specific catchment area (contour length simply as cell size)", "specific catchment area (contour length dependent on aspect)", "catchment length (square root of catchment area)", "effective flow length"]
		param.value = "specific catchment area (contour length dependent on aspect)"
		params += [param]
		param = arcpy.Parameter(displayName="Stop at Edge", name="STOP_AT_EDGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Rill/Interrill Erosivity", name="EROSIVITY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stability", name="STABILITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["stable", "instable (thawing)"]
		param.value = "stable"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '25')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('FIELDS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('STATISTICS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('UPSLOPE_AREA', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('UPSLOPE_LENGTH', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('UPSLOPE_SLOPE', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('LS_FACTOR', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('BALANCE', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[8].valueAsText)
		Tool.Set_Option('METHOD_SLOPE', parameters[9].valueAsText)
		Tool.Set_Option('METHOD_AREA', parameters[10].valueAsText)
		Tool.Set_Option('STOP_AT_EDGE', parameters[11].valueAsText)
		Tool.Set_Option('EROSIVITY', parameters[12].valueAsText)
		Tool.Set_Option('STABILITY', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Slope Limited Flow Accumulation"
		self.description = "<p>Flow accumulation is calculated as upslope contributing (catchment) area using the multiple flow direction approach of Freeman (1991). For this tool the approach has been modified to limit the flow portion routed through a cell depending on the local slope. If a cell is not inclined, no flow is routed through it at all. With increasing slopes the portion of flow routed through a cell becomes higher. Cells with slopes greater than a specified slope threshold route their entire accumulated flow downhill. </p><p>References:</p><p>- Freeman, G.T. (1991): Calculating catchment area with divergent flow based on a regular grid. Computers and Geosciences, 17:413-22</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Weight", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="FLOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope Minimum", name="SLOPE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Threshold", name="SLOPE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Use Flow Threshold", name="B_FLOW", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Flow Threshold (Minimum)", name="T_FLOW_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Flow Threshold (Maximum)", name="T_FLOW_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '26')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('FLOW', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('SLOPE_MIN', parameters[3].valueAsText)
		Tool.Set_Option('SLOPE_MAX', parameters[4].valueAsText)
		Tool.Set_Option('B_FLOW', parameters[5].valueAsText)
		Tool.Set_Option('T_FLOW_MIN', parameters[6].valueAsText)
		Tool.Set_Option('T_FLOW_MAX', parameters[7].valueAsText)
		Tool.Run()
		return
