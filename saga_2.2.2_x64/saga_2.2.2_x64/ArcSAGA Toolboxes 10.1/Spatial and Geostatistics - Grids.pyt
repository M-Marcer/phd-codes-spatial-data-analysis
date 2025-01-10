import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grids"
		self.alias = ""
		self.tools = [tool_0, tool_2, tool_3, tool_4, tool_5, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13]

class tool_0(object):
	def __init__(self):
		self.label = "Fast Representativeness"
		self.description = "<p>A fast representativeness algorithm. Resulting seeds might be used with 'Fast Region Growing'.</p><p></p><p>References:</p><p>Boehner, J., Selige, T., Ringeler, A. (2006): Image segmentation using representativeness analysis and region growing. In: Boehner, J., McCloy, K.R., Strobl, J. [Eds.]:  SAGA – Analysis and Modelling Applications. Goettinger Geographische Abhandlungen, Vol.115, <a href=\"http://downloads.sourceforge.net/saga-gis/gga115_03.pdf\">pdf</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output Lod", name="RESULT_LOD", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output Seeds", name="SEEDS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Level of Generalisation", name="LOD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 16.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT_LOD', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SEEDS', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Representativeness (Grid)"
		self.description = "<p>Representativeness - calculation of the variance within a given search radius.</p><p></p><p>Reference:</p><p>- Boehner, J., Koethe, R., Trachinow, C. (1997): 'Weiterentwicklung der automatischen Reliefanalyse auf der Basis von Digitalen Gelaendemodellen', Goettinger Geographische Abhandlungen, Vol.100, p.3-21</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Representativeness", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Exponent", name="EXPONENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '2')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[2].valueAsText)
		Tool.Set_Option('EXPONENT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Radius of Variance (Grid)"
		self.description = "<p>Find the radius within which the cell values exceed the given variance criterium. This module is closely related to the representativeness calculation (variance within given search radius). For easier usage, the variance criterium is entered as standard deviation value. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Variance Radius", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="VARIANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Radius (cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Type of Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Cells", "Map Units"]
		param.value = "Cells"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '3')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('VARIANCE', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Statistics for Grids"
		self.description = "<p>Calculates statistical properties (arithmetic mean, minimum, maximum, variance, standard deviation) for each cell position for the values of the selected grids.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean less Standard Deviation", name="STDDEVLO", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean plus Standard Deviation", name="STDDEVHI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PCTL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PCTL_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '4')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('MEAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MIN', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('MAX', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('RANGE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('SUM', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('VAR', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('STDDEVLO', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('STDDEVHI', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('PCTL', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('PCTL_VAL', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Zonal Grid Statistics"
		self.description = "<p>The module calculates zonal statistics and reports these in a table. The module can be used to create a contingency table of unique condition units (UCUs). These units are delineated from a zonal grid (e.g. sub catchments) and optional categorical grids (e.g. landcover, soil, ...). It is possible to calculate descriptive statistics (n, min, max, mean, standard deviation and sum) for each UCU from optional grids with continious data (e.g. slope; aspect must be handled specially, please use the \"Aspect\" input parameter for such a grid). The number of input grids is only limited by available memory.</p><p></p><p>The module has four different modes of operation:</p><p>(1) only a zonal grid is used as input. This results in a simple contingency table with the number of grid cells in each zone.</p><p>(2) a zonal grid and additional categorical grids are used as input. This results in a contingency table with the number of cells in each UCU.</p><p>(3) a zonal grid and additional grids with continuous data are used as input. This results in a contingency table with the number of cells in each zone and some simple statistics for each zone. The statistics are calculated for each continuous grid.</p><p>(4) a zonal grid, additional categorical grids and additional grids with continuous data are used as input. This results in a contingency table with the number of cells in each UCU and the corresponding statistics for each continuous grid.</p><p></p><p>Depending on the mode of operation, the output table contains information about the categorical combination of each UCU, the number of cells in each UCU and the statistics for each UCU. A typical output table may look like this:</p><p><table border=\"1\"><tr><td>ID Zone</td><td>ID 1stCat</td><td>ID 2ndCat</td><td>Count UCU</td><td>N 1stCont</td><td>MIN 1stCont</td><td>MAX 1stCont</td><td>MEAN 1stCont</td><td>STDDEV 1stCont</td><td>SUM 1stCont</td></tr><tr><td>0      </td><td>2        </td><td>6        </td><td>6        </td><td>6        </td><td>708.5      </td><td>862.0      </td><td>734.5       </td><td>62.5          </td><td>4406.8     </td></tr><tr><td>0      </td><td>3        </td><td>4        </td><td>106      </td><td>106      </td><td>829.1      </td><td>910.1      </td><td>848.8       </td><td>28.5          </td><td>89969.0    </td></tr></table><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Zone Grid", name="ZONES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Categorical Grids", name="CATLIST", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Grids to analyse", name="STATLIST", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Zonal Statistics", name="OUTTAB", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Short Field Names", name="SHORTNAMES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '5')
		Tool.Set_Input ('ZONES', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CATLIST', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('STATLIST', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('ASPECT', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('OUTTAB', parameters[4].valueAsText, 'table')
		Tool.Set_Option('SHORTNAMES', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Global Moran's I for Grids"
		self.description = "<p>Global spatial autocorrelation for grids calculated as Moran's I.</p><p></p><p>References:</p><p>- Lloyd, C.D. (2010): Spatial data analysis - An introduction for GIS users. Oxford. 206p.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Case of contiguity", name="CONTIGUITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rook", "Queen"]
		param.value = "Queen"
		params += [param]
		param = arcpy.Parameter(displayName="Show Result in Dialog", name="DIALOG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '7')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'table')
		Tool.Set_Option('CONTIGUITY', parameters[2].valueAsText)
		Tool.Set_Option('DIALOG', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Principle Components Analysis"
		self.description = "<p>Principle Components Analysis (PCA) for grids. Implementation based on F. Murtagh's <a target=\"_blank\" href=\"http://lib.stat.cmu.edu/multi/pca.c\">code</a> as provided by the <a target=\"_blank\" href=\"http://lib.stat.cmu.edu\">StatLib</a> web site.</p><p></p><p>References:</p><p>Bahrenberg, G., Giese, E., Nipper, J. (1992): Statistische Methoden in der Geographie 2 - Multivariate Statistik. pp.198-277.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Principle Components", name="PCA", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Eigen Vectors", name="EIGEN", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["correlation matrix", "variance-covariance matrix", "sums-of-squares-and-cross-products matrix"]
		param.value = "variance-covariance matrix"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Components", name="NFIRST", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '8')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('PCA', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('EIGEN', parameters[2].valueAsText, 'table')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('NFIRST', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Multi-Band Variation"
		self.description = "<p>Calculates for each cell the spectral variation based on feature space distances to the centroid for all cells in specified neighbourhood. The average distance has been used for Spectral Variation Hypothesis (SVH).</p><p></p><p>References:</p><p>- Palmer, M.W., Earls, P., Hoagland, B.W., White, P.S., Wohlgemuth, T. (2002): Quantitative tools for perfecting species lists. Environmetrics 13, 121–137.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="BANDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Mean Distance", name="MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DIFF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius [Cells]", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "no distance weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '9')
		Tool.Set_Input ('BANDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('MEAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DIFF', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[4].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[6].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[7].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Inverse Principle Components Rotation"
		self.description = "<p>Inverse principle components rotation for grids. </p><p>References:</p><p>Bahrenberg, G., Giese, E., Nipper, J. (1992): Statistische Methoden in der Geographie 2 - Multivariate Statistik. pp.198-277.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Principle Components", name="PCA", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Eigen Vectors", name="EIGEN", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '10')
		Tool.Set_Input ('PCA', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('EIGEN', parameters[1].valueAsText, 'table')
		Tool.Set_Output('GRIDS', parameters[2].valueAsText, 'grid_list')
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Longitudinal Grid Statistics"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Latitudinal Statistics", name="STATS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '11')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('STATS', parameters[1].valueAsText, 'table')
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Meridional Grid Statistics"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Meridional Statistics", name="STATS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '12')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('STATS', parameters[1].valueAsText, 'table')
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Save Grid Statistics to Table"
		self.description = "<p>Calculates statistical properties (arithmetic mean, minimum, maximum, variance, standard deviation) for each of the given grids and saves it to a table.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Statistics for Grids", name="STATS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Data Cells", name="DATA_CELLS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Number of No-Data Cells", name="NODATA_CELLS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="CELLSIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Mean less Standard Deviation", name="STDDEVLO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mean plus Standard Deviation", name="STDDEVHI", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PCTL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PCTL_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '13')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('STATS', parameters[1].valueAsText, 'table')
		Tool.Set_Option('DATA_CELLS', parameters[2].valueAsText)
		Tool.Set_Option('NODATA_CELLS', parameters[3].valueAsText)
		Tool.Set_Option('CELLSIZE', parameters[4].valueAsText)
		Tool.Set_Option('MEAN', parameters[5].valueAsText)
		Tool.Set_Option('MIN', parameters[6].valueAsText)
		Tool.Set_Option('MAX', parameters[7].valueAsText)
		Tool.Set_Option('RANGE', parameters[8].valueAsText)
		Tool.Set_Option('VAR', parameters[9].valueAsText)
		Tool.Set_Option('STDDEV', parameters[10].valueAsText)
		Tool.Set_Option('STDDEVLO', parameters[11].valueAsText)
		Tool.Set_Option('STDDEVHI', parameters[12].valueAsText)
		Tool.Set_Option('PCTL', parameters[13].valueAsText)
		Tool.Set_Option('PCTL_VAL', parameters[14].valueAsText)
		Tool.Run()
		return
