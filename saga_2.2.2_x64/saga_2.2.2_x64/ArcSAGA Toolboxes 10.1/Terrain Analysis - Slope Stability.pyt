import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Slope Stability"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5]

class tool_0(object):
	def __init__(self):
		self.label = "SAFETYFACTOR"
		self.description = "<p>This module computes a slope stability (expressed as a factor-of-safety) raster according to the traditional infinite slope model theory (see cf Selby, 1993) The resulting raster represents the ratio of resisting forces/driving forces (fs) on a potential shear plane with fs lesser 1 unstable, fs greater 1 stable. Except for a slope raster (in radians), all input variables can be specified either globally or distributed (through grids). The module creates a continuous fs raster (values above 10 are truncated), and a binary stability grid with nodata = stable, 1 = unstable (optional).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope grid (rad)", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Min thickness grid (m) ", name="Bmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max thickness grid (m) ", name="Bmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min saturation grid (-) ", name="Cmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max saturation grid (-) ", name="Cmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min friction grid (degree) ", name="Dmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max friction grid (degree) ", name="Dmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min density grid (g/cm3)", name="Emin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max density grid (g/cm3)", name="Emax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min cohesion grid (MPa) ", name="Fmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max cohesion grid (MPa) ", name="Fmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min global thickness (m)", name="fBmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Max global thickness (m)", name="fBmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Min global saturation (-)", name="fCmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Max global saturation (-)", name="fCmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Min global friction (degree)", name="fDmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 33.000000
		params += [param]
		param = arcpy.Parameter(displayName="Max global friction (degree)", name="fDmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 33.000000
		params += [param]
		param = arcpy.Parameter(displayName="Min global density (g/cm3)", name="fEmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.600000
		params += [param]
		param = arcpy.Parameter(displayName="Max global density (g/cm3)", name="fEmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.600000
		params += [param]
		param = arcpy.Parameter(displayName="Min global cohesion (MPa)", name="fFmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Max global cohesion (MPa)", name="fFmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Parameter sampling runs", name="fI", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="FS values", name="G", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="FS classes", name="H", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_slope_stability', '0')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('Bmin', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('Bmax', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('Cmin', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('Cmax', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('Dmin', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('Dmax', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('Emin', parameters[7].valueAsText, 'grid')
		Tool.Set_Input ('Emax', parameters[8].valueAsText, 'grid')
		Tool.Set_Input ('Fmin', parameters[9].valueAsText, 'grid')
		Tool.Set_Input ('Fmax', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('fBmin', parameters[11].valueAsText)
		Tool.Set_Option('fBmax', parameters[12].valueAsText)
		Tool.Set_Option('fCmin', parameters[13].valueAsText)
		Tool.Set_Option('fCmax', parameters[14].valueAsText)
		Tool.Set_Option('fDmin', parameters[15].valueAsText)
		Tool.Set_Option('fDmax', parameters[16].valueAsText)
		Tool.Set_Option('fEmin', parameters[17].valueAsText)
		Tool.Set_Option('fEmax', parameters[18].valueAsText)
		Tool.Set_Option('fFmin', parameters[19].valueAsText)
		Tool.Set_Option('fFmax', parameters[20].valueAsText)
		Tool.Set_Option('fI', parameters[21].valueAsText)
		Tool.Set_Output('G', parameters[22].valueAsText, 'grid')
		Tool.Set_Output('H', parameters[23].valueAsText, 'grid')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "TOBIA"
		self.description = "<p></p><p>This module computes both a continuous and a categorical TOBIA (Topography Bedding Intersection Angle) Index according to Meentemeyer & Moody (2000) For computation, a slope and a aspect raster (both in radians) determining slope face orientations are required. The categorical TOBIA classifies the alignement of a geological structure to Topography into seven classes:</p><p>0) Underdip slope</p><p>1) Dip slope</p><p>2) Overdip slope</p><p>3) Steepened escarpmemt</p><p>4) Normal escarpment</p><p>5) Subdued escarpment</p><p>6) Orthoclinal slope</p><p>The continuous TOBIA index ranges from -1 to 1 (parallel orientation)</p><p>The structure TOBIA should be calculated with can be set either distributed (through dip direction and dip grids, in degrees!), or globally using integers (dip and dip direction, in degrees!). The module creates a TOBIA class integer grid, and (optionally) a continuous TOBIA index grid.</p><p></p><p>Reference: <a href=\"http://www.sciencedirect.com/science/article/pii/S009830040000011X\">Meentemeyer R. K., Moody A. (2000). Automated mapping of conformity between topographic and geological surfaces. Computers & Geosciences, 26, 815 - 829</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope grid (rad)", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Aspect grid (rad)", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dip grid (degrees) ", name="C", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dip direction grid (degrees) ", name="D", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Global structure dip (degrees)", name="fB", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global structure dip direction (degrees)", name="fC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params += [param]
		param = arcpy.Parameter(displayName="TOBIA classes", name="E", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="TOBIA index", name="F", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_slope_stability', '1')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('C', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('D', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('fB', parameters[4].valueAsText)
		Tool.Set_Option('fC', parameters[5].valueAsText)
		Tool.Set_Output('E', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('F', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "SHALSTAB"
		self.description = "<p></p><p>This module is a realization of the SHALSTAB (Shallow Slope Stability) model from Montgomery & Dietrich (1994). The model computes grid cell critical shallow groundwater recharge values (CR in mm/day) as a measure for relative shallow slope stability, utilizing a simple model that combines a steady-state hydrologic model (a topographic wetness index) to predict groundwater pressures with an infinite slope stability model. For computation, a slope (in radians) and a catchment area (in m2) grid are required. Additionally, information on material density (g/cm3), material friction angle (&deg;), material hydraulic conductivity (m/hr), bulk cohesion (MPa) and depth to potential shear plane (m) are required that can be specified either globally or through grids. The module produces a continuous CR (mm/day) raster with unconditionally stable cells blanked, and unconditionally unstable cells as CR = 0. Optionally, a classified CR grid can be calculated representing seven stability classes.</p><p></p><p>Reference: <a href=\"http://www.agu.org/pubs/crossref/1994/93WR02979.shtml\">Montgomery D. R., Dietrich, W. E. (1994) A physically based model for the topographic control on shallow landsliding. Water Resources Research, 30, 1153-1171.</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope grid (rad)", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment area grid (m2)", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min Density grid (g/cm3)", name="Cmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max Density grid (g/cm3)", name="Cmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min Hydraulic conductivity grid (m/hr) ", name="Dmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max Hydraulic conductivity grid (m/hr) ", name="Dmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min Thickness grid (m)", name="Emin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max Thickness grid (m)", name="Emax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min Friction angle grid (degree) ", name="Fmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max Friction angle grid (degree) ", name="Fmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min Bulk cohesion grid (MPa) ", name="Jmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max Bulk cohesion grid (MPa) ", name="Jmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Global minimum density (g/cm3)", name="fCmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.600000
		params += [param]
		param = arcpy.Parameter(displayName="Global maximum density (g/cm3)", name="fCmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.600000
		params += [param]
		param = arcpy.Parameter(displayName="Global minimum conductivity (m/hr)", name="fDmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.700000
		params += [param]
		param = arcpy.Parameter(displayName="Global maximum conductivity (m/hr)", name="fDmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.700000
		params += [param]
		param = arcpy.Parameter(displayName="Global minimum thickness (m)", name="fEmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global maximum thickness (m)", name="fEmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global minimum friction angle (degree)", name="fFmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 33.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global maximum friction angle (degree)", name="fFmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 33.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global minimum bulk cohesion (MPa)", name="fJmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global maximum bulk cohesion (MPa)", name="fJmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Parameter sampling runs", name="fK", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="CR values", name="G", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="CR classes", name="H", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_slope_stability', '2')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('Cmin', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('Cmax', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('Dmin', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('Dmax', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('Emin', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('Emax', parameters[7].valueAsText, 'grid')
		Tool.Set_Input ('Fmin', parameters[8].valueAsText, 'grid')
		Tool.Set_Input ('Fmax', parameters[9].valueAsText, 'grid')
		Tool.Set_Input ('Jmin', parameters[10].valueAsText, 'grid')
		Tool.Set_Input ('Jmax', parameters[11].valueAsText, 'grid')
		Tool.Set_Option('fCmin', parameters[12].valueAsText)
		Tool.Set_Option('fCmax', parameters[13].valueAsText)
		Tool.Set_Option('fDmin', parameters[14].valueAsText)
		Tool.Set_Option('fDmax', parameters[15].valueAsText)
		Tool.Set_Option('fEmin', parameters[16].valueAsText)
		Tool.Set_Option('fEmax', parameters[17].valueAsText)
		Tool.Set_Option('fFmin', parameters[18].valueAsText)
		Tool.Set_Option('fFmax', parameters[19].valueAsText)
		Tool.Set_Option('fJmin', parameters[20].valueAsText)
		Tool.Set_Option('fJmax', parameters[21].valueAsText)
		Tool.Set_Option('fK', parameters[22].valueAsText)
		Tool.Set_Output('G', parameters[23].valueAsText, 'grid')
		Tool.Set_Output('H', parameters[24].valueAsText, 'grid')
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "WETNESS"
		self.description = "<p></p><p>This module calculates a topographic wetness index (TWI) following Montgomery & Dietrich (1994) that can be used to estimate the degree of saturation of unconsolidated, permeable materials above (more or less) impermeable bedrock. In contrast to the common TOPMODEL (Beven & Kirkby, 1979) - based TWI, this index differs in such that it considers hydraulic conductivity to be constant in a soil mantle overlying relatively impermeable bedrock. Also, it uses the sine of the slope rather than its tangens, which is more correct and significantly matters for steeper slopes that give raise to landslides. For computation, a slope (in radians) and a catchment area (in m2) grid are required. Additionally, information on groundwater recharge (m/hr), material hydraulic conductivity (m/hr), and depth to potential shear plane (m) are required that can be specified either globally or through grids. The module produces a continuous wetness index (-) where cells with WI values > 1 (overland flow) set to 1, and optionally creates a classified WI grid rendering three saturation classes:.</p><p>0): Low moisture (WI smaller 0.1)</p><p>1): Partially wet (0.1 smaller WI smaller 1)</p><p>2): Saturation zone (WI larger 1)</p><p></p><p>References:</p><p><a href=\"http://www.tandfonline.com/doi/abs/10.1080/02626667909491834\">Beven, K.J., Kirkby, M.J. (1979) A physically-based variable contributing area model of basin hydrology. Hydrology Science Bulletin, 24, 43-69.</a>.</p><p></p><p><a href=\"http://www.agu.org/pubs/crossref/1994/93WR02979.shtml\">Montgomery D. R., Dietrich, W. E. (1994) A physically based model for the topographic control on shallow landsliding. Water Resources Research, 30, 1153-1171.</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Min hydraulic conductivity grid (m/hr) ", name="Cmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max hydraulic conductivity grid (m/hr) ", name="Cmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min groundwater recharge grid (m/hr) ", name="Dmin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max groundwater recharge grid (m/hr) ", name="Dmax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min material depth grid (m)", name="Emin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max material depth grid (m)", name="Emax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min global material conductivity (m/hr)", name="fCmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.700000
		params += [param]
		param = arcpy.Parameter(displayName="Max global material conductivity (m/hr)", name="fCmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.700000
		params += [param]
		param = arcpy.Parameter(displayName="Min global groundwater recharge (m/hr)", name="fDmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.001000
		params += [param]
		param = arcpy.Parameter(displayName="Max global groundwater recharge (m/hr)", name="fDmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.001000
		params += [param]
		param = arcpy.Parameter(displayName="Min global material depth (m)", name="fEmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Max global material depth (m)", name="fEmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Parameter sampling runs", name="fH", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="WI values", name="F", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="WI classes", name="G", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Catchment Area Calculation", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Braunschweiger Reliefmodell", "Deterministic Infinity", "Multiple Flow Direction", "Multiple Triangular Flow Directon"]
		param.value = "Multiple Flow Direction"
		params += [param]
		param = arcpy.Parameter(displayName="Preprocessing", name="PREPROC", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_slope_stability', '3')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('Cmin', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('Cmax', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('Dmin', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('Dmax', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('Emin', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('Emax', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('fCmin', parameters[7].valueAsText)
		Tool.Set_Option('fCmax', parameters[8].valueAsText)
		Tool.Set_Option('fDmin', parameters[9].valueAsText)
		Tool.Set_Option('fDmax', parameters[10].valueAsText)
		Tool.Set_Option('fEmin', parameters[11].valueAsText)
		Tool.Set_Option('fEmax', parameters[12].valueAsText)
		Tool.Set_Option('fH', parameters[13].valueAsText)
		Tool.Set_Output('F', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('G', parameters[15].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[16].valueAsText)
		Tool.Set_Option('PREPROC', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "WEDGEFAIL"
		self.description = "<p></p><p>This module determines terrain elements where failure (slide- or topple movements) on geological discontinuies are kinematically possible through the spatial application of common frictional feasibility criteria (G&uuml;nther et al. 2012 and references therein). Both the orientation of slope elements specified through aspect- and dip grids (in radians) are required together with the orientation of one planar structure defined through global- or grid dip direction and dip data, or two planar structures defined by plunge direction and plunge information of their intersection line (in degrees). The shear strength of the discontinuities is specified using global or grid-based friction angle data. Optionally, a cone value can be set allowing for some variance in discontinuity dip orientations. The tool operates in slide (testing for plane and wedge sliding) or topple (testing for plane and wedge toppling) modes.</p><p></p><p>Reference:</p><p><a href=\"http://link.springer.com/article/10.1007/s11069-011-9771-2.\">G&uuml;nther A., Wienh&ouml;fer J., Konietzky H. (2012) Automated mapping of rock slope geometry, kinematics and stability with RSS-GIS. Natural Hazards, 61, 29-49.</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Dip/Plunge direction grid (degree) ", name="C", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dip/Plunge grid (degree) ", name="D", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min friction angle grid (degree) ", name="Emin", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max friction angle grid (degree) ", name="Emax", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Global dip/plunge direction (degree)", name="fC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global dip/plunge (degree)", name="fD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 35.000000
		params += [param]
		param = arcpy.Parameter(displayName="Min global friction angle (degree)", name="fEmin", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 35.000000
		params += [param]
		param = arcpy.Parameter(displayName="Max global friction angle (degree)", name="fEmax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 35.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cone radius (degree)", name="ff", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Failures", name="F", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Parameter sampling runs", name="fI", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Mode", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Slide", "Topple"]
		param.value = "Slide"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_slope_stability', '4')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('C', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('D', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('Emin', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('Emax', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('fC', parameters[5].valueAsText)
		Tool.Set_Option('fD', parameters[6].valueAsText)
		Tool.Set_Option('fEmin', parameters[7].valueAsText)
		Tool.Set_Option('fEmax', parameters[8].valueAsText)
		Tool.Set_Option('ff', parameters[9].valueAsText)
		Tool.Set_Output('F', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('fI', parameters[11].valueAsText)
		Tool.Set_Option('METHOD', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "ANGMAP"
		self.description = "<p></p><p>This module computes the acute angle raster between the topographic surface defined by slope and aspect rasters internally derived from input elevation raster, and a structural plane defined by diop direction- and dip grids. Optionally, the dip direction and dip of the cutting line linears between the two planes can be calculated</p><p>Reference: <a href=\"http://www.sciencedirect.com/science/article/pii/S0098300403000864\">G&uuml;nther, A. (2003). SLOPEMAP: programs for automated mapping of geometrical and kinematical properties of hard rock hill slopes. Computers & Geosciences, 29, 865 - 875</a>.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Dip grid (degrees) ", name="C", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dip direction grid (degrees) ", name="D", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Global structure dip (degrees)", name="fB", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Global structure dip direction (degrees)", name="fC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params += [param]
		param = arcpy.Parameter(displayName="Angle", name="E", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="CL dipdir", name="F", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="CL dip", name="G", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_slope_stability', '5')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('C', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('D', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('fB', parameters[3].valueAsText)
		Tool.Set_Option('fC', parameters[4].valueAsText)
		Tool.Set_Output('E', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('F', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('G', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return
