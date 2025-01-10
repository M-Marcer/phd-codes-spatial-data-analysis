import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "PostgreSQL"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18, tool_20, tool_21]

class tool_0(object):
	def __init__(self):
		self.label = "List PostgreSQL Connections"
		self.description = "<p>Lists all PostgreSQL sources.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Connections", name="CONNECTIONS", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '0')
		Tool.Set_Output('CONNECTIONS', parameters[0].valueAsText, 'table')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Connect to PostgreSQL"
		self.description = "<p>Connect to PostgreSQL data source.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "localhost"
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "geo_test"
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "postgres"
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "postgres"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '1')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Disconnect from PostgreSQL"
		self.description = "<p>Disconnect PostgreSQL data source.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Transactions", name="TRANSACT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["rollback", "commit"]
		param.value = "commit"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '2')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Option('TRANSACT', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Disconnect All"
		self.description = "<p>Disconnects all PostgreSQL connections.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Transactions", name="TRANSACT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["rollback", "commit"]
		param.value = "commit"
		params  = [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '3')
		Tool.Set_Option('TRANSACT', parameters[0].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Begin Transaction"
		self.description = "<p>Begins a transaction, which will be finished later with a commit or rollback. Tries to add a save point, if already in transaction mode. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Save Point", name="SAVEPOINT", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "SAVEPOINT_01"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '4')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Option('SAVEPOINT', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Commit/Rollback Transaction"
		self.description = "<p>Execute a commit or rollback on open transactions with PostgreSQL source.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Transactions", name="TRANSACT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["rollback", "commit"]
		param.value = "commit"
		params += [param]
		param = arcpy.Parameter(displayName="Save Point", name="SAVEPOINT", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '5')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Option('TRANSACT', parameters[5].valueAsText)
		Tool.Set_Option('SAVEPOINT', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Execute SQL"
		self.description = "<p>Execute SQL commands on a connected PostgreSQL source. Separate different commands with a semicolon (';'). <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="SQL Statment", name="SQL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "CREATE TABLE myTable1 (Col1 VARCHAR(255) PRIMARY KEY, Col2 INTEGER);\nINSERT INTO myTable1 (Col1, Col2) VALUES('First Value', 1);\nDROP TABLE myTable1;\n"
		params += [param]
		param = arcpy.Parameter(displayName="Show Results", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Stop on Error", name="STOP", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '6')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Option('SQL', parameters[5].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[6].valueAsText)
		Tool.Set_Option('STOP', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "List Tables"
		self.description = "<p>Lists all tables of an PostgreSQL data source.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '10')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Output('TABLES', parameters[5].valueAsText, 'table')
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "List Table Fields"
		self.description = "<p>Loads table information from PostgreSQL data source.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Field Description", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '11')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Output('TABLE', parameters[5].valueAsText, 'table')
		Tool.Set_Option('TABLES', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Import Table"
		self.description = "<p>Imports a table from a PostgreSQL database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '12')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Output('TABLE', parameters[5].valueAsText, 'table')
		Tool.Set_Option('TABLES', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Export Table"
		self.description = "<p>Exports a table to a PostgreSQL database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Primary Key", name="TABLE_PK", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Not Null", name="TABLE_NN", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Unique", name="TABLE_UQ", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Table Name", name="NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="If table exists...", name="EXISTS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["abort export", "replace existing table", "append records, if table structure allows"]
		param.value = "abort export"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '13')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Input ('TABLE', parameters[5].valueAsText, 'table')
		Tool.Set_Option('TABLE_PK', parameters[6].valueAsText)
		Tool.Set_Option('TABLE_NN', parameters[7].valueAsText)
		Tool.Set_Option('TABLE_UQ', parameters[8].valueAsText)
		Tool.Set_Option('NAME', parameters[9].valueAsText)
		Tool.Set_Option('EXISTS', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Drop Table"
		self.description = "<p>Deletes a table from a PostgreSQL database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '14')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Option('TABLES', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Import Table from SQL Query"
		self.description = "<p>Import a SQL table from a PostgreSQL database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Table from SQL Query", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Fields", name="FIELDS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "*"
		params += [param]
		param = arcpy.Parameter(displayName="Where", name="WHERE", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Group by", name="GROUP", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Having", name="HAVING", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Order by", name="ORDER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Distinct", name="DISTINCT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '15')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Output('TABLE', parameters[5].valueAsText, 'table')
		Tool.Set_Option('TABLES', parameters[6].valueAsText)
		Tool.Set_Option('FIELDS', parameters[7].valueAsText)
		Tool.Set_Option('WHERE', parameters[8].valueAsText)
		Tool.Set_Option('GROUP', parameters[9].valueAsText)
		Tool.Set_Option('HAVING', parameters[10].valueAsText)
		Tool.Set_Option('ORDER', parameters[11].valueAsText)
		Tool.Set_Option('DISTINCT', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Import Shapes from PostGIS"
		self.description = "<p>Imports shapes from a PostGIS database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '20')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Output('SHAPES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TABLES', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Export Shapes to PostGIS"
		self.description = "<p>Exports shapes to a PostGIS database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Primary Key", name="SHAPES_PK", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Not Null", name="SHAPES_NN", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Unique", name="SHAPES_UQ", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Table Name", name="NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="If table exists...", name="EXISTS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["abort export", "replace existing table", "append records, if table structure allows"]
		param.value = "abort export"
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '21')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Input ('SHAPES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('SHAPES_PK', parameters[6].valueAsText)
		Tool.Set_Option('SHAPES_NN', parameters[7].valueAsText)
		Tool.Set_Option('SHAPES_UQ', parameters[8].valueAsText)
		Tool.Set_Option('NAME', parameters[9].valueAsText)
		Tool.Set_Option('EXISTS', parameters[10].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Update Shapes SRID"
		self.description = "<p> Change the SRID of all geometries in the user-specified column and table.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '22')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Option('TABLES', parameters[5].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Import Raster from PostGIS"
		self.description = "<p>Imports grids from a PostGIS database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		param = arcpy.Parameter(displayName="Where", name="WHERE", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '30')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Output('GRIDS', parameters[5].valueAsText, 'grid_list')
		Tool.Set_Option('TABLES', parameters[6].valueAsText)
		Tool.Set_Option('WHERE', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Export Raster to PostGIS"
		self.description = "<p>Exports grids to a PostGIS database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Bands", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		param = arcpy.Parameter(displayName="Table Name", name="NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Add Grid Name Field", name="GRID_NAME", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '31')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Input ('GRIDS', parameters[5].valueAsText, 'grid_list')
		Tool.Set_Option('TABLE', parameters[6].valueAsText)
		Tool.Set_Option('NAME', parameters[7].valueAsText)
		Tool.Set_Option('GRID_NAME', parameters[8].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Update Raster SRID"
		self.description = "<p> Change the SRID of all rasters in the user-specified column and table.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["<not set>"]
		param.value = "<not set>"
		params += [param]
		param = arcpy.Parameter(displayName="EPSG Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '32')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Set_Option('TABLES', parameters[5].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Create Database"
		self.description = "<p>Creates a new PostgreSQL Database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "localhost"
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "geo_test"
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "postgres"
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "postgres"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '35')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Drop Database"
		self.description = "<p>Deletes a PostgreSQL Database.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Host", name="PG_HOST", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "localhost"
		params  = [param]
		param = arcpy.Parameter(displayName="Port", name="PG_PORT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5432
		params += [param]
		param = arcpy.Parameter(displayName="Database", name="PG_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "geo_test"
		params += [param]
		param = arcpy.Parameter(displayName="User", name="PG_USER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "postgres"
		params += [param]
		param = arcpy.Parameter(displayName="Password", name="PG_PWD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "postgres"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('db_pgsql', '36')
		Tool.Set_Option('PG_HOST', parameters[0].valueAsText)
		Tool.Set_Option('PG_PORT', parameters[1].valueAsText)
		Tool.Set_Option('PG_NAME', parameters[2].valueAsText)
		Tool.Set_Option('PG_USER', parameters[3].valueAsText)
		Tool.Set_Option('PG_PWD', parameters[4].valueAsText)
		Tool.Run()
		return
