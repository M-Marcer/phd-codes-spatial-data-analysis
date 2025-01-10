import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Morphometry"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_18, tool_19, tool_20, tool_21, tool_22, tool_23, tool_24, tool_25, tool_26, tool_27]

class tool_0(object):
	def __init__(self):
		self.label = "Slope, Aspect, Curvature"
		self.description = "<p>Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.</p><p></p><p>References:</p><p></p><p>Maximum Slope</p><p>- Travis, M.R., Elsner, G.H., Iverson, W.D., Johnson, C.G. (1975):</p><p>    'VIEWIT: computation of seen areas, slope, and aspect for land-use planning',</p><p>    USDA F.S. Gen. Tech. Rep. PSW-11/1975, 70p. Berkeley, California, U.S.A.</p><p></p><p>Maximum Triangle Slope</p><p>- Tarboton, D.G. (1997):</p><p>    'A new method for the determination of flow directions and upslope areas in grid digital elevation models',</p><p>    Water Resources Research, Vol.33, No.2, p.309-319</p><p></p><p>Least Squares or Best Fitted Plane</p><p>- Horn, B. K. (1981):</p><p>    'Hill shading and the relectance map',</p><p>    Proceedings of the IEEE, v. 69, no. 1, p. 14-47.</p><p></p><p>- Beasley, D.B., Huggins, L.F. (1982):</p><p>    'ANSWERS: User's manual',</p><p>    U.S. EPA-905/9-82-001, Chicago, IL. 54pp.</p><p></p><p>- Costa-Cabral, M., Burges, S.J., (1994):</p><p>    'Digital Elevation Model Networks (DEMON): a model of flow over hillslopes for computation of contributing and dispersal areas',</p><p>    Water Resources Research, v. 30, no. 6, p. 1681-1692.</p><p></p><p>Fit 2.Degree Polynom</p><p>- Evans, I.S. (1979):</p><p>    'An integrated system of terrain analysis and slope mapping',</p><p>    Final report on grant DA-ERO-591-73-G0040. University of Durham, England.</p><p></p><p>- Bauer, J., Rohdenburg, H., Bork, H.-R. (1985):</p><p>    'Ein Digitales Reliefmodell als Vorraussetzung fuer ein deterministisches Modell der Wasser- und Stoff-Fluesse',</p><p>    Landschaftsgenese und Landschaftsoekologie, H.10, Parameteraufbereitung fuer deterministische Gebiets-Wassermodelle,</p><p>    Grundlagenarbeiten zu Analyse von Agrar-Oekosystemen, (Eds.: Bork, H.-R. / Rohdenburg, H.), p.1-15</p><p></p><p>- Heerdegen, R.G., Beran, M.A. (1982):</p><p>    'Quantifying source areas through land surface curvature',</p><p>    Journal of Hydrology, Vol.57</p><p></p><p>- Olaya, V. (2006):</p><p>    'Basic Land-Surface Parameters',</p><p>     in: Hengl, T., Reuter, H.I. [Eds.]: Geomorphometry: Concepts, Software, Applications.      Developments in Soil Science, Elsevier, Vol.33, 141-169.</p><p></p><p>- Zevenbergen, L.W., Thorne, C.R. (1987):</p><p>    'Quantitative analysis of land surface topography',</p><p>    Earth Surface Processes and Landforms, 12: 47-56.</p><p></p><p>Fit 3.Degree Polynom</p><p>- R.M. Haralick (1983):</p><p>    'Ridge and valley detection on digital images',</p><p>    Computer Vision, Graphics and Image Processing, Vol.22, No.1, p.28-38</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="General Curvature", name="C_GENE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Curvature", name="C_PROF", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Plan Curvature", name="C_PLAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tangential Curvature", name="C_TANG", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Longitudinal Curvature", name="C_LONG", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Sectional Curvature", name="C_CROS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimal Curvature", name="C_MINI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximal Curvature", name="C_MAXI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Curvature", name="C_TOTA", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Line Curvature", name="C_ROTO", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum slope (Travis et al. 1975)", "maximum triangle slope (Tarboton 1997)", "least squares fitted plane (Horn 1981, Costa-Cabral & Burgess 1996)", "6 parameter 2nd order polynom (Evans 1979)", "6 parameter 2nd order polynom (Heerdegen & Beran 1982)", "6 parameter 2nd order polynom (Bauer, Rohdenburg, Bork 1985)", "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)", "10 parameter 3rd order polynom (Haralick 1983)"]
		param.value = "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)"
		params += [param]
		param = arcpy.Parameter(displayName="Slope Units", name="UNIT_SLOPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree", "percent"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Aspect Units", name="UNIT_ASPECT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ASPECT', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('C_GENE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('C_PROF', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('C_PLAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('C_TANG', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('C_LONG', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('C_CROS', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('C_MINI', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('C_MAXI', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('C_TOTA', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('C_ROTO', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[13].valueAsText)
		Tool.Set_Option('UNIT_SLOPE', parameters[14].valueAsText)
		Tool.Set_Option('UNIT_ASPECT', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Convergence Index"
		self.description = "<p>Reference:</p><p>Koethe, R. & Lehmeier, F. (1996): SARA - System zur Automatischen Relief-Analyse. User Manual, 2. Edition [Dept. of Geography, University of Goettingen, unpublished]</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Convergence Index", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Aspect", "Gradient"]
		param.value = "Aspect"
		params += [param]
		param = arcpy.Parameter(displayName="Gradient Calculation", name="NEIGHBOURS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["2 x 2", "3 x 3"]
		param.value = "2 x 2"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '1')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('NEIGHBOURS', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Surface Specific Points"
		self.description = "<p>References:</p><p>Peucker, T.K. and Douglas, D.H., 1975:</p><p>'Detection of surface-specific points by local parallel processing of discrete terrain elevation data',</p><p>Computer Graphics and Image Processing, 4, 375-387</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Mark Highest Neighbour", "Opposite Neighbours", "Flow Direction", "Flow Direction (up and down)", "Peucker & Douglas"]
		param.value = "Opposite Neighbours"
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '3')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Curvature Classification"
		self.description = "<p>Surface curvature based terrain classification.</p><p>Reference:</p><p>Dikau, R. (1988):</p><p>'Entwurf einer geomorphographisch-analytischen Systematik von Reliefeinheiten',</p><p>Heidelberger Geographische Bausteine, Heft 5</p><p></p><p>0 - V  / V</p><p>1 - GE / V</p><p>2 - X  / V</p><p>3 - V  / GR</p><p>4 - GE / GR</p><p>5 - X  / GR</p><p>6 - V  / X</p><p>7 - GE / X</p><p>8 - X  / X</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Curvature Classification", name="CLASS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for plane", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000500
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '4')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CLASS', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Hypsometry"
		self.description = "<p>Calculates the hypsometric curve for a given DEM.</p><p></p><p>The hypsometric curve is an empirical cumulative distribution function of elevations in a catchment or of a whole planet. The module calculates both the relative (scaled from 0 to 100 percent) and absolute (minimum to maximum values) distributions. The former scales elevation and area by the maximum values. Such a non-dimensional curve allows one to asses the similarity of watersheds as differences in hypsometric curves arise from different geomorphic processes shaping a landscape.</p><p></p><p>In case the hypsometric curve should not be calculated for the whole elevation range of the input dataset, a user-specified elevation range can be specified with the classification constant area.</p><p></p><p>The output table has two attribute columns with relative height and area values, and two columns with absolute height and area values. In order to plot the non-dimensional hypsometric curve as diagram, use the relative area as x-axis values and the relative height for the y-axis. For a diagram with absolute values, use the absolute area as x-axis values and the absolute height for the y-axis.</p><p></p><p>References:</p><p>- Harlin, J.M (1978):</p><p>    'Statistical moments of the hypsometric curve and its density function',</p><p>    J. Int. Assoc. Math. Geol., Vol.10, p.59-72</p><p></p><p>- Luo, W. (2000):</p><p>    'Quantifying groundwater-sapping landforms with a hypsometric technique',</p><p>    J. of Geophysical Research, Vol.105, No.E1, p.1685-1694</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Hypsometry", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Sort", name="SORTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["up", "down"]
		param.value = "down"
		params += [param]
		param = arcpy.Parameter(displayName="Classification Constant", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["height", "area"]
		param.value = "area"
		params += [param]
		param = arcpy.Parameter(displayName="Use Z-Range", name="BZRANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Z-Range (Minimum)", name="ZRANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Z-Range (Maximum)", name="ZRANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '5')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TABLE', parameters[1].valueAsText, 'table')
		Tool.Set_Option('COUNT', parameters[2].valueAsText)
		Tool.Set_Option('SORTING', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('BZRANGE', parameters[5].valueAsText)
		Tool.Set_Option('ZRANGE_MIN', parameters[6].valueAsText)
		Tool.Set_Option('ZRANGE_MAX', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Real Surface Area"
		self.description = "<p>Calculates real (not projected) cell area<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Surface Area", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '6')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Morphometric Protection Index"
		self.description = "<p>This algorithm analyses the immediate surrounding of each cell up to an given distance and evaluates how the relief protects it.</p><p>It is equivalent to the positive openness described in: Visualizing Topography by Openness: A New Application of Image Processing to Digital Elevation Models, Photogrammetric Engineering and Remote Sensing(68), No. 3, March 2002, pp. 257-266.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Protection Index", name="PROTECTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2000.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '7')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('PROTECTION', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Multiresolution Index of Valley Bottom Flatness (MRVBF)"
		self.description = "<p>Calculation of the 'multiresolution index of valley bottom flatness' (MRVBF) and the complementary 'multiresolution index of the ridge top flatness' (MRRTF). </p><p></p><p>References:</p><p>- Gallant, J.C., Dowling, T.I. (2003):   'A multiresolution index of valley bottom flatness for mapping depositional areas',   Water Resources Research, 39/12:1347-1359</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="MRVBF", name="MRVBF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="MRRTF", name="MRRTF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Initial Threshold for Slope", name="T_SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 16.000000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for Elevation Percentile (Lowness)", name="T_PCTL_V", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.400000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for Elevation Percentile (Upness)", name="T_PCTL_R", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.350000
		params += [param]
		param = arcpy.Parameter(displayName="Shape Parameter for Slope", name="P_SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 4.000000
		params += [param]
		param = arcpy.Parameter(displayName="Shape Parameter for Elevation Percentile", name="P_PCTL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Update Views", name="UPDATE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Classify", name="CLASSIFY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Resolution (Percentage)", name="MAX_RES", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '8')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MRVBF', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MRRTF', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('T_SLOPE', parameters[3].valueAsText)
		Tool.Set_Option('T_PCTL_V', parameters[4].valueAsText)
		Tool.Set_Option('T_PCTL_R', parameters[5].valueAsText)
		Tool.Set_Option('P_SLOPE', parameters[6].valueAsText)
		Tool.Set_Option('P_PCTL', parameters[7].valueAsText)
		Tool.Set_Option('UPDATE', parameters[8].valueAsText)
		Tool.Set_Option('CLASSIFY', parameters[9].valueAsText)
		Tool.Set_Option('MAX_RES', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Downslope Distance Gradient"
		self.description = "<p>Calculation of a new topographic index to quantify downslope controls on local drainage. </p><p></p><p>References:</p><p>- Hjerdt, K.N., McDonnell, J.J., Seibert, J. Rodhe, A. (2004):   'A new topographic index to quantify downslope controls on local drainage',   Water Resources Research, 40</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Gradient", name="GRADIENT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Gradient Difference", name="DIFFERENCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["distance", "gradient (tangens)", "gradient (degree)"]
		param.value = "gradient (degree)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '9')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('GRADIENT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIFFERENCE', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('DISTANCE', parameters[3].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Mass Balance Index"
		self.description = "<p></p><p>References:</p><p></p><p>Friedrich, K. (1996): Digitale Reliefgliederungsverfahren zur Ableitung bodenkundlich relevanter Flaecheneinheiten. Frankfurter Geowissenschaftliche Arbeiten D 21, Frankfurt/M., <a href=\"http://user.uni-frankfurt.de/~relief/fga21/\">online</a>.</p><p></p><p>Friedrich, K. (1998): Multivariate distance methods for geomorphographic relief classification. in Heinecke, H., Eckelmann, W., Thomasson, A., Jones, J., Montanarella, L., Buckley, B. (eds.): Land Inforamtion Systems - Developments for planning the sustainable use of land resources. European Soil Bureau - Research Report 4, EUR 17729 EN, Office for oficial publications of the European Communities, Ispra, pp. 259-266, <a href=\"http://eusoils.jrc.it/ESDB_Archive/eusoils_docs/esb_rr/n04_land_information_systems/contents.html\">online</a>.</p><p></p><p>Moeller, M., Volk, M., Friedrich, K., Lymburner, L. (2008): Placing soil-genesis and transport processes into a landscape context: A multiscale terrain-analysis approach. Journal of Plant Nutrition and Soil Science, 171, pp. 419-430, DOI: 10.1002/jpln.200625039</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Vertical Distance to Channel Network", name="HREL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mass Balance Index", name="MBI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="T Slope", name="TSLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="T Curvature", name="TCURVE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		param = arcpy.Parameter(displayName="T Vertical Distance to Channel Network", name="THREL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '10')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('HREL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MBI', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('TSLOPE', parameters[3].valueAsText)
		Tool.Set_Option('TCURVE', parameters[4].valueAsText)
		Tool.Set_Option('THREL', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Effective Air Flow Heights"
		self.description = "<p></p><p>References:</p><p>- Boehner, J., Antonic, O. (2009): 'Land-surface parameters specific to topo-climatology'. in: Hengl, T., Reuter, H. (Eds.): 'Geomorphometry - Concepts, Software, Applications'. Developments in Soil Science, Volume 33, p.195-226, Elsevier.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Direction", name="DIR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wind Direction Units", name="DIR_UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Wind Speed", name="LEN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scaling", name="LEN_SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Effective Air Flow Heights", name="AFH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance [km]", name="MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Constant Wind Direction", name="DIR_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 135.000000
		params += [param]
		param = arcpy.Parameter(displayName="Old Version", name="OLDVER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Acceleration", name="ACCEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.500000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Averaging", name="PYRAMIDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Windward Factor", name="LEE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Luv Factor", name="LUV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '11')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('DIR_UNITS', parameters[2].valueAsText)
		Tool.Set_Input ('LEN', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LEN_SCALE', parameters[4].valueAsText)
		Tool.Set_Output('AFH', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('MAXDIST', parameters[6].valueAsText)
		Tool.Set_Option('DIR_CONST', parameters[7].valueAsText)
		Tool.Set_Option('OLDVER', parameters[8].valueAsText)
		Tool.Set_Option('ACCEL', parameters[9].valueAsText)
		Tool.Set_Option('PYRAMIDS', parameters[10].valueAsText)
		Tool.Set_Option('LEE', parameters[11].valueAsText)
		Tool.Set_Option('LUV', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Diurnal Anisotropic Heating"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Diurnal Anisotropic Heating", name="DAH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Alpha Max (Degree)", name="ALPHA_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 202.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '12')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DAH', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('ALPHA_MAX', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Land Surface Temperature"
		self.description = "<p>References:</p><p>Bohner, J., Antonic, O. (2008): 'Land-suface parameters specific to topo-climatology'. in: Hengl, T., Reuter, H. (Eds.): 'Geomorphometry - Concepts, Software, Applications', in press</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation [m]", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Short Wave Radiation [kW/m2]", name="SWR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Leaf Area Index", name="LAI", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Land Surface Temperature [Deg.Celsius]", name="LST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Elevation at Reference Station [m]", name="Z_REFERENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Temperature at Reference Station [Deg.Celsius]", name="T_REFERENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Temperature Gradient [Deg.Celsius/km]", name="T_GRADIENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.500000
		params += [param]
		param = arcpy.Parameter(displayName="C Factor", name="C_FACTOR", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '13')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SWR', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('LAI', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LST', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('Z_REFERENCE', parameters[4].valueAsText)
		Tool.Set_Option('T_REFERENCE', parameters[5].valueAsText)
		Tool.Set_Option('T_GRADIENT', parameters[6].valueAsText)
		Tool.Set_Option('C_FACTOR', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Relative Heights and Slope Positions"
		self.description = "<p>The module allows one to calculate several terrain indices from a digital elevation model.</p><p></p><p>General information on the computational concept can be found in:</p><p>- Boehner, J. and Selige, T. (2006): Spatial prediction of soil attributes using terrain analysis and climate regionalisation. In: Boehner, J., McCloy, K.R., Strobl, J. [Ed.]: SAGA - Analysis and Modelling Applications, Goettinger Geographische Abhandlungen, Goettingen: 13-28. (<a target=\"_blank\" href=\"http://downloads.sourceforge.net/saga-gis/gga115_02.pdf\">pdf</a>)</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope Height", name="HO", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Valley Depth", name="HU", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Normalized Height", name="NH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standardized Height", name="SH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mid-Slope Positon", name="MS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="w", name="W", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="t", name="T", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="e", name="E", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '14')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('HO', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('HU', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('NH', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('SH', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('MS', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('W', parameters[6].valueAsText)
		Tool.Set_Option('T', parameters[7].valueAsText)
		Tool.Set_Option('E', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Wind Effect (Windward / Leeward Index)"
		self.description = "<p>The 'Wind Effect' is a dimensionless index. Values below 1 indicate wind shadowed areas whereas values above 1 indicate areas exposed to wind, all with regard to the specified wind direction. Wind direction, i.e. the direction into which the wind blows, might be either constant or variying in space, if a wind direction grid is supplied.</p><p></p><p>References:</p><p><ul><ul><li> Boehner, J., Antonic, O. (2009): Land-surface parameters specific to topo-climatology. in: Hengl, T., Reuter, H. (Eds.): 'Geomorphometry - Concepts, Software, Applications'. Developments in Soil Science, Volume 33, p.195-226, Elsevier.</li><li> Gerlitz, L., Conrad, O., Böhner, J. (2015): Large scale atmospheric forcing and topographic modification of precipitation rates over High Asia – a neural network based approach. Earth System Dynamics, 6, 1-21. doi:10.5194/esd-6-1-2015.</li></ul></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Direction", name="DIR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wind Direction Units", name="DIR_UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Wind Speed", name="LEN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scaling", name="LEN_SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Wind Effect", name="EFFECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Effective Air Flow Heights", name="AFH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance [km]", name="MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Constant Wind Direction", name="DIR_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 135.000000
		params += [param]
		param = arcpy.Parameter(displayName="Old Version", name="OLDVER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Acceleration", name="ACCEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.500000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Averaging", name="PYRAMIDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '15')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('DIR_UNITS', parameters[2].valueAsText)
		Tool.Set_Input ('LEN', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LEN_SCALE', parameters[4].valueAsText)
		Tool.Set_Output('EFFECT', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('AFH', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('MAXDIST', parameters[7].valueAsText)
		Tool.Set_Option('DIR_CONST', parameters[8].valueAsText)
		Tool.Set_Option('OLDVER', parameters[9].valueAsText)
		Tool.Set_Option('ACCEL', parameters[10].valueAsText)
		Tool.Set_Option('PYRAMIDS', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Topographic Position Index (TPI)"
		self.description = "<p>Topographic Position Index (TPI) calculation as proposed by Guisan et al. (1999). This is literally the same as the difference to the mean calculation (residual analysis) proposed by Wilson & Gallant (2000).</p><p>The bandwidth parameter for distance weighting is given as percentage of the (outer) radius.</p><p></p><p>References:</p><p>- Guisan, A., Weiss, S.B., Weiss, A.D. (1999): GLM versus CCA spatial modeling of plant species distribution. Plant Ecology 143: 107-122.</p><p>- Weiss, A.D. (2000): Topographic Position and Landforms Analysis. <a target=\"_blank\" href=\"http://www.jennessent.com/downloads/tpi-poster-tnc_18x22.pdf\">poster</a>.</p><p>- Wilson, J.P. & Gallant, J.C. (2000): Terrain Analysis - Principles and Applications.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Topographic Position Index", name="TPI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standardize", name="STANDARD", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Minimum)", name="RADIUS_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Maximum)", name="RADIUS_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
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
		param.value = 75.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '18')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TPI', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('STANDARD', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS_MIN', parameters[3].valueAsText)
		Tool.Set_Option('RADIUS_MAX', parameters[4].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[6].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[7].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "TPI Based Landform Classification"
		self.description = "<p>Topographic Position Index (TPI) calculation as proposed by Guisan et al. (1999). This is literally the same as the difference to the mean calculation (residual analysis) proposed by Wilson & Gallant (2000).</p><p>The bandwidth parameter for distance weighting is given as percentage of the (outer) radius.</p><p></p><p>References:</p><p>- Guisan, A., Weiss, S.B., Weiss, A.D. (1999): GLM versus CCA spatial modeling of plant species distribution. Plant Ecology 143: 107-122.</p><p>- Weiss, A.D. (2000): Topographic Position and Landforms Analysis. <a target=\"_blank\" href=\"http://www.jennessent.com/downloads/tpi-poster-tnc_18x22.pdf\">poster</a>.</p><p>- Wilson, J.P. & Gallant, J.C. (2000): Terrain Analysis - Principles and Applications.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Landforms", name="LANDFORMS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Minimum)", name="RADIUS_A_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Maximum)", name="RADIUS_A_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Minimum)", name="RADIUS_B_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Maximum)", name="RADIUS_B_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
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
		param.value = 75.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '19')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LANDFORMS', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RADIUS_A_MIN', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS_A_MAX', parameters[3].valueAsText)
		Tool.Set_Option('RADIUS_B_MIN', parameters[4].valueAsText)
		Tool.Set_Option('RADIUS_B_MAX', parameters[5].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[6].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[7].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[8].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Terrain Surface Texture"
		self.description = "<p>Terrain surface texture as proposed by Iwahashi & Pike (2007) for subsequent terrain classification.</p><p></p><p>Reference:</p><p>Iwahashi, J. & Pike, R.J. (2007): Automated classifications of topography from DEMs by an unsupervised nested-means algorithm and a three-part geometric signature. Geomorphology, Vol. 86, pp. 409–440</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Texture", name="TEXTURE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["counting cells", "resampling"]
		param.value = "resampling"
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.700000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '20')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TEXTURE', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('EPSILON', parameters[2].valueAsText)
		Tool.Set_Option('SCALE', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[6].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[7].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Terrain Surface Convexity"
		self.description = "<p>Terrain surface convexity as proposed by Iwahashi & Pike (2007) for subsequent terrain classification.</p><p></p><p>Reference:</p><p>Iwahashi, J. & Pike, R.J. (2007): Automated classifications of topography from DEMs by an unsupervised nested-means algorithm and a three-part geometric signature. Geomorphology, Vol. 86, pp. 409–440</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Convexity", name="CONVEXITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Laplacian Filter Kernel", name="KERNEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["conventional four-neighbourhood", "conventional eight-neihbourhood", "eight-neihbourhood (distance based weighting)"]
		param.value = "conventional four-neighbourhood"
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["convexity", "concavity"]
		param.value = "convexity"
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["counting cells", "resampling"]
		param.value = "resampling"
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.700000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '21')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONVEXITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('KERNEL', parameters[2].valueAsText)
		Tool.Set_Option('TYPE', parameters[3].valueAsText)
		Tool.Set_Option('EPSILON', parameters[4].valueAsText)
		Tool.Set_Option('SCALE', parameters[5].valueAsText)
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[7].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[9].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "Terrain Surface Classification (Iwahashi and Pike)"
		self.description = "<p>Terrain surface classification as proposed by Iwahashi & Pike (2007).</p><p></p><p>Reference:</p><p>Iwahashi, J. & Pike, R.J. (2007): Automated classifications of topography from DEMs by an unsupervised nested-means algorithm and a three-part geometric signature. Geomorphology, Vol. 86, pp. 409–440</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Convexity", name="CONVEXITY", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Recalculate", name="CONV_RECALC", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Texture", name="TEXTURE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Recalculate", name="TEXT_RECALC", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Landforms", name="LANDFORMS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["8", "12", "16"]
		param.value = "16"
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="CONV_SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Laplacian Filter Kernel", name="CONV_KERNEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["four-neighbourhood", "eight-neihbourhood", "eight-neihbourhood (distance based weighting)"]
		param.value = "four-neighbourhood"
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="CONV_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["convexity", "concavity"]
		param.value = "convexity"
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="CONV_EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="TEXT_SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="TEXT_EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '22')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SLOPE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('CONVEXITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CONV_RECALC', parameters[3].valueAsText)
		Tool.Set_Input ('TEXTURE', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('TEXT_RECALC', parameters[5].valueAsText)
		Tool.Set_Output('LANDFORMS', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[7].valueAsText)
		Tool.Set_Option('CONV_SCALE', parameters[8].valueAsText)
		Tool.Set_Option('CONV_KERNEL', parameters[9].valueAsText)
		Tool.Set_Option('CONV_TYPE', parameters[10].valueAsText)
		Tool.Set_Option('CONV_EPSILON', parameters[11].valueAsText)
		Tool.Set_Option('TEXT_SCALE', parameters[12].valueAsText)
		Tool.Set_Option('TEXT_EPSILON', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "Morphometric Features"
		self.description = "<p>Uses a multi-scale approach by fitting quadratic parameters to any size window (via least squares) to derive slope, aspect and curvatures (optional output) for subsequent classification of morphometric features (peaks, ridges, passes, channels, pits and planes). This is the method as proposed and implemented by Jo Wood (1996) in LandSerf and GRASS GIS (r.param.scale). </p><p></p><p>Optional output is described in the following. Generalised elevation is the smoothed input DEM. Slope is the magnitude of maximum gradient. It is given for steepest slope angle and measured in degrees. Aspect is the direction of maximum gradient. Profile curvature is the curvature intersecting with the plane defined by the Z axis and maximum gradient direction. Positive values describe convex profile curvature, negative values concave profile. Plan curvature is the horizontal curvature, intersecting with the XY plane. Longitudinal curvature is the profile curvature intersecting with the plane defined by the surface normal and maximum gradient direction. Cross-sectional curvature is the tangential curvature intersecting with the plane defined by the surface normal and a tangent to the contour - perpendicular to maximum gradient direction. Minimum curvature is measured in direction perpendicular to the direction of of maximum curvature. The maximum curvature is measured in any direction. </p><p></p><p>References:</p><p></p><p>Wood, J. (1996): The Geomorphological characterisation of Digital Elevation Models. Diss., Department of Geography, University of Leicester, U.K. <a target=\"_blank\" href=\"http://www.soi.city.ac.uk/~jwo/phd/\">online</a>.</p><p></p><p>Wood, J. (2009): Geomorphometry in LandSerf. In: Hengl, T. and Reuter, H.I. [Eds.]: Geomorphometry: Concepts, Software, Applications. Developments in Soil Science, Elsevier, Vol.33, 333-349.</p><p></p><p><a target=\"_blank\" href=\"http://www.landserf.org/\">LandSerf Homepage</a>.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Morphometric Features", name="FEATURES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Generalized Surface", name="ELEVATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Curvature", name="PROFC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Plan Curvature", name="PLANC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Longitudinal Curvature", name="LONGC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Sectional Curvature", name="CROSC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Curvature", name="MAXIC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Curvature", name="MINIC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scale Radius (Cells)", name="SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Slope Tolerance", name="TOL_SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Curvature Tolerance", name="TOL_CURVE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000100
		params += [param]
		param = arcpy.Parameter(displayName="Distance Weighting Exponent", name="EXPONENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Scaling", name="ZSCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Constrain", name="CONSTRAIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '23')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('FEATURES', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ELEVATION', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('ASPECT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('PROFC', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('PLANC', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('LONGC', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('CROSC', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('MAXIC', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('MINIC', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('SIZE', parameters[11].valueAsText)
		Tool.Set_Option('TOL_SLOPE', parameters[12].valueAsText)
		Tool.Set_Option('TOL_CURVE', parameters[13].valueAsText)
		Tool.Set_Option('EXPONENT', parameters[14].valueAsText)
		Tool.Set_Option('ZSCALE', parameters[15].valueAsText)
		Tool.Set_Option('CONSTRAIN', parameters[16].valueAsText)
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Valley and Ridge Detection (Top Hat Approach)"
		self.description = "<p>Calculating fuzzy valley and ridge class memberships using the Top Hat approach. Based on the AML script 'tophat' by Jochen Schmidt, Landcare Research. </p><p></p><p>References:</p><p>Rodriguez, F., Maire, E., Courjault-Rad'e, P., Darrozes, J. (2002): The Black Top Hat function applied to a DEM: a tool to estimate recent incision in a mountainous watershed. (Estib`ere Watershed, Central Pyrenees). Geophysical Research Letters, 29(6), 9-1 - 9-4.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Valley Depth", name="VALLEY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hill Height", name="HILL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Valley Index", name="VALLEY_IDX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hill Index", name="HILL_IDX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hillslope Index", name="SLOPE_IDX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Valley Radius", name="RADIUS_VALLEY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Hill Radius", name="RADIUS_HILL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Index", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["default", "alternative"]
		param.value = "default"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '24')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VALLEY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('HILL', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('VALLEY_IDX', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('HILL_IDX', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('SLOPE_IDX', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('RADIUS_VALLEY', parameters[6].valueAsText)
		Tool.Set_Option('RADIUS_HILL', parameters[7].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[8].valueAsText)
		Tool.Set_Option('METHOD', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Fuzzy Landform Element Classification"
		self.description = "<p>Algorithm for derivation of form elements according to slope, maximum curvature, minimum curvature, profile curvature, tangential curvature, based on a linear semantic import model for slope and curvature and a fuzzy classification Based on the AML script 'felementf' by Jochen Schmidt, Landcare Research. </p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Minimum Curvature", name="MINCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Curvature", name="MAXCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Curvature", name="PCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tangential Curvature", name="TCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Plain", name="PLAIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Pit", name="PIT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Peak", name="PEAK", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Ridge", name="RIDGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel", name="CHANNEL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Saddle", name="SADDLE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Back Slope", name="BSLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Foot Slope", name="FSLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shoulder Slope", name="SSLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hollow", name="HOLLOW", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Foot Hollow", name="FHOLLOW", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shoulder Hollow", name="SHOLLOW", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Spur", name="SPUR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Foot Spur", name="FSPUR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shoulder Spur", name="SSPUR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Landform", name="FORM", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Membership", name="MEM", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Entropy", name="ENTROPY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Confusion Index", name="CI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope Grid Units", name="SLOPETODEG", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["degree", "radians"]
		param.value = "degree"
		params += [param]
		param = arcpy.Parameter(displayName="Slope Thresholds [Degree] (Minimum)", name="T_SLOPE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Thresholds [Degree] (Maximum)", name="T_SLOPE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="Curvature Thresholds [1 / m] (Minimum)", name="T_CURVE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000002
		params += [param]
		param = arcpy.Parameter(displayName="Curvature Thresholds [1 / m] (Maximum)", name="T_CURVE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000050
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '25')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MINCURV', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('MAXCURV', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('PCURV', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('TCURV', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('PLAIN', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('PIT', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('PEAK', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('RIDGE', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('CHANNEL', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('SADDLE', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('BSLOPE', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('FSLOPE', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('SSLOPE', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('HOLLOW', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('FHOLLOW', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('SHOLLOW', parameters[16].valueAsText, 'grid')
		Tool.Set_Output('SPUR', parameters[17].valueAsText, 'grid')
		Tool.Set_Output('FSPUR', parameters[18].valueAsText, 'grid')
		Tool.Set_Output('SSPUR', parameters[19].valueAsText, 'grid')
		Tool.Set_Output('FORM', parameters[20].valueAsText, 'grid')
		Tool.Set_Output('MEM', parameters[21].valueAsText, 'grid')
		Tool.Set_Output('ENTROPY', parameters[22].valueAsText, 'grid')
		Tool.Set_Output('CI', parameters[23].valueAsText, 'grid')
		Tool.Set_Option('SLOPETODEG', parameters[24].valueAsText)
		Tool.Set_Option('T_SLOPE_MIN', parameters[25].valueAsText)
		Tool.Set_Option('T_SLOPE_MAX', parameters[26].valueAsText)
		Tool.Set_Option('T_CURVE_MIN', parameters[27].valueAsText)
		Tool.Set_Option('T_CURVE_MAX', parameters[28].valueAsText)
		Tool.Run()
		return


class tool_26(object):
	def __init__(self):
		self.label = "Upslope and Downslope Curvature"
		self.description = "<p>Calculates the local curvature of a cell as sum of the gradients to its neighbour cells. Upslope curvature is the distance weighted average local curvature in a cell's upslope contributing area based on multiple flow direction after Freeman 1994. </p><p>References:</p><p>- Freeman, G.T. (1991): Calculating catchment area with divergent flow based on a regular grid.   Computers and Geosciences, 17:413-22</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Local Curvature", name="C_LOCAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Curvature", name="C_UP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Local Upslope Curvature", name="C_UP_LOCAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Downslope Curvature", name="C_DOWN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Local Downslope Curvature", name="C_DOWN_LOCAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Weighting", name="WEIGHTING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '26')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('C_LOCAL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('C_UP', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('C_UP_LOCAL', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('C_DOWN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('C_DOWN_LOCAL', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('WEIGHTING', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_27(object):
	def __init__(self):
		self.label = "Wind Exposition Index"
		self.description = "<p>This tool calculates the average 'Wind Effect Index' for all directions using an angular step. Like the 'Wind Effect Index' it is a dimensionless index. Values below 1 indicate wind shadowed areas whereas values above 1 indicate areas exposed to wind.</p><p></p><p>References:</p><p><ul><li> Boehner, J., Antonic, O. (2009): Land-surface parameters specific to topo-climatology. in: Hengl, T., Reuter, H. (Eds.): 'Geomorphometry - Concepts, Software, Applications'. Developments in Soil Science, Volume 33, p.195-226, Elsevier.</li><li> Gerlitz, L., Conrad, O., Böhner, J. (2015): Large scale atmospheric forcing and topographic modification of precipitation rates over High Asia – a neural network based approach. Earth System Dynamics, 6, 1-21. doi:10.5194/esd-6-1-2015.</li></ul></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Exposition", name="EXPOSITION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance [km]", name="MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Angular Step Size (Degree)", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="Old Version", name="OLDVER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Acceleration", name="ACCEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.500000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Averaging", name="PYRAMIDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '27')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('EXPOSITION', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MAXDIST', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('OLDVER', parameters[4].valueAsText)
		Tool.Set_Option('ACCEL', parameters[5].valueAsText)
		Tool.Set_Option('PYRAMIDS', parameters[6].valueAsText)
		Tool.Run()
		return
