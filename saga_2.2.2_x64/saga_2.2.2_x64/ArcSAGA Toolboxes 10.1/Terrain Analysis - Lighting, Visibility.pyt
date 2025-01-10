import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Lighting, Visibility"
		self.alias = ""
		self.tools = [tool_0, tool_2, tool_3, tool_4, tool_5, tool_6]

class tool_0(object):
	def __init__(self):
		self.label = "Analytical Hillshading"
		self.description = "<p>Analytical hillshading calculation.</p><p>Method 'Ambient Occlusion' is based on concepts of Tarini et al. (2006), but only the northern half-space is considered.</p><p></p><p>References:</p><p>Tarini, M. / Cignoni, P. / Montani, C. (2006): Ambient Occlusion and Edge Cueing to Enhance Real Time Molecular Visualization. IEEE Transactions on Visualization and Computer Graphics, Vol. 12, No. 5, pp. 1237-1244.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Analytical Hillshading", name="SHADE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shading Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Standard", "Standard (max. 90Degree)", "Combined Shading", "Ray Tracing", "Ambient Occlusion"]
		param.value = "Standard"
		params += [param]
		param = arcpy.Parameter(displayName="Azimuth [Degree]", name="AZIMUTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 315.000000
		params += [param]
		param = arcpy.Parameter(displayName="Height [Degree]", name="DECLINATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Exaggeration", name="EXAGGERATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 4.000000
		params += [param]
		param = arcpy.Parameter(displayName="Shadow", name="SHADOW", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["slim", "fat"]
		param.value = "fat"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Directions", name="NDIRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		param = arcpy.Parameter(displayName="Search Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SHADE', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('AZIMUTH', parameters[3].valueAsText)
		Tool.Set_Option('DECLINATION', parameters[4].valueAsText)
		Tool.Set_Option('EXAGGERATION', parameters[5].valueAsText)
		Tool.Set_Option('SHADOW', parameters[6].valueAsText)
		Tool.Set_Option('NDIRS', parameters[7].valueAsText)
		Tool.Set_Option('RADIUS', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Potential Incoming Solar Radiation"
		self.description = "<p>Calculation of potential incoming solar radiation (insolation).</p><p>Times of sunrise/sunset will only be calculated if time span is set to single day.</p><p></p><p>References:</p><p><ul><li>Boehner, J., Antonic, O. (2009): Land Surface Parameters Specific to Topo-Climatology. in Hengl, T. & Reuter, H.I. [Eds.]: Geomorphometry - Concepts, Software, Applications.</li><li>Oke, T.R. (1988): Boundary Layer Climates. London, Taylor & Francis.</li><li>Wilson, J.P., Gallant, J.C. [Eds.] (2000): Terrain Analysis - Principles and Applications. New York, John Wiley & Sons, Inc.</li><li>Joint Research Centre: <a target=\"_blank\" href=\"http://re.jrc.ec.europa.eu/pvgis/\">GIS solar radiation database for Europe</a> and  <a target=\"_blank\" href=\"http://re.jrc.ec.europa.eu/pvgis/solres/solmod3.htm\">Solar radiation and GIS</a>.</li><li>Hofierka, J., Suri, M. (2002): The solar radiation model for Open source GIS: implementation and applications. International GRASS users conference in Trento, Italy, September 2002. <a target=\"_blank\" href=\"http://skagit.meas.ncsu.edu/~jaroslav/trento/Hofierka_Jaroslav.pdf\">pdf</a>.</li></ul></p><p></p><p>*) Most options should do well, but TAPES-G based diffuse irradiance calculation ('Atmospheric Effects' methods 2 and 3) needs further revision!<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="GRD_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sky View Factor", name="GRD_SVF", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Water Vapour Pressure [mbar]", name="GRD_VAPOUR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="GRD_VAPOUR_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Linke Turbidity Coefficient", name="GRD_LINKE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="GRD_LINKE_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Direct Insolation", name="GRD_DIRECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Diffuse Insolation", name="GRD_DIFFUS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Insolation", name="GRD_TOTAL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direct to Diffuse Ratio", name="GRD_RATIO", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Duration of Insolation", name="GRD_DURATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sunrise", name="GRD_SUNRISE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sunset", name="GRD_SUNSET", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Solar Constant [W / m²]", name="SOLARCONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1367.000000
		params += [param]
		param = arcpy.Parameter(displayName="Local Sky View Factor", name="LOCALSVF", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["kWh / m2", "kJ / m2", "J / cm2"]
		param.value = "kWh / m2"
		params += [param]
		param = arcpy.Parameter(displayName="Shadow", name="SHADOW", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["slim", "fat", "none"]
		param.value = "fat"
		params += [param]
		param = arcpy.Parameter(displayName="Update", name="UPDATE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["do not update", "fit histogram stretch for each time step", "constant histogram stretch for all time steps"]
		param.value = "do not update"
		params += [param]
		param = arcpy.Parameter(displayName="Constant Histogram Stretch", name="UPDATE_STRETCH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Location", name="LOCATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["constant latitude", "calculate from grid system"]
		param.value = "constant latitude"
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LATITUDE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time Period", name="PERIOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["moment", "day", "range of days"]
		param.value = "day"
		params += [param]
		param = arcpy.Parameter(displayName="Moment [h]", name="MOMENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 12.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time Span [h] (Minimum)", name="HOUR_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time Span [h] (Maximum)", name="HOUR_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 24.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time Resolution [h]: Day", name="HOUR_STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Time Resolution [d]: Range of Days", name="DAYS_STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Day", name="DAY_A", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 15
		params += [param]
		param = arcpy.Parameter(displayName="Month", name="MON_A", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		param.value = "October"
		params += [param]
		param = arcpy.Parameter(displayName="Year", name="YEAR_A", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2015
		params += [param]
		param = arcpy.Parameter(displayName="Day", name="DAY_B", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 15
		params += [param]
		param = arcpy.Parameter(displayName="Month", name="MON_B", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		param.value = "October"
		params += [param]
		param = arcpy.Parameter(displayName="Year", name="YEAR_B", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2015
		params += [param]
		param = arcpy.Parameter(displayName="Atmospheric Effects", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Height of Atmosphere and Vapour Pressure", "Air Pressure, Water and Dust Content", "Lumped Atmospheric Transmittance", "Hofierka and Suri"]
		param.value = "Lumped Atmospheric Transmittance"
		params += [param]
		param = arcpy.Parameter(displayName="Height of Atmosphere [m]", name="ATMOSPHERE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 12000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Barometric Pressure [mbar]", name="PRESSURE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1013.000000
		params += [param]
		param = arcpy.Parameter(displayName="Water Content [cm]", name="WATER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.680000
		params += [param]
		param = arcpy.Parameter(displayName="Dust [ppm]", name="DUST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lumped Atmospheric Transmittance [Percent]", name="LUMPED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 70.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '2')
		Tool.Set_Input ('GRD_DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRD_SVF', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('GRD_VAPOUR', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('GRD_VAPOUR_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Input ('GRD_LINKE', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('GRD_LINKE_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Output('GRD_DIRECT', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('GRD_DIFFUS', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('GRD_TOTAL', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('GRD_RATIO', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('GRD_DURATION', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('GRD_SUNRISE', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('GRD_SUNSET', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('SOLARCONST', parameters[13].valueAsText)
		Tool.Set_Option('LOCALSVF', parameters[14].valueAsText)
		Tool.Set_Option('UNITS', parameters[15].valueAsText)
		Tool.Set_Option('SHADOW', parameters[16].valueAsText)
		Tool.Set_Option('UPDATE', parameters[17].valueAsText)
		Tool.Set_Option('UPDATE_STRETCH', parameters[18].valueAsText)
		Tool.Set_Option('LOCATION', parameters[19].valueAsText)
		Tool.Set_Option('LATITUDE', parameters[20].valueAsText)
		Tool.Set_Option('PERIOD', parameters[21].valueAsText)
		Tool.Set_Option('MOMENT', parameters[22].valueAsText)
		Tool.Set_Option('HOUR_RANGE_MIN', parameters[23].valueAsText)
		Tool.Set_Option('HOUR_RANGE_MAX', parameters[24].valueAsText)
		Tool.Set_Option('HOUR_STEP', parameters[25].valueAsText)
		Tool.Set_Option('DAYS_STEP', parameters[26].valueAsText)
		Tool.Set_Option('DAY_A', parameters[27].valueAsText)
		Tool.Set_Option('MON_A', parameters[28].valueAsText)
		Tool.Set_Option('YEAR_A', parameters[29].valueAsText)
		Tool.Set_Option('DAY_B', parameters[30].valueAsText)
		Tool.Set_Option('MON_B', parameters[31].valueAsText)
		Tool.Set_Option('YEAR_B', parameters[32].valueAsText)
		Tool.Set_Option('METHOD', parameters[33].valueAsText)
		Tool.Set_Option('ATMOSPHERE', parameters[34].valueAsText)
		Tool.Set_Option('PRESSURE', parameters[35].valueAsText)
		Tool.Set_Option('WATER', parameters[36].valueAsText)
		Tool.Set_Option('DUST', parameters[37].valueAsText)
		Tool.Set_Option('LUMPED', parameters[38].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Sky View Factor"
		self.description = "<p>Calculation of visible sky, sky view factor (SVF) and related parameters.</p><p></p><p>References:</p><p>Boehner, J., Antonic, O. (2009): 'Land-surface parameters specific to topo-climatology'. in: Hengl, T., Reuter, H. (Eds.): 'Geomorphometry - Concepts, Software, Applications'. Developments in Soil Science, Volume 33, p.195-226, Elsevier</p><p></p><p>Hantzschel, J., Goldberg, V., Bernhofer, C. (2005): 'GIS-based regionalisation of radiation, temperature and coupling measures in complex terrain for low mountain ranges'. Meteorological Applications, V.12:01, p.33-42, doi:10.1017/S1350482705001489</p><p></p><p>Oke, T.R. (2000): 'Boundary Layer Climates'. Taylor & Francis, New York. 435pp.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Visible Sky", name="VISIBLE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sky View Factor", name="SVF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sky View Factor (Simplified)", name="SIMPLE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Terrain View Factor", name="TERRAIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="View Distance", name="DISTANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["multi scale", "sectors"]
		param.value = "sectors"
		params += [param]
		param = arcpy.Parameter(displayName="Multi Scale Factor", name="DLEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Sectors", name="NDIRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '3')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VISIBLE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SVF', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SIMPLE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('TERRAIN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('DISTANCE', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Set_Option('DLEVEL', parameters[8].valueAsText)
		Tool.Set_Option('NDIRS', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Topographic Correction"
		self.description = "<p></p><p>References:</p><p>Civco, D. L. (1989): 'Topographic Normalization of Landsat Thematic Mapper Digital Imagery', Photogrammetric Engineering and Remote Sensing, 55(9), pp.1303-1309.</p><p></p><p>Law, K.H., Nichol, J. (2004): 'Topographic Correction for Differential Illumination Effects on Ikonos Satellite Imagery', ISPRS 2004 International Society for Photogrammetry and Remote Sensing, <a href=\"http://www.cartesia.org/geodoc/isprs2004/comm3/papers/347.pdf\">pdf</a>.</p><p></p><p>Phua, M.-H., Saito, H. (2003): 'Estimation of biomass of a mountainous tropical forest using Landsat TM data', Canadian Journal of Remote Sensing, 29(4), pp.429-440.</p><p></p><p>Riano, D., Chuvieco, E. Salas, J., Aguado, I. (2003): 'Assessment of Different Topographic Corrections in Landsat-TM Data for Mapping Vegetation Types', IEEE Transactions on Geoscience and Remote Sensing, 41(5), pp.1056-1061, <a href=\"http://www.geogra.uah.es/~emilio/pdf/Riano2003b.pdf\">pdf</a>.</p><p></p><p>Teillet, P.M., Guindon, B., Goodenough, D.G. (1982): 'On the slope-aspect correction of multispectral scanner data', Canadian Journal of Remote Sensing, 8(2), pp.1537-1540.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Original Image", name="ORIGINAL", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Corrected Image", name="CORRECTED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Azimuth", name="AZI", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 180.000000
		params += [param]
		param = arcpy.Parameter(displayName="Height", name="HGT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Cosine Correction (Teillet et al. 1982)", "Cosine Correction (Civco 1989)", "Minnaert Correction", "Minnaert Correction with Slope (Riano et al. 2003)", "Minnaert Correction with Slope (Law & Nichol 2004)", "C Correction", "Normalization (after Civco, modified by Law & Nichol)"]
		param.value = "Minnaert Correction with Slope (Law & Nichol 2004)"
		params += [param]
		param = arcpy.Parameter(displayName="Minnaert Correction", name="MINNAERT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Cells (C Correction Analysis)", name="MAXCELLS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1000
		params += [param]
		param = arcpy.Parameter(displayName="Value Range", name="MAXVALUE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 byte (0-255)", "2 byte (0-65535)"]
		param.value = "1 byte (0-255)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '4')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('ORIGINAL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CORRECTED', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('AZI', parameters[3].valueAsText)
		Tool.Set_Option('HGT', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Set_Option('MINNAERT', parameters[6].valueAsText)
		Tool.Set_Option('MAXCELLS', parameters[7].valueAsText)
		Tool.Set_Option('MAXVALUE', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Topographic Openness"
		self.description = "<p>Topographic openness expresses the dominance (positive) or enclosure (negative) of a landscape location. See Yokoyama et al. (2002) for a precise definition. Openness has been related to how wide a landscape can be viewed from any position. It has been proven to be a meaningful input for computer aided geomorphological mapping.</p><p></p><p>References:</p><p>Anders, N. S. / Seijmonsbergen, A. C. / Bouten, W. (2009): Multi-Scale and Object-Oriented Image Analysis of High-Res LiDAR Data for Geomorphological Mapping in Alpine Mountains. Proceedings of Geomorphometry 2009. <a target=\"_blank\" href=\"http://geomorphometry.org/system/files/anders2009geomorphometry.pdf\">online at geomorphometry.org</a>.</p><p></p><p>Prima, O.D.A / Echigo, A. / Yokoyama, R. / Yoshida, T. (2006): Supervised landform classification of Northeast Honshu from DEM-derived thematic maps. Geomorphology, vol.78, pp.373-386.</p><p></p><p>Yokoyama, R. / Shirasawa, M. / Pike, R.J. (2002): Visualizing topography by openness: A new application of image processing to digital elevation models. Photogrammetric Engineering and Remote Sensing, Vol.68, pp.251-266. <a target=\"_blank\" href=\"http://www.asprs.org/a/publications/pers/2002journal/march/2002_mar_257-265.pdf\">online at ASPRS</a>.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Positive Openness", name="POS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Negative Openness", name="NEG", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radial Limit", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["multi scale", "sectors"]
		param.value = "sectors"
		params += [param]
		param = arcpy.Parameter(displayName="Multi Scale Factor", name="DLEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Sectors", name="NDIRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '5')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('POS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('NEG', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('DLEVEL', parameters[5].valueAsText)
		Tool.Set_Option('NDIRS', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Visibility (points)"
		self.description = "<p>This module computes a visibility analysis using observer points from a point shapefile.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Visibility", name="VISIBILITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Height", name="FIELD_HEIGHT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Visibility", "Shade", "Distance", "Size"]
		param.value = "Shade"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '6')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VISIBILITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('POINTS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('FIELD_HEIGHT', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return
