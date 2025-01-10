import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Spline Interpolation"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6]

class tool_0(object):
	def __init__(self):
		self.label = "Thin Plate Spline"
		self.description = "<p>Creates a 'Thin Plate Spline' function for each grid point based on all of the scattered data points that are within a given distance. The number of points can be limited to a maximum number of closest points. </p><p></p><p>References:</p><p>- Donato G., Belongie S. (2002): 'Approximation Methods for Thin Plate Spline Mappings and Principal Warps', In Heyden, A., Sparr, G., Nielsen, M., Johansen, P. (Eds.): 'Computer Vision - ECCV 2002: 7th European Conference on Computer Vision, Copenhagen, Denmark, May 28-31, 2002', Proceedings, Part III, Lecture Notes in Computer Science. Springer-Verlag Heidelberg; pp.21-31.</p><p></p><p>- Elonen, J. (2005): 'Thin Plate Spline editor - an example program in C++', <a target=\"_blank\" href=\"http://elonen.iki.fi/code/tpsdemo/index.html\">http://elonen.iki.fi/code/tpsdemo/index.html</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regularisation", name="REGULARISATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000100
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "local"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "maximum number of nearest points"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="SEARCH_POINTS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 16
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="SEARCH_POINTS_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="SEARCH_DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all directions", "quadrants"]
		param.value = "all directions"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_spline', '1')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('REGULARISATION', parameters[4].valueAsText)
		Tool.Set_Option('SEARCH_RANGE', parameters[5].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[6].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[7].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[8].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[9].valueAsText)
		Tool.Set_Option('SEARCH_DIRECTION', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Thin Plate Spline (TIN)"
		self.description = "<p>Creates a 'Thin Plate Spline' function for each triangle of a TIN and uses it for subsequent gridding. The TIN is internally created from the scattered data points input. The 'Neighbourhood' option determines the number of points used for the spline generation. 'Immediate neighbourhood' includes the points of the triangle as well as the immediate neighbour points. 'Level 1' adds the neighbours of the immediate neighbourhood and 'level 2' adds the neighbours of 'level 1' neighbours too. A higher neighbourhood degree reduces sharp breaks but also increases the computation time. </p><p></p><p>References:</p><p>- Donato G., Belongie S. (2002): 'Approximation Methods for Thin Plate Spline Mappings and Principal Warps', In Heyden, A., Sparr, G., Nielsen, M., Johansen, P. (Eds.): 'Computer Vision - ECCV 2002: 7th European Conference on Computer Vision, Copenhagen, Denmark, May 28-31, 2002', Proceedings, Part III, Lecture Notes in Computer Science. Springer-Verlag Heidelberg; pp.21-31.</p><p></p><p>- Elonen, J. (2005): 'Thin Plate Spline editor - an example program in C++', <a target=\"_blank\" href=\"http://elonen.iki.fi/code/tpsdemo/index.html\">http://elonen.iki.fi/code/tpsdemo/index.html</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Regularisation", name="REGULARISATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000100
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="LEVEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["immediate", "level 1", "level 2"]
		param.value = "level 1"
		params += [param]
		param = arcpy.Parameter(displayName="Add Frame", name="FRAME", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_spline', '2')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('REGULARISATION', parameters[4].valueAsText)
		Tool.Set_Option('LEVEL', parameters[5].valueAsText)
		Tool.Set_Option('FRAME', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "B-Spline Approximation"
		self.description = "<p>Calculates B-spline functions for chosen level of detail. This module serves as the basis for the 'Multilevel B-Spline Interpolation' and is not suited as is for spatial data interpolation from scattered data. </p><p></p><p>Reference:</p><p> - Lee, S., Wolberg, G., Shin, S.Y. (1997): 'Scattered Data Interpolation with Multilevel B-Splines', IEEE Transactions On Visualisation And Computer Graphics, Vol.3, No.3</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Resolution", name="LEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_spline', '3')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LEVEL', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Multilevel B-Spline Interpolation"
		self.description = "<p>Multilevel B-spline algorithm for spatial interpolation of scattered data as proposed by Lee, Wolberg and Shin (1997). The algorithm makes use of a coarse-to-fine hierarchy of control lattices to generate a sequence of bicubic B-spline functions, whose sum approaches the desired interpolation function. Large performance gains are realized by using B-spline refinement to reduce the sum of these functions into one equivalent B-spline function. </p><p></p><p>The 'Maximum Level' determines the maximum size of the final B-spline matrix and increases exponential with each level. Where level=10 requires about 1mb level=12 needs about 16mb and level=14 about 256mb(!) of additional memory. </p><p></p><p>Reference:</p><p> - Lee, S., Wolberg, G., Shin, S.Y. (1997): 'Scattered Data Interpolation with Multilevel B-Splines', IEEE Transactions On Visualisation And Computer Graphics, Vol.3, No.3</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["without B-spline refinement", "with B-spline refinement"]
		param.value = "with B-spline refinement"
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Error", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000100
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Level", name="LEVEL_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 11
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_spline', '4')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('EPSILON', parameters[5].valueAsText)
		Tool.Set_Option('LEVEL_MAX', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Multilevel B-Spline Interpolation (from Grid)"
		self.description = "<p>Multilevel B-spline algorithm for spatial interpolation of scattered data as proposed by Lee, Wolberg and Shin (1997). The algorithm makes use of a coarse-to-fine hierarchy of control lattices to generate a sequence of bicubic B-spline functions, whose sum approaches the desired interpolation function. Large performance gains are realized by using B-spline refinement to reduce the sum of these functions into one equivalent B-spline function. </p><p></p><p>The 'Maximum Level' determines the maximum size of the final B-spline matrix and increases exponential with each level. Where level=10 requires about 1mb level=12 needs about 16mb and level=14 about 256mb(!) of additional memory. </p><p></p><p>Reference:</p><p> - Lee, S., Wolberg, G., Shin, S.Y. (1997): 'Scattered Data Interpolation with Multilevel B-Splines', IEEE Transactions On Visualisation And Computer Graphics, Vol.3, No.3</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["without B-spline refinement", "with B-spline refinement"]
		param.value = "with B-spline refinement"
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Error", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000100
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Level", name="LEVEL_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 11
		params += [param]
		param = arcpy.Parameter(displayName="Update View", name="UPDATE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="DATATYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["same as input grid", "floating point"]
		param.value = "floating point"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_spline', '5')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('TARGET_USER_SIZE', parameters[1].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('EPSILON', parameters[4].valueAsText)
		Tool.Set_Option('LEVEL_MAX', parameters[5].valueAsText)
		Tool.Set_Option('UPDATE', parameters[6].valueAsText)
		Tool.Set_Option('DATATYPE', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Cubic Spline Approximation"
		self.description = "<p>This module approximates irregular scalar 2D data in specified points using C1-continuous bivariate cubic spline.</p><p>Minimal Number of Points:                minimal number of points locally involved                in spline calculation (normally = 3)</p><p></p><p>Maximal Number of Points:npmax:          maximal number of points locally involved                in spline calculation (required > 10,                recommended 20 < npmax < 60)</p><p>Tolerance:                relative tolerance multiple in fitting                spline coefficients: the higher this                value, the higher degree of the locally                fitted spline (recommended 80 < k < 200)</p><p></p><p>Points per square:                average number of points per square                (increase if the point distribution is strongly non-uniform                to get larger cells)</p><p></p><p>Author:         Pavel Sakov,                CSIRO Marine Research</p><p></p><p>Purpose:        2D data approximation with bivariate C1 cubic spline.                A set of library functions + standalone utility.</p><p></p><p>Description:    See J. Haber, F. Zeilfelder, O.Davydov and H.-P. Seidel,                Smooth approximation and rendering of large scattered data                sets, in 'Proceedings of IEEE Visualization 2001'                (Th.Ertl, K.Joy and A.Varshney, Eds.), pp.341-347, 571,                IEEE Computer Society, 2001.</p><p><a target=\"_blank\" href=\"http://www.uni-giessen.de/www-Numerische-Mathematik/davydov/VIS2001.ps.gz\">www.uni-giessen.de/www-Numerische-Mathematik/davydov/VIS2001.ps.gz</a></p><p><a target=\"_blank\" href=\"http://www.math.uni-mannheim.de/~lsmath4/paper/VIS2001.pdf.gz\">www.math.uni-mannheim.de/~lsmath4/paper/VIS2001.pdf.gz</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimal Number of Points", name="NPMIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Maximal Number of Points", name="NPMAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Points per Square", name="NPPC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="K", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 140
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_spline', '6')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('NPMIN', parameters[4].valueAsText)
		Tool.Set_Option('NPMAX', parameters[5].valueAsText)
		Tool.Set_Option('NPPC', parameters[6].valueAsText)
		Tool.Set_Option('K', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Multilevel B-Spline Interpolation for Categories"
		self.description = "<p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Categories", name="CATEGORIES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Propability", name="PROPABILITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_spline', '7')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('CATEGORIES', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('PROPABILITY', parameters[4].valueAsText, 'grid')
		Tool.Run()
		return
