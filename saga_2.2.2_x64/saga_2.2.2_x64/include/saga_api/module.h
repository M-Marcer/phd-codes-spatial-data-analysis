/**********************************************************
 * Version $Id: module.h 2412 2015-02-17 22:18:08Z oconrad $
 *********************************************************/

///////////////////////////////////////////////////////////
//                                                       //
//                         SAGA                          //
//                                                       //
//      System for Automated Geoscientific Analyses      //
//                                                       //
//           Application Programming Interface           //
//                                                       //
//                  Library: SAGA_API                    //
//                                                       //
//-------------------------------------------------------//
//                                                       //
//                       module.h                        //
//                                                       //
//          Copyright (C) 2005 by Olaf Conrad            //
//                                                       //
//-------------------------------------------------------//
//                                                       //
// This file is part of 'SAGA - System for Automated     //
// Geoscientific Analyses'.                              //
//                                                       //
// This library is free software; you can redistribute   //
// it and/or modify it under the terms of the GNU Lesser //
// General Public License as published by the Free       //
// Software Foundation, version 2.1 of the License.      //
//                                                       //
// This library is distributed in the hope that it will  //
// be useful, but WITHOUT ANY WARRANTY; without even the //
// implied warranty of MERCHANTABILITY or FITNESS FOR A  //
// PARTICULAR PURPOSE. See the GNU Lesser General Public //
// License for more details.                             //
//                                                       //
// You should have received a copy of the GNU Lesser     //
// General Public License along with this program; if    //
// not, write to the Free Software Foundation, Inc.,     //
// 51 Franklin Street, 5th Floor, Boston, MA 02110-1301, //
// USA.                                                  //
//                                                       //
//-------------------------------------------------------//
//                                                       //
//    contact:    Olaf Conrad                            //
//                Institute of Geography                 //
//                University of Goettingen               //
//                Goldschmidtstr. 5                      //
//                37077 Goettingen                       //
//                Germany                                //
//                                                       //
//    e-mail:     oconrad@saga-gis.org                   //
//                                                       //
///////////////////////////////////////////////////////////

//---------------------------------------------------------

///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
#ifndef HEADER_INCLUDED__SAGA_API__module_H
#define HEADER_INCLUDED__SAGA_API__module_H


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
#include "parameters.h"


///////////////////////////////////////////////////////////
//														 //
//		XML tags for mark-up of module synopsis	 		 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
#define SG_XML_SYSTEM				SG_T("system")
#define SG_XML_SYSTEM_VER			SG_T("version")
#define SG_XML_SYSTEM_MLP			SG_T("library-path")
#define SG_XML_LIBRARY				SG_T("library")
#define SG_XML_LIBRARY_PATH			SG_T("path")
#define SG_XML_LIBRARY_NAME			SG_T("name")
#define SG_XML_MODULE				SG_T("module")
#define SG_XML_MODULE_ATT_NAME		SG_T("name")
#define SG_XML_MODULE_ATT_ID		SG_T("id")
#define SG_XML_MODULE_ATT_AUTHOR	SG_T("author")
#define SG_XML_SPECIFICATION		SG_T("specification")
#define SG_XML_SPEC_ATT_GRID		SG_T("grid")
#define SG_XML_SPEC_ATT_INTERA		SG_T("interactive")
#define SG_XML_MENU					SG_T("menu")
#define SG_XML_DESCRIPTION			SG_T("description")
#define SG_XML_PARAM				SG_T("parameter")
#define SG_XML_PARAM_ATT_NAME		SG_T("name")
#define SG_XML_PARAM_ATT_CLASS		SG_T("class")
#define SG_XML_PARAM_MAND			SG_T("mandatory")
#define SG_XML_PARAM_TYPE			SG_T("type")
#define SG_XML_PARAM_IDENT			SG_T("identifier")
#define SG_XML_PARAM_DESC			SG_T("description")
#define SG_XML_PARAM_PROP			SG_T("properties")
#define SG_XML_PARAM_LIST			SG_T("list")
#define SG_XML_PARAM_ITEM			SG_T("item")
#define SG_XML_PARAM_TABLE			SG_T("table")
#define SG_XML_PARAM_FIELD			SG_T("field")
#define SG_XML_PARAM_FIELD_ATT_NAME	SG_T("name")
#define SG_XML_PARAM_FIELD_ATT_TYPE	SG_T("type")
#define SG_XML_PARAM_MIN			SG_T("min")
#define SG_XML_PARAM_MAX			SG_T("max")

//---------------------------------------------------------
#define SG_XML_ERROR				SG_T("error")
#define SG_XML_ERROR_ATT_MSG		SG_T("message")
#define SG_XML_ERROR_ATT_DESC		SG_T("description")
#define SG_XML_WARNING				SG_T("warning")
#define SG_XML_MESSAGE				SG_T("message")
#define SG_XML_MESSAGE_PROC			SG_T("message-proc")
#define SG_XML_MESSAGE_EXEC			SG_T("message-exec")
#define SG_XML_PROGRESS				SG_T("progress")

//---------------------------------------------------------
#define SG_GET_XML_TAGGED_STR(value, tag)	CSG_String::Format(SG_T("<%s>%s</%s>"), tag, value, tag)
#define SG_GET_XML_TAGGED_INT(value, tag)	CSG_String::Format(SG_T("<%s>%d</%s>"), tag, value, tag)
#define SG_GET_XML_TAGGED_FLT(value, tag)	CSG_String::Format(SG_T("<%s>%f</%s>"), tag, value, tag)


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
typedef enum ESG_Module_Type
{
	MODULE_TYPE_Base			= 0,
	MODULE_TYPE_Interactive,
	MODULE_TYPE_Grid,
	MODULE_TYPE_Grid_Interactive,
	MODULE_TYPE_Chain
}
TSG_Module_Type;


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
typedef enum ESG_Module_Error
{
	MODULE_ERROR_Unknown		= 0,
	MODULE_ERROR_Calculation
}
TSG_Module_Error;


///////////////////////////////////////////////////////////
//														 //
//						CSG_Module						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
/**
  * CSG_Module is the base class for all executable SAGA modules.
  * @see CSG_Parameters
  * @see CSG_Module_Interactive
  * @see CSG_Module_Grid
  * @see CSG_Module_Grid_Interactive
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Module
{
	friend class CSG_Module_Interactive_Base;
	friend class CSG_Module_Library_Interface;
	friend class CSG_Module_Chain;

public:

	CSG_Module(void);
	virtual ~CSG_Module(void);

	virtual void				Destroy						(void);

	virtual TSG_Module_Type		Get_Type					(void)	{	return( MODULE_TYPE_Base );	}

	const CSG_String &			Get_ID						(void)	const	{	return( m_ID );	}

	const CSG_String &			Get_Library					(void)	const;
	const CSG_String &			Get_File_Name				(void)	const;	// Returns the file name of the module's library or, if this is a module chain, the associated XML file.
	const CSG_String &			Get_Name					(void)	const;
	const CSG_String &			Get_Description				(void)	const;
	const CSG_String &			Get_Author					(void)	const;
	const SG_Char *				Get_Icon					(void)	{	return( NULL );	}
	CSG_String					Get_Summary					(bool bParameters = true, const CSG_String &Menu = "", const CSG_String &Description = "", bool bXML = false);

	virtual CSG_String			Get_MenuPath				(void)	{	return( SG_T("") );	}
	virtual CSG_String			Get_MenuPath				(bool bSolved);

	int							Get_Parameters_Count		(void)	{	return( m_npParameters );	}
	CSG_Parameters *			Get_Parameters				(void)	{	return( &Parameters );	}
	CSG_Parameters *			Get_Parameters				(int i)	{	return( i >= 0 && i < m_npParameters ? m_pParameters[i] : NULL );	}
	CSG_Parameters *			Get_Parameters				(const CSG_String &Identifier);

	bool						Set_Parameter				(const CSG_String &Identifier, CSG_Parameter *pSource);
	bool						Set_Parameter				(const CSG_String &Identifier, int            Value, int Type = PARAMETER_TYPE_Undefined);
	bool						Set_Parameter				(const CSG_String &Identifier, double         Value, int Type = PARAMETER_TYPE_Undefined);
	bool						Set_Parameter				(const CSG_String &Identifier, void          *Value, int Type = PARAMETER_TYPE_Undefined);
	bool						Set_Parameter				(const CSG_String &Identifier, const SG_Char *Value, int Type = PARAMETER_TYPE_Undefined);

	bool						Update_Parameter_States		(void);

	void						Set_Callback				(bool bActive = true);
	void						Set_Manager					(class CSG_Data_Manager *pManager);

	bool						Settings_Push				(class CSG_Data_Manager *pManager = NULL);
	bool						Settings_Pop				(void);

	virtual bool				do_Sync_Projections			(void)	{	return( true  );	}

	virtual bool				needs_GUI					(void)	{	return( false );	}

	virtual bool				is_Grid						(void)	{	return( false );	}
	virtual bool				is_Interactive				(void)	{	return( false );	}
	bool						is_Progress					(void)	{	return( SG_UI_Process_Get_Okay(false) );	}
	bool						is_Executing				(void)	{	return( m_bExecutes );	}

	void						Set_Show_Progress			(bool bOn = true);

	virtual bool				On_Before_Execution			(void)	{	return( true );	}
	virtual bool				On_After_Execution			(void)	{	return( true );	}

	bool						Execute						(void);


protected:

	CSG_Parameters				Parameters;

	CSG_MetaData				History_Supplement;


	//-----------------------------------------------------
	void						Set_Name					(const CSG_String &String);
	void						Set_Description				(const CSG_String &String);
	void						Set_Author					(const CSG_String &String);

	//-----------------------------------------------------
	virtual bool				On_Execute					(void)	= 0;

	virtual int					On_Parameter_Changed		(CSG_Parameters *pParameters, CSG_Parameter *pParameter);
	virtual int					On_Parameters_Enable		(CSG_Parameters *pParameters, CSG_Parameter *pParameter);

	TSG_PFNC_Parameter_Changed	Get_Parameter_Changed		(void)	{	return( _On_Parameter_Changed );	}

	//-----------------------------------------------------
	CSG_Parameters *			Add_Parameters				(const CSG_String &Identifier, const CSG_String &Name, const CSG_String &Description);
	bool						Dlg_Parameters				(const CSG_String &Identifier);
	bool						Dlg_Parameters				(CSG_Parameters *pParameters, const CSG_String &Caption);


	//-----------------------------------------------------
	virtual bool				Process_Get_Okay			(bool bBlink = false);
	virtual void				Process_Set_Text			(const CSG_String &Text);

	virtual bool				Set_Progress				(double Percent);
	virtual bool				Set_Progress				(double Position, double Range);

	bool						Stop_Execution				(bool bDialog = true);

	void						Message_Add					(const CSG_String &Text, bool bNewLine = true);
	void						Message_Dlg					(const CSG_String &Text, const SG_Char *Caption = NULL);
	bool						Message_Dlg_Confirm			(const CSG_String &Text, const SG_Char *Caption = NULL);

	bool						Error_Set					(TSG_Module_Error Error_ID = MODULE_ERROR_Unknown);
	bool						Error_Set					(const CSG_String &Error_Text);
	bool						Error_Fmt					(const char    *Format, ...);
	bool						Error_Fmt					(const wchar_t *Format, ...);


	//-----------------------------------------------------
	bool						DataObject_Add				(CSG_Data_Object *pDataObject, bool bUpdate = false);
	bool						DataObject_Update			(CSG_Data_Object *pDataObject, int Show = SG_UI_DATAOBJECT_UPDATE_ONLY);
	bool						DataObject_Update			(CSG_Data_Object *pDataObject, double Parm_1, double Parm_2, int Show = SG_UI_DATAOBJECT_UPDATE_ONLY);

	void						DataObject_Update_All		(void);

	bool						DataObject_Get_Colors		(CSG_Data_Object *pDataObject, CSG_Colors &Colors);
	bool						DataObject_Set_Colors		(CSG_Data_Object *pDataObject, const CSG_Colors &Colors);
	bool						DataObject_Set_Colors		(CSG_Data_Object *pDataObject, int nColors, int Palette = SG_COLORS_DEFAULT, bool bRevert = false);

	bool						DataObject_Get_Parameters	(CSG_Data_Object *pDataObject, CSG_Parameters &Parameters);
	bool						DataObject_Set_Parameters	(CSG_Data_Object *pDataObject, CSG_Parameters &Parameters);

	CSG_Parameter *				DataObject_Get_Parameter	(CSG_Data_Object *pDataObject, const CSG_String &ID);
	bool						DataObject_Set_Parameter	(CSG_Data_Object *pDataObject, CSG_Parameter *pParameter);
	bool						DataObject_Set_Parameter	(CSG_Data_Object *pDataObject, const CSG_String &ID, int            Value);
	bool						DataObject_Set_Parameter	(CSG_Data_Object *pDataObject, const CSG_String &ID, double         Value);
	bool						DataObject_Set_Parameter	(CSG_Data_Object *pDataObject, const CSG_String &ID, void          *Value);
	bool						DataObject_Set_Parameter	(CSG_Data_Object *pDataObject, const CSG_String &ID, const SG_Char *Value);
	bool						DataObject_Set_Parameter	(CSG_Data_Object *pDataObject, const CSG_String &ID, double loVal, double hiVal);	// Range Parameter

	bool						DataObject_Set_History		(CSG_Parameter *pParameter, CSG_MetaData *pHistory = NULL);

	bool						Get_Projection				(CSG_Projection &Projection)	const;


private:

	bool						m_bExecutes, m_bError_Ignore, m_bShow_Progress;

	int							m_npParameters;

	CSG_Array					m_Settings_Stack;

	CSG_Parameters				**m_pParameters;

	CSG_String					m_ID, m_Library, m_Library_Menu, m_File_Name, m_Author;


	bool						_Synchronize_DataObjects	(void);

	CSG_MetaData				_Get_Output_History			(void);
	void						_Set_Output_History			(void);

	void						_Update_Parameter_States	(CSG_Parameters *pParameters);

	static int					_On_Parameter_Changed		(CSG_Parameter *pParameter, int Flags);

};


///////////////////////////////////////////////////////////
//														 //
//					CSG_Module_Grid						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
/**
  * CSG_Module_Grid.
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Module_Grid : public CSG_Module
{
public:
	CSG_Module_Grid(void);
	virtual ~CSG_Module_Grid(void);

	virtual TSG_Module_Type		Get_Type				(void)			{	return( MODULE_TYPE_Grid );	}

	CSG_Grid_System *			Get_System				(void)			{	return( Parameters.Get_Grid_System() );	}

	virtual bool				is_Grid					(void)			{	return( true );	}


protected:

	virtual bool				Set_Progress_NCells		(sLong iCell);
	virtual bool				Set_Progress			(int  iRow);
	virtual bool				Set_Progress			(double Position, double Range);

	//-----------------------------------------------------
	int							Get_NX					(void)						{	return( Get_System()->Get_NX() );				}
	int							Get_NY					(void)						{	return( Get_System()->Get_NY() );				}
	sLong						Get_NCells				(void)						{	return( Get_System()->Get_NCells() );			}
	double						Get_Cellsize			(void)						{	return( Get_System()->Get_Cellsize() );			}
	double						Get_Cellarea			(void)						{	return( Get_System()->Get_Cellarea() );			}
	double						Get_XMin				(void)						{	return( Get_System()->Get_XMin() );				}
	double						Get_YMin				(void)						{	return( Get_System()->Get_YMin() );				}
	double						Get_XMax				(void)						{	return( Get_System()->Get_XMax() );				}
	double						Get_YMax				(void)						{	return( Get_System()->Get_YMax() );				}
	int							Get_xTo					(int Dir, int x = 0)		{	return( Get_System()->Get_xTo(Dir, x) );		}
	int							Get_yTo					(int Dir, int y = 0)		{	return( Get_System()->Get_yTo(Dir, y) );		}
	int							Get_xFrom				(int Dir, int x = 0)		{	return( Get_System()->Get_xFrom(Dir, x) );		}
	int							Get_yFrom				(int Dir, int y = 0)		{	return( Get_System()->Get_yFrom(Dir, y) );		}
	double						Get_Length				(int Dir)					{	return( Get_System()->Get_Length(Dir) );		}
	double						Get_UnitLength			(int Dir)					{	return( Get_System()->Get_UnitLength(Dir) );	}
	bool						is_InGrid				(int x, int y)				{	return(	Get_System()->is_InGrid(x, y) );		}
	bool						is_InGrid				(int x, int y, int Rand)	{	return(	Get_System()->is_InGrid(x, y, Rand) );	}

	//-----------------------------------------------------
	void						Lock_Create				(void);
	void						Lock_Destroy			(void);

	bool						is_Locked				(int x, int y)	{	return( Lock_Get(x, y) != 0 );	}
	char						Lock_Get				(int x, int y)	{	return( m_pLock && x >= 0 && x < Get_System()->Get_NX() && y >= 0 && y < Get_System()->Get_NY() ? m_pLock->asChar(x, y) : 0 );	}

	void						Lock_Set				(int x, int y, char Value = 1)
	{
		if( m_pLock && x >= 0 && x < Get_System()->Get_NX() && y >= 0 && y < Get_System()->Get_NY() )
		{
			m_pLock->Set_Value(x, y, Value);
		}
	}


private:

	CSG_Grid					*m_pLock;

};


///////////////////////////////////////////////////////////
//														 //
//				CSG_Module_Interactive_Base				 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
typedef enum ESG_Module_Interactive_Mode
{
	MODULE_INTERACTIVE_UNDEFINED		= 0,
	MODULE_INTERACTIVE_LDOWN,
	MODULE_INTERACTIVE_LUP,
	MODULE_INTERACTIVE_LDCLICK,
	MODULE_INTERACTIVE_MDOWN,
	MODULE_INTERACTIVE_MUP,
	MODULE_INTERACTIVE_MDCLICK,
	MODULE_INTERACTIVE_RDOWN,
	MODULE_INTERACTIVE_RUP,
	MODULE_INTERACTIVE_RDCLICK,
	MODULE_INTERACTIVE_MOVE,
	MODULE_INTERACTIVE_MOVE_LDOWN,
	MODULE_INTERACTIVE_MOVE_MDOWN,
	MODULE_INTERACTIVE_MOVE_RDOWN
}
TSG_Module_Interactive_Mode;

//---------------------------------------------------------
typedef enum ESG_Module_Interactive_DragMode
{
	MODULE_INTERACTIVE_DRAG_NONE		= 0,
	MODULE_INTERACTIVE_DRAG_LINE,
	MODULE_INTERACTIVE_DRAG_BOX,
	MODULE_INTERACTIVE_DRAG_CIRCLE
}
TSG_Module_Interactive_DragMode;

//---------------------------------------------------------
#define MODULE_INTERACTIVE_KEY_LEFT		0x01
#define MODULE_INTERACTIVE_KEY_MIDDLE	0x02
#define MODULE_INTERACTIVE_KEY_RIGHT	0x04
#define MODULE_INTERACTIVE_KEY_SHIFT	0x08
#define MODULE_INTERACTIVE_KEY_ALT		0x10
#define MODULE_INTERACTIVE_KEY_CTRL		0x20

//---------------------------------------------------------
/**
  * CSG_Module_Interactive_Base.
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Module_Interactive_Base
{
	friend class CSG_Module_Interactive;
	friend class CSG_Module_Grid_Interactive;

public:
	CSG_Module_Interactive_Base(void);
	virtual ~CSG_Module_Interactive_Base(void);

	bool						Execute_Position		(CSG_Point ptWorld, TSG_Module_Interactive_Mode Mode, int Keys);
	bool						Execute_Keyboard		(int Character, int Keys);
	bool						Execute_Finish			(void);

	int							Get_Drag_Mode			(void)	{	return( m_Drag_Mode );	}


protected:

	virtual bool				On_Execute_Position		(CSG_Point ptWorld, TSG_Module_Interactive_Mode Mode);
	virtual bool				On_Execute_Keyboard		(int Character);
	virtual bool				On_Execute_Finish		(void);

	CSG_Point &					Get_Position			(void)	{	return( m_Point );				}
	double						Get_xPosition			(void)	{	return( m_Point.Get_X() );		}
	double						Get_yPosition			(void)	{	return( m_Point.Get_Y() );		}

	CSG_Point &					Get_Position_Last		(void)	{	return( m_Point_Last );			}
	double						Get_xPosition_Last		(void)	{	return( m_Point_Last.Get_X() );	}
	double						Get_yPosition_Last		(void)	{	return( m_Point_Last.Get_Y() );	}

	bool						is_Shift				(void)	{	return( (m_Keys & MODULE_INTERACTIVE_KEY_SHIFT) != 0 );	}
	bool						is_Alt					(void)	{	return( (m_Keys & MODULE_INTERACTIVE_KEY_ALT)   != 0 );	}
	bool						is_Ctrl					(void)	{	return( (m_Keys & MODULE_INTERACTIVE_KEY_CTRL)  != 0 );	}

	void						Set_Drag_Mode			(int Drag_Mode);


private:

	int							m_Keys, m_Drag_Mode;

	CSG_Point					m_Point, m_Point_Last;

	CSG_Module					*m_pModule;

};


///////////////////////////////////////////////////////////
//														 //
//				CSG_Module_Interactive					 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
/**
  * CSG_Module_Interactive.
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Module_Interactive : public CSG_Module_Interactive_Base, public CSG_Module
{
public:
	CSG_Module_Interactive(void);
	virtual ~CSG_Module_Interactive(void);

	virtual TSG_Module_Type		Get_Type				(void)	{	return( MODULE_TYPE_Interactive );	}

	virtual bool				needs_GUI				(void)	{	return( true );	}

	virtual bool				is_Interactive			(void)	{	return( true );	}

};


///////////////////////////////////////////////////////////
//														 //
//				CSG_Module_Grid_Interactive				 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
/**
  * CSG_Module_Grid_Interactive.
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Module_Grid_Interactive : public CSG_Module_Interactive_Base, public CSG_Module_Grid
{
public:
	CSG_Module_Grid_Interactive(void);
	virtual ~CSG_Module_Grid_Interactive(void);

	virtual TSG_Module_Type		Get_Type				(void)	{	return( MODULE_TYPE_Grid_Interactive );	}

	virtual bool				needs_GUI				(void)	{	return( true );	}

	virtual bool				is_Interactive			(void)	{	return( true );	}


protected:

	bool						Get_Grid_Pos			(int &x, int &y);

	int							Get_xGrid				(void);
	int							Get_yGrid				(void);

};


///////////////////////////////////////////////////////////
//														 //
//			Module Library Interface Definitions		 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
typedef enum ESG_MLB_Info
{
	MLB_INFO_Name	= 0,
	MLB_INFO_Description,
	MLB_INFO_Author,
	MLB_INFO_Version,
	MLB_INFO_Menu_Path,
	MLB_INFO_Category,
	MLB_INFO_User,
	MLB_INFO_File,
	MLB_INFO_Library,
	MLB_INFO_Count
}
TSG_MLB_Info;

//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Module_Library_Interface
{
public:
	CSG_Module_Library_Interface(void);
	virtual ~CSG_Module_Library_Interface(void);

	void						Set_Info				(int ID, const CSG_String &Info);
	const CSG_String &			Get_Info				(int ID);

	int							Get_Count				(void);
	bool						Add_Module				(CSG_Module *pModule, int ID);
	CSG_Module *				Get_Module				(int iModule);

	void						Set_File_Name			(const CSG_String &File_Name);


private:

	CSG_String					m_Info[MLB_INFO_Count];

	int							m_nModules;

	CSG_Module					**m_Modules;

};

//---------------------------------------------------------
#define SYMBOL_MLB_Initialize			SG_T("MLB_Initialize")
typedef bool							(* TSG_PFNC_MLB_Initialize)		(const SG_Char *);

#define SYMBOL_MLB_Finalize				SG_T("MLB_Finalize")
typedef bool							(* TSG_PFNC_MLB_Finalize)		(void);

#define SYMBOL_MLB_Get_Interface		SG_T("MLB_Get_Interface")
typedef CSG_Module_Library_Interface *	(* TSG_PFNC_MLB_Get_Interface)	(void);

//---------------------------------------------------------
#define MLB_INTERFACE_SKIP_MODULE		((CSG_Module *)0x1)

//---------------------------------------------------------
#define MLB_INTERFACE_CORE	CSG_Module_Library_Interface	MLB_Interface;\
\
extern "C" _SAGA_DLL_EXPORT CSG_Module_Library_Interface *	MLB_Get_Interface   (void)\
{\
	return( &MLB_Interface );\
}\
\
extern "C" _SAGA_DLL_EXPORT const SG_Char *					Get_Version			(void)\
{\
	return( SAGA_VERSION );\
}\

//---------------------------------------------------------
#define MLB_INTERFACE_INITIALIZE	extern "C" _SAGA_DLL_EXPORT bool MLB_Initialize	(const SG_Char *File_Name)\
{\
	int		i;\
\
	MLB_Interface.Set_File_Name(File_Name);\
\
	for(i=0; i<MLB_INFO_User; i++)\
	{\
		MLB_Interface.Set_Info(i, Get_Info(i));\
	}\
\
	for(i=0; MLB_Interface.Add_Module(Create_Module(i), i); i++)\
	{}\
\
	return( MLB_Interface.Get_Count() > 0 );\
}\

//---------------------------------------------------------
#define MLB_INTERFACE_FINALIZE		extern "C" _SAGA_DLL_EXPORT bool MLB_Finalize	(void)\
{\
	return( true );\
}\

//---------------------------------------------------------
#define MLB_INTERFACE	MLB_INTERFACE_CORE MLB_INTERFACE_INITIALIZE MLB_INTERFACE_FINALIZE

//---------------------------------------------------------
#ifndef SWIG

extern CSG_Module_Library_Interface	MLB_Interface;

#endif	// #ifdef SWIG


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
#endif // #ifndef HEADER_INCLUDED__SAGA_API__module_H
