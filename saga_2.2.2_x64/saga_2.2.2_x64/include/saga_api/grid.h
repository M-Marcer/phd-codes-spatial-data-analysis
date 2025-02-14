/**********************************************************
 * Version $Id: grid.h 2593 2015-09-23 07:34:34Z oconrad $
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
//                        grid.h                         //
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
#ifndef HEADER_INCLUDED__SAGA_API__grid_H
#define HEADER_INCLUDED__SAGA_API__grid_H


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
#include "table.h"
#include "grid_pyramid.h"


///////////////////////////////////////////////////////////
//														 //
//					Memory Handling						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
typedef enum ESG_Grid_Memory_Type
{
	GRID_MEMORY_Normal					= 0,
	GRID_MEMORY_Cache,
	GRID_MEMORY_Compression
}
TSG_Grid_Memory_Type;


///////////////////////////////////////////////////////////
//														 //
//						Grid File						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
typedef enum ESG_Grid_File_Format
{
	GRID_FILE_FORMAT_Undefined			= 0,
	GRID_FILE_FORMAT_Binary,
	GRID_FILE_FORMAT_ASCII
}
TSG_Grid_File_Format;

//---------------------------------------------------------
typedef enum ESG_Grid_File_Key
{
	GRID_FILE_KEY_NAME					= 0,
	GRID_FILE_KEY_DESCRIPTION,
	GRID_FILE_KEY_UNITNAME,
	GRID_FILE_KEY_DATAFILE_NAME,
	GRID_FILE_KEY_DATAFILE_OFFSET,
	GRID_FILE_KEY_DATAFORMAT,
	GRID_FILE_KEY_BYTEORDER_BIG,
	GRID_FILE_KEY_POSITION_XMIN,
	GRID_FILE_KEY_POSITION_YMIN,
	GRID_FILE_KEY_CELLCOUNT_X,
	GRID_FILE_KEY_CELLCOUNT_Y,
	GRID_FILE_KEY_CELLSIZE,
	GRID_FILE_KEY_Z_FACTOR,
	GRID_FILE_KEY_Z_OFFSET,
	GRID_FILE_KEY_NODATA_VALUE,
	GRID_FILE_KEY_TOPTOBOTTOM,
	GRID_FILE_KEY_Count
}
TSG_Grid_File_Key;

//---------------------------------------------------------
const SG_Char	gSG_Grid_File_Key_Names[GRID_FILE_KEY_Count][32]	=
{
	SG_T("NAME"),
	SG_T("DESCRIPTION"),
	SG_T("UNIT"),
	SG_T("DATAFILE_NAME"),
	SG_T("DATAFILE_OFFSET"),
	SG_T("DATAFORMAT"),
	SG_T("BYTEORDER_BIG"),
	SG_T("POSITION_XMIN"),
	SG_T("POSITION_YMIN"),
	SG_T("CELLCOUNT_X"),
	SG_T("CELLCOUNT_Y"),
	SG_T("CELLSIZE"),
	SG_T("Z_FACTOR"),
	SG_T("Z_OFFSET"),
	SG_T("NODATA_VALUE"),
	SG_T("TOPTOBOTTOM")
};

//---------------------------------------------------------
#define GRID_FILE_KEY_TRUE	SG_T("TRUE")
#define GRID_FILE_KEY_FALSE	SG_T("FALSE")


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
typedef enum ESG_Grid_Interpolation
{
	GRID_INTERPOLATION_NearestNeighbour	= 0,
	GRID_INTERPOLATION_Bilinear,
	GRID_INTERPOLATION_InverseDistance,
	GRID_INTERPOLATION_BicubicSpline,
	GRID_INTERPOLATION_BSpline,

	GRID_INTERPOLATION_Mean_Nodes,
	GRID_INTERPOLATION_Mean_Cells,
	GRID_INTERPOLATION_Minimum,
	GRID_INTERPOLATION_Maximum,
	GRID_INTERPOLATION_Majority,

	GRID_INTERPOLATION_Undefined
}
TSG_Grid_Interpolation;

//---------------------------------------------------------
typedef enum ESG_Grid_Operation
{
	GRID_OPERATION_Addition				= 0,
	GRID_OPERATION_Subtraction,
	GRID_OPERATION_Multiplication,
	GRID_OPERATION_Division
}
TSG_Grid_Operation;


///////////////////////////////////////////////////////////
//														 //
//					CSG_Grid_System						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
/**
  * CSG_Grid_System is used by the CSG_Grid class to provide
  * information about the number of rows and columns, the
  * cell size and the georeference, which define the grid.
  * It offers various functions, which help when working
  * with grids.
  * @see CSG_Grid
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Grid_System
{
public:
	CSG_Grid_System(void);
	CSG_Grid_System(const CSG_Grid_System &System);
	CSG_Grid_System(double Cellsize, const CSG_Rect &Extent);
	CSG_Grid_System(double Cellsize, double xMin, double yMin, double xMax, double yMax);
	CSG_Grid_System(double Cellsize, double xMin, double yMin, int NX, int NY);

	~CSG_Grid_System(void);


	//-----------------------------------------------------
	bool						is_Valid			(void)	const;

	const SG_Char *				Get_Name			(bool bShort = true);

	double						Get_Cellsize		(void)	const	{	return( m_Cellsize );	}
	double						Get_Cellarea		(void)	const	{	return( m_Cellarea );	}

	int							Get_NX				(void)	const	{	return( m_NX );			}
	int							Get_NY				(void)	const	{	return( m_NY );			}
	sLong						Get_NCells			(void)	const	{	return( m_NCells );		}

	const CSG_Rect &			Get_Extent			(bool bCells = false)	const	{	return( bCells ? m_Extent_Cells : m_Extent );	}

	double						Get_XMin			(bool bCells = false)	const	{	return( bCells ? m_Extent_Cells.Get_XMin  () : m_Extent.Get_XMin  () );	}
	double						Get_XMax			(bool bCells = false)	const	{	return( bCells ? m_Extent_Cells.Get_XMax  () : m_Extent.Get_XMax  () );	}
	double						Get_XRange			(bool bCells = false)	const	{	return( bCells ? m_Extent_Cells.Get_XRange() : m_Extent.Get_XRange() );	}

	double						Get_YMin			(bool bCells = false)	const	{	return( bCells ? m_Extent_Cells.Get_YMin  () : m_Extent.Get_YMin  () );	}
	double						Get_YMax			(bool bCells = false)	const	{	return( bCells ? m_Extent_Cells.Get_YMax  () : m_Extent.Get_YMax  () );	}
	double						Get_YRange			(bool bCells = false)	const	{	return( bCells ? m_Extent_Cells.Get_YRange() : m_Extent.Get_YRange() );	}


	//-----------------------------------------------------
	bool						operator ==			(const CSG_Grid_System &System) const;
	void						operator =			(const CSG_Grid_System &System);

	bool						Assign				(const CSG_Grid_System &System);
	bool						Assign				(double Cellsize, const CSG_Rect &Extent);
	bool						Assign				(double Cellsize, double xMin, double yMin, double xMax, double yMax);
	bool						Assign				(double Cellsize, double xMin, double yMin, int NX, int NY);

	bool						is_Equal			(const CSG_Grid_System &System) const;
	bool						is_Equal			(double Cellsize, const TSG_Rect &Extent) const;


	//-----------------------------------------------------
	/// Aligns the world coordinate x to the rows of the grid system and returns it.
	double						Fit_xto_Grid_System	(double x)	const	{	return( Get_XMin() + m_Cellsize * (int)(0.5 + (x - Get_XMin()) / m_Cellsize) );	}

	/// Aligns the world coordinate y to the columns of the grid system and returns it.
	double						Fit_yto_Grid_System	(double y)	const	{	return( Get_YMin() + m_Cellsize * (int)(0.5 + (y - Get_YMin()) / m_Cellsize) );	}

	/// Aligns the world coordinate ptWorld to the rows and columns of the grid system and returns it.
	TSG_Point					Fit_to_Grid_System	(TSG_Point ptWorld)	const
	{
		ptWorld.x	= Fit_xto_Grid_System(ptWorld.x);
		ptWorld.y	= Fit_yto_Grid_System(ptWorld.y);

		return( ptWorld );
	}


	//-----------------------------------------------------
	double						Get_xGrid_to_World	(int xGrid)	const	{	return( Get_XMin() + xGrid * m_Cellsize );	}
	double						Get_yGrid_to_World	(int yGrid)	const	{	return( Get_YMin() + yGrid * m_Cellsize );	}

	TSG_Point					Get_Grid_to_World	(int xGrid, int yGrid)	const
	{
		TSG_Point	pt;

		pt.x	= Get_xGrid_to_World(xGrid);
		pt.y	= Get_yGrid_to_World(yGrid);

		return( pt );
	}


	//-----------------------------------------------------
	int							Get_xWorld_to_Grid	(double xWorld)	const	{	return( (int)(0.5 + (xWorld - Get_XMin()) / m_Cellsize) );	}
	int							Get_yWorld_to_Grid	(double yWorld)	const	{	return( (int)(0.5 + (yWorld - Get_YMin()) / m_Cellsize) );	}

	bool						Get_World_to_Grid	(int &xGrid, int &yGrid, double xWorld, double yWorld)	const
	{
		return( is_InGrid(xGrid = Get_xWorld_to_Grid(xWorld), yGrid = Get_yWorld_to_Grid(yWorld)) );
	}

	bool						Get_World_to_Grid	(int &xGrid, int &yGrid, TSG_Point ptWorld)	const
	{
		return( is_InGrid(xGrid = Get_xWorld_to_Grid(ptWorld.x), yGrid = Get_yWorld_to_Grid(ptWorld.y)) );
	}


	//-----------------------------------------------------
	bool						Get_Neighbor_Pos	(int Direction, int x, int y, int &xPos, int &yPos)	const
	{
		return( is_InGrid(xPos = Get_xTo(Direction, x), yPos = Get_yTo(Direction, y)) );
	}

	static int					Get_xTo				(int Direction, int x = 0)
	{
		static int	ix[8]	= { 0, 1, 1, 1, 0,-1,-1,-1 };

		Direction	%= 8;

		if( Direction < 0 )
		{
			Direction	+= 8;
		}

		return( x + ix[Direction] );
	}

	static int					Get_yTo				(int Direction, int y = 0)
	{
		static int	iy[8]	= { 1, 1, 0,-1,-1,-1, 0, 1 };

		Direction	%= 8;

		if( Direction < 0 )
		{
			Direction	+= 8;
		}

		return( y + iy[Direction] );
	}

	static int					Get_xFrom			(int Direction, int x = 0)			{	return( Get_xTo(Direction + 4, x) );	}
	static int					Get_yFrom			(int Direction, int y = 0)			{	return( Get_yTo(Direction + 4, y) );	}

	int							Get_xToSave			(int Direction, int x)		const	{	return( (x = Get_xTo  (Direction, x)) < 0 ? 0 : (x >= m_NX ? m_NX - 1 : x) );	}
	int							Get_yToSave			(int Direction, int y)		const	{	return( (y = Get_yTo  (Direction, y)) < 0 ? 0 : (y >= m_NY ? m_NY - 1 : y) );	}
	int							Get_xFromSave		(int Direction, int x)		const	{	return( (x = Get_xFrom(Direction, x)) < 0 ? 0 : (x >= m_NX ? m_NX - 1 : x) );	}
	int							Get_yFromSave		(int Direction, int y)		const	{	return( (y = Get_yFrom(Direction, y)) < 0 ? 0 : (y >= m_NY ? m_NY - 1 : y) );	}

	bool						is_InGrid			(int x, int y)				const	{	return(	x >= 0    && x < m_NX        && y >= 0    && y < m_NY );		}
	bool						is_InGrid			(int x, int y, int Rand)	const	{	return(	x >= Rand && x < m_NX - Rand && y >= Rand && y < m_NY - Rand );	}

	double						Get_Length			(int Direction)				const	{	return( Direction % 2 ? m_Diagonal : m_Cellsize );	}
	static double				Get_UnitLength		(int Direction)						{	return( Direction % 2 ? sqrt(2.0)  : 1.0 );			}


private:	///////////////////////////////////////////////

	int							m_NX, m_NY;

	sLong						m_NCells;

	double						m_Cellsize, m_Cellarea, m_Diagonal;

	CSG_Rect					m_Extent, m_Extent_Cells;

	CSG_String					m_Name;

};


///////////////////////////////////////////////////////////
//														 //
//						CSG_Grid						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
/**
  * CSG_Grid is the data object created for raster handling.
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Grid_File_Info
{
//---------------------------------------------------------
public:		///////////////////////////////////////////////

	//-----------------------------------------------------
	CSG_Grid_File_Info(void);

								CSG_Grid_File_Info		(const CSG_Grid_File_Info &Info);
	bool						Create					(const CSG_Grid_File_Info &Info);

								CSG_Grid_File_Info		(const CSG_String &File_Name);
	bool						Create					(const CSG_String &File_Name);

								CSG_Grid_File_Info		(const CSG_Grid &Grid);
	bool						Create					(const CSG_Grid &Grid);

	bool						Save					(const CSG_String &File_Name                                                                      , bool bBinary = true);
	bool						Save					(const CSG_String &File_Name                      , int xStart, int yStart, int xCount, int yCount, bool bBinary = true);
	static bool					Save					(const CSG_String &File_Name, const CSG_Grid &Grid                                                , bool bBinary = true);
	static bool					Save					(const CSG_String &File_Name, const CSG_Grid &Grid, int xStart, int yStart, int xCount, int yCount, bool bBinary = true);


	//-----------------------------------------------------
	bool						m_bFlip, m_bSwapBytes;

	sLong						m_Offset;

	double						m_zScale, m_zOffset, m_NoData;

	TSG_Data_Type				m_Type;

	CSG_String					m_Name, m_Description, m_Unit, m_Data_File;

	CSG_Grid_System				m_System;

	CSG_Projection				m_Projection;


private:

	void						_On_Construction		(void);

	int							_Get_Key				(CSG_File &Stream, CSG_String &Line);

};


///////////////////////////////////////////////////////////
//														 //
//						CSG_Grid						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
/**
  * CSG_Grid is the data object created for raster handling.
*/
//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Grid : public CSG_Data_Object
{
//---------------------------------------------------------
public:		///////////////////////////////////////////////

	//-----------------------------------------------------
	CSG_Grid(void);

								CSG_Grid	(const CSG_Grid &Grid);
	bool						Create		(const CSG_Grid &Grid);

								CSG_Grid	(const CSG_String &File_Name, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal, bool bLoadData = true);
	bool						Create		(const CSG_String &File_Name, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal, bool bLoadData = true);

								CSG_Grid	(CSG_Grid *pGrid, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);
	bool						Create		(CSG_Grid *pGrid, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);

								CSG_Grid	(const CSG_Grid_System &System, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);
	bool						Create		(const CSG_Grid_System &System, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);

								CSG_Grid	(TSG_Data_Type Type, int NX, int NY, double Cellsize = 0.0, double xMin = 0.0, double yMin = 0.0, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);
	bool						Create		(TSG_Data_Type Type, int NX, int NY, double Cellsize = 0.0, double xMin = 0.0, double yMin = 0.0, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);


	//-----------------------------------------------------
	virtual ~CSG_Grid(void);

	virtual bool				Destroy	(void);


	//-----------------------------------------------------
	/** Data object type information.
	*/
	virtual TSG_Data_Object_Type	Get_ObjectType	(void)	const	{	return( DATAOBJECT_TYPE_Grid );		}


	//-----------------------------------------------------
	// Data-Info...

	TSG_Data_Type				Get_Type		(void)	const	{	return( m_Type );					}

	int							Get_nValueBytes	(void)	const	{	return( (int)SG_Data_Type_Get_Size(m_Type) );	}
	int							Get_nLineBytes	(void)	const	{	return( m_Type != SG_DATATYPE_Bit ? (int)SG_Data_Type_Get_Size(m_Type) * Get_NX() : 1 + Get_NX() / 8 );	}

	void						Set_Unit		(const SG_Char *String);
	const SG_Char *				Get_Unit		(void)	const;

	const CSG_Grid_System &		Get_System		(void)	const	{	return( m_System );					}

	int							Get_NX			(void)	const	{	return( m_System.Get_NX() );		}
	int							Get_NY			(void)	const	{	return( m_System.Get_NY() );		}
	sLong						Get_NCells		(void)	const	{	return( m_System.Get_NCells() );	}

	double						Get_Cellsize	(void)	const	{	return( m_System.Get_Cellsize() );	}
	double						Get_Cellarea	(void)	const	{	return( m_System.Get_Cellarea() );	}

	const CSG_Rect &			Get_Extent		(bool bCells = false)	const	{	return( m_System.Get_Extent(bCells) );	}

	double						Get_XMin		(bool bCells = false)	const	{	return( m_System.Get_XMin  (bCells) );	}
	double						Get_XMax		(bool bCells = false)	const	{	return( m_System.Get_XMax  (bCells) );	}
	double						Get_XRange		(bool bCells = false)	const	{	return( m_System.Get_XRange(bCells) );	}

	double						Get_YMin		(bool bCells = false)	const	{	return( m_System.Get_YMin  (bCells) );	}
	double						Get_YMax		(bool bCells = false)	const	{	return( m_System.Get_YMax  (bCells) );	}
	double						Get_YRange		(bool bCells = false)	const	{	return( m_System.Get_YRange(bCells) );	}

	double						Get_ZMin		(void);
	double						Get_ZMax		(void);
	double						Get_ZRange		(void);

	void						Set_Scaling		(double Scale = 1.0, double Offset = 0.0);
	double						Get_Scaling		(void)	const;
	double						Get_Offset		(void)	const;
	bool						is_Scaled		(void)	const	{	return( m_zScale != 1.0 || m_zOffset != 0.0 );	}

	double						Get_Mean		(void);
	double						Get_StdDev		(void);
	double						Get_Variance	(void);
	double						Get_Percentile	(double Percent);

	sLong						Get_Data_Count	(void);
	sLong						Get_NoData_Count(void);

	virtual bool				Save	(const CSG_String &File_Name, int Format = GRID_FILE_FORMAT_Binary);
	virtual bool				Save	(const CSG_String &File_Name, int Format, int xA, int yA, int xN, int yN);


	//-----------------------------------------------------
	// Checks...

	virtual bool				is_Valid		(void)	const;

	TSG_Intersection			is_Intersecting	(const CSG_Rect &Extent) const;
	TSG_Intersection			is_Intersecting	(const TSG_Rect &Extent) const;
	TSG_Intersection			is_Intersecting	(double xMin, double yMin, double xMax, double yMax) const;

	bool						is_Compatible	(CSG_Grid *pGrid) const;
	bool						is_Compatible	(const CSG_Grid_System &System) const;
	bool						is_Compatible	(int NX, int NY, double Cellsize, double xMin, double yMin) const;

	bool						is_InGrid		(int    x, int    y, bool bCheckNoData = true)	const	{	return( m_System.is_InGrid(x, y) && (!bCheckNoData || !is_NoData(x, y)) );	}
	bool						is_InGrid_byPos	(double x, double y, bool bCheckNoData = true)	const	{	return( x >= Get_XMin() && x <= Get_XMax() && y >= Get_YMin() && y <= Get_YMax() && (!bCheckNoData || !is_NoData(m_System.Get_xWorld_to_Grid(x), m_System.Get_yWorld_to_Grid(y))) );	}
	bool						is_InGrid_byPos	(TSG_Point Position, bool bCheckNoData = true)	const	{	return( is_InGrid_byPos(Position.x, Position.y, bCheckNoData) );	}


	//-----------------------------------------------------
	// Memory...

	sLong						Get_Memory_Size				(void)		const	{	return( Get_NCells() * Get_nValueBytes() );	}
	double						Get_Memory_Size_MB			(void)		const	{	return( (double)Get_Memory_Size() / N_MEGABYTE_BYTES );	}

	bool						Set_Buffer_Size				(sLong nBytes);
	int							Get_Buffer_Size				(void)		const	{	return( m_LineBuffer_Count * Get_nLineBytes() );	}

	bool						Set_Cache					(bool bOn);
	bool						is_Cached					(void)		const	{	return( m_Memory_Type == GRID_MEMORY_Cache );	}

	bool						Set_Compression				(bool bOn);
	bool						is_Compressed				(void)		const	{	return( m_Memory_Type == GRID_MEMORY_Compression );	};
	double						Get_Compression_Ratio		(void)		const;


	//-----------------------------------------------------
	// Operations...

	void						Assign_NoData				(void);

	virtual bool				Assign						(double Value = 0.0);
	virtual bool				Assign						(CSG_Data_Object *pObject);
	virtual bool				Assign						(CSG_Grid *pGrid, TSG_Grid_Interpolation Interpolation);

	void						Flip						(void);
	void						Mirror						(void);
	void						Invert						(void);

	bool						Normalise					(void);
	bool						DeNormalise					(double Minimum, double Maximum);

	bool						Standardise					(void);
	bool						DeStandardise				(double Mean, double StdDev);

	int							Get_Gradient_NeighborDir	(int x, int y, bool bMustBeLower = true)			const;
	bool						Get_Gradient				(int x, int y, double &Decline, double &Azimuth)	const;


	//-----------------------------------------------------
	// Set update flag when modified...

	virtual void				Set_Modified	(bool bOn = true)
	{
		CSG_Data_Object::Set_Modified(bOn);

		if( bOn )
		{
			Set_Update_Flag();

			Set_Index(false);
		}
	}


	//-----------------------------------------------------
	// Index...

	bool						Set_Index		(bool bOn = true)
	{
		if( !bOn )
		{
			m_bIndex	= false;

			return( true );
		}

		return( m_bIndex || _Set_Index() );
	}

	sLong						Get_Sorted		(sLong Position, bool bDown = true, bool bCheckNoData = true)
	{
		if( Position >= 0 && Position < Get_NCells() && (m_bIndex || _Set_Index()) )
		{
			Position	= m_Index[bDown ? Get_NCells() - Position - 1 : Position];

			if( !bCheckNoData || !is_NoData(Position) )
			{
				return( Position );
			}
		}

		return( -1 );
	}

	bool						Get_Sorted		(sLong Position, sLong &n, bool bDown = true, bool bCheckNoData = true)
	{
		return( (n = Get_Sorted(Position, bDown, false)) >= 0 && (!bCheckNoData || !is_NoData(n)) );
	}

	bool						Get_Sorted		(sLong Position, int &x, int &y, bool bDown = true, bool bCheckNoData = true)
	{
		if( (Position = Get_Sorted(Position, bDown, false)) >= 0 )
		{
			x	= (int)(Position % Get_NX());
			y	= (int)(Position / Get_NX());

			return( !bCheckNoData || !is_NoData(x, y) );
		}

		return( false );
	}


	//-----------------------------------------------------
	// No Data Value...

	virtual bool				is_NoData		(int x, int y)	const	{	return( is_NoData_Value(asDouble(x, y, false)) );	}
	virtual bool				is_NoData		(sLong n)		const	{	return( is_NoData_Value(asDouble(   n, false)) );	}

	virtual void				Set_NoData		(int x, int y)	{	Set_Value(x, y, Get_NoData_Value(), false);	}
	virtual void				Set_NoData		(sLong n)		{	Set_Value(   n, Get_NoData_Value(), false);	}


	//-----------------------------------------------------
	// Operators...

	virtual CSG_Grid &			operator  =		(const CSG_Grid &Grid);
	virtual CSG_Grid &			operator  =		(double Value);

	virtual CSG_Grid			operator +		(const CSG_Grid &Grid)	const;
	virtual CSG_Grid			operator +		(double Value)			const;
	virtual CSG_Grid &			operator +=		(const CSG_Grid &Grid);
	virtual CSG_Grid &			operator +=		(double Value);
	virtual CSG_Grid &			Add				(const CSG_Grid &Grid);
	virtual CSG_Grid &			Add				(double Value);

	virtual CSG_Grid			operator -		(const CSG_Grid &Grid)	const;
	virtual CSG_Grid			operator -		(double Value)			const;
	virtual CSG_Grid &			operator -=		(const CSG_Grid &Grid);
	virtual CSG_Grid &			operator -=		(double Value);
	virtual CSG_Grid &			Subtract		(const CSG_Grid &Grid);
	virtual CSG_Grid &			Subtract		(double Value);

	virtual CSG_Grid			operator *		(const CSG_Grid &Grid)	const;
	virtual CSG_Grid			operator *		(double Value)			const;
	virtual CSG_Grid &			operator *=		(const CSG_Grid &Grid);
	virtual CSG_Grid &			operator *=		(double Value);
	virtual CSG_Grid &			Multiply		(const CSG_Grid &Grid);
	virtual CSG_Grid &			Multiply		(double Value);

	virtual CSG_Grid			operator /		(const CSG_Grid &Grid)	const;
	virtual CSG_Grid			operator /		(double Value)			const;
	virtual CSG_Grid &			operator /=		(const CSG_Grid &Grid);
	virtual CSG_Grid &			operator /=		(double Value);
	virtual CSG_Grid &			Divide			(const CSG_Grid &Grid);
	virtual CSG_Grid &			Divide			(double Value);

	virtual double				operator ()		(int x, int y) const	{	return( asDouble(x, y) );	}


	//-----------------------------------------------------
	// Get Value...

	double						Get_Value(double xPos, double yPos,                int Interpolation = GRID_INTERPOLATION_BSpline, bool bByteWise = false, bool bOnlyValidCells = false) const;
	double						Get_Value(TSG_Point Position      ,                int Interpolation = GRID_INTERPOLATION_BSpline, bool bByteWise = false, bool bOnlyValidCells = false) const;
	bool						Get_Value(double xPos, double yPos, double &Value, int Interpolation = GRID_INTERPOLATION_BSpline, bool bByteWise = false, bool bOnlyValidCells = false) const;
	bool						Get_Value(TSG_Point Position      , double &Value, int Interpolation = GRID_INTERPOLATION_BSpline, bool bByteWise = false, bool bOnlyValidCells = false) const;

	virtual BYTE				asByte	(int x, int y, bool bScaled = true) const	{	return( SG_ROUND_TO_BYTE (asDouble(x, y, bScaled)) );	}
	virtual BYTE				asByte	(     sLong n, bool bScaled = true) const	{	return( SG_ROUND_TO_BYTE (asDouble(   n, bScaled)) );	}
	virtual char				asChar	(int x, int y, bool bScaled = true) const	{	return( SG_ROUND_TO_CHAR (asDouble(x, y, bScaled)) );	}
	virtual char				asChar	(     sLong n, bool bScaled = true) const	{	return( SG_ROUND_TO_CHAR (asDouble(   n, bScaled)) );	}
	virtual short				asShort	(int x, int y, bool bScaled = true) const	{	return( SG_ROUND_TO_SHORT(asDouble(x, y, bScaled)) );	}
	virtual short				asShort	(     sLong n, bool bScaled = true) const	{	return( SG_ROUND_TO_SHORT(asDouble(   n, bScaled)) );	}
	virtual int					asInt	(int x, int y, bool bScaled = true) const	{	return( SG_ROUND_TO_INT  (asDouble(x, y, bScaled)) );	}
	virtual int					asInt	(     sLong n, bool bScaled = true) const	{	return( SG_ROUND_TO_INT  (asDouble(   n, bScaled)) );	}
	virtual sLong				asLong	(int x, int y, bool bScaled = true) const	{	return( SG_ROUND_TO_SLONG(asDouble(x, y, bScaled)) );	}
	virtual sLong				asLong	(     sLong n, bool bScaled = true) const	{	return( SG_ROUND_TO_SLONG(asDouble(   n, bScaled)) );	}
	virtual float				asFloat	(int x, int y, bool bScaled = true) const	{	return( (float)          (asDouble(x, y, bScaled)) );	}
	virtual float				asFloat	(     sLong n, bool bScaled = true) const	{	return( (float)          (asDouble(   n, bScaled)) );	}

	//-----------------------------------------------------
	virtual double				asDouble(     sLong n, bool bScaled = true) const
	{
		return( asDouble((int)(n % Get_NX()), (int)(n / Get_NX()), bScaled) );
	}

	virtual double				asDouble(int x, int y, bool bScaled = true) const
	{
		double	Value;

		if( m_Memory_Type != GRID_MEMORY_Normal )
		{
			Value	= _LineBuffer_Get_Value(x, y);
		}
		else switch( m_Type )
		{
			default:	return( 0.0 );
			case SG_DATATYPE_Byte:		Value	= (double)((BYTE   **)m_Values)[y][x];	break;
			case SG_DATATYPE_Char:		Value	= (double)((char   **)m_Values)[y][x];	break;
			case SG_DATATYPE_Word:		Value	= (double)((WORD   **)m_Values)[y][x];	break;
			case SG_DATATYPE_Short:		Value	= (double)((short  **)m_Values)[y][x];	break;
			case SG_DATATYPE_DWord:		Value	= (double)((DWORD  **)m_Values)[y][x];	break;
			case SG_DATATYPE_Int:		Value	= (double)((int    **)m_Values)[y][x];	break;
			case SG_DATATYPE_Long:		Value	= (double)((sLong  **)m_Values)[y][x];	break;
			case SG_DATATYPE_Float:		Value	= (double)((float  **)m_Values)[y][x];	break;
			case SG_DATATYPE_Double:	Value	= (double)((double **)m_Values)[y][x];	break;
			case SG_DATATYPE_Bit:		Value	=(double)(((BYTE   **)m_Values)[y][x / 8] & m_Bitmask[x % 8]) == 0 ? 0.0 : 1.0;	break;
		}

		if( bScaled && is_Scaled() )
		{
			Value	= m_zOffset + m_zScale * Value;
		}

		return( Value );
	}


	//-----------------------------------------------------
	// Set Value...

	virtual void				Add_Value(int x, int y, double Value)	{	Set_Value(x, y, asDouble(x, y) + Value );	}
	virtual void				Add_Value(     sLong n, double Value)	{	Set_Value(   n, asDouble(   n) + Value );	}

	virtual void				Mul_Value(int x, int y, double Value)	{	Set_Value(x, y, asDouble(x, y) * Value );	}
	virtual void				Mul_Value(     sLong n, double Value)	{	Set_Value(   n, asDouble(   n) * Value );	}

	//-----------------------------------------------------
	virtual void				Set_Value(     sLong n, double Value, bool bScaled = true)
	{
		Set_Value((int)(n % Get_NX()), (int)(n / Get_NX()), Value, bScaled);
	}

	virtual void				Set_Value(int x, int y, double Value, bool bScaled = true)
	{
		if( bScaled && is_Scaled() )
		{
			Value	= (Value - m_zOffset) / m_zScale;
		}

		if( m_Memory_Type != GRID_MEMORY_Normal )
		{
			_LineBuffer_Set_Value(x, y, Value);
		}
		else switch( m_Type )
		{
			default:	return;
			case SG_DATATYPE_Byte:		((BYTE   **)m_Values)[y][x]	= SG_ROUND_TO_BYTE (Value);	break;
			case SG_DATATYPE_Char:		((char   **)m_Values)[y][x]	= SG_ROUND_TO_CHAR (Value);	break;
			case SG_DATATYPE_Word:		((WORD   **)m_Values)[y][x]	= SG_ROUND_TO_WORD (Value);	break;
			case SG_DATATYPE_Short:		((short  **)m_Values)[y][x]	= SG_ROUND_TO_SHORT(Value);	break;
			case SG_DATATYPE_DWord:		((DWORD  **)m_Values)[y][x]	= SG_ROUND_TO_DWORD(Value);	break;
			case SG_DATATYPE_Int:		((int    **)m_Values)[y][x]	= SG_ROUND_TO_INT  (Value);	break;
			case SG_DATATYPE_Long:		((sLong  **)m_Values)[y][x]	= SG_ROUND_TO_SLONG(Value);	break;
			case SG_DATATYPE_Float:		((float  **)m_Values)[y][x]	= (float )Value;			break;
			case SG_DATATYPE_Double:	((double **)m_Values)[y][x]	= (double)Value;			break;
			case SG_DATATYPE_Bit:		((BYTE   **)m_Values)[y][x / 8]	= Value != 0.0
					? ((BYTE  **)m_Values)[y][x / 8] |   m_Bitmask[x % 8]
					: ((BYTE  **)m_Values)[y][x / 8] & (~m_Bitmask[x % 8]);
				break;
		}

		Set_Modified();
	}


//---------------------------------------------------------
protected:	///////////////////////////////////////////////

	virtual bool				On_Update				(void);


//---------------------------------------------------------
private:	///////////////////////////////////////////////

	void						**m_Values;

	bool						m_bCreated, m_bIndex, m_Memory_bLock,
								m_Cache_bTemp, m_Cache_bSwap, m_Cache_bFlip;

	int							m_LineBuffer_Count;

	sLong						*m_Index, m_Cache_Offset;

	double						m_zOffset, m_zScale;

	CSG_Simple_Statistics		m_zStats;

	CSG_File					m_Cache_Stream;

	TSG_Data_Type				m_Type;

	TSG_Grid_Memory_Type		m_Memory_Type;

	CSG_Grid_System				m_System;

	CSG_String					m_Unit, m_Cache_Path;


	//-----------------------------------------------------
	static	BYTE				m_Bitmask[8];

	//-----------------------------------------------------
	typedef struct
	{
		bool	bModified;
		int		y;
		char	*Data;
	}
	TSG_Grid_Line;

	TSG_Grid_Line				*m_LineBuffer;


	//-----------------------------------------------------
	void						_On_Construction		(void);

	void						_Set_Properties			(TSG_Data_Type m_Type, int NX, int NY, double Cellsize, double xMin, double yMin);

	bool						_Set_Index				(void);


	//-----------------------------------------------------
	// Memory handling...

	int							_Get_nLineBytes			(void)	{	return( m_Type == SG_DATATYPE_Bit ? Get_NX() / 8 + 1 : Get_NX() * Get_nValueBytes() );	}

	bool						_Memory_Create			(TSG_Grid_Memory_Type aMemory_Type);
	void						_Memory_Destroy			(void);

	void						_LineBuffer_Create		(void);
	void						_LineBuffer_Destroy		(void);
	void						_LineBuffer_Flush		(void);
	TSG_Grid_Line *				_LineBuffer_Get_Line	(int y)							const;
	void						_LineBuffer_Set_Value	(int x, int y, double Value);
	double						_LineBuffer_Get_Value	(int x, int y)					const;

	bool						_Array_Create			(void);
	void						_Array_Destroy			(void);

	bool						_Cache_Create			(const SG_Char *FilePath, TSG_Data_Type File_Type, sLong Offset, bool bSwap, bool bFlip);
	bool						_Cache_Create			(void);
	bool						_Cache_Destroy			(bool bMemory_Restore);
	void						_Cache_LineBuffer_Save	(TSG_Grid_Line *pLine)			const;
	void						_Cache_LineBuffer_Load	(TSG_Grid_Line *pLine, int y)	const;

	bool						_Compr_Create			(void);
	bool						_Compr_Destroy			(bool bMemory_Restore);
	void						_Compr_LineBuffer_Save	(TSG_Grid_Line *pLine)			const;
	void						_Compr_LineBuffer_Load	(TSG_Grid_Line *pLine, int y)	const;


	//-----------------------------------------------------
	// File access...

	void						_Swap_Bytes				(char *Bytes, int nBytes)			const;

	bool						_Load					(const CSG_String &File_Name, TSG_Data_Type m_Type, TSG_Grid_Memory_Type aMemory_Type, bool bLoadData);

	bool						_Load_Binary			(CSG_File &Stream, TSG_Data_Type File_Type, bool bFlip, bool bSwapBytes);
	bool						_Save_Binary			(CSG_File &Stream, int xA, int yA, int xN, int yN, TSG_Data_Type File_Type, bool bFlip, bool bSwapBytes);
	bool						_Load_ASCII				(CSG_File &Stream, TSG_Grid_Memory_Type aMemory_Type, bool bFlip = false);
	bool						_Save_ASCII				(CSG_File &Stream, int xA, int yA, int xN, int yN, bool bFlip = false);
	bool						_Load_Native			(const CSG_String &File_Name, TSG_Grid_Memory_Type aMemory_Type, bool bLoadData);
	bool						_Save_Native			(const CSG_String &File_Name, int xA, int yA, int xN, int yN, bool bBinary = true);

	bool						_Load_Surfer			(const CSG_String &File_Name, TSG_Grid_Memory_Type aMemory_Type, bool bLoadData);

	//-----------------------------------------------------
	CSG_Grid &					_Operation_Arithmetic	(const CSG_Grid &Grid, TSG_Grid_Operation Operation);
	CSG_Grid &					_Operation_Arithmetic	(double Value        , TSG_Grid_Operation Operation);


	//-----------------------------------------------------
	// Interpolation subroutines...

	double						_Get_ValAtPos_NearestNeighbour	(int x, int y, double dx, double dy)				 const;
	double						_Get_ValAtPos_BiLinear			(int x, int y, double dx, double dy, bool bByteWise) const;
	double						_Get_ValAtPos_InverseDistance	(int x, int y, double dx, double dy, bool bByteWise) const;
	double						_Get_ValAtPos_BiCubicSpline		(int x, int y, double dx, double dy, bool bByteWise) const;
	double						_Get_ValAtPos_BiCubicSpline		(double dx, double dy, double z_xy[4][4])			 const;
	double						_Get_ValAtPos_BSpline			(int x, int y, double dx, double dy, bool bByteWise) const;
	double						_Get_ValAtPos_BSpline			(double dx, double dy, double z_xy[4][4])			 const;
	bool						_Get_ValAtPos_Fill4x4Submatrix	(int x, int y, double z_xy[4][4])					 const;
	bool						_Get_ValAtPos_Fill4x4Submatrix	(int x, int y, double z_xy[4][4][4])				 const;

	bool						_Assign_Interpolated	(CSG_Grid *pSource, TSG_Grid_Interpolation Interpolation);
	bool						_Assign_MeanValue		(CSG_Grid *pSource, bool bAreaProportional);
	bool						_Assign_ExtremeValue	(CSG_Grid *pSource, bool bMaximum);
	bool						_Assign_Majority		(CSG_Grid *pSource);

};


///////////////////////////////////////////////////////////
//														 //
//						Functions						 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
#define SG_GRID_PTR_SAFE_SET_NODATA(g, x, y)	{ if( g && g->is_InGrid(x, y, false) ) { g->Set_NoData(x, y   ); } }
#define SG_GRID_PTR_SAFE_SET_VALUE(g, x, y, z)	{ if( g && g->is_InGrid(x, y, false) ) { g->Set_Value (x, y, z); } }

//---------------------------------------------------------
/** Safe grid construction */
SAGA_API_DLL_EXPORT CSG_Grid *		SG_Create_Grid		(void);

/** Safe grid construction */
SAGA_API_DLL_EXPORT CSG_Grid *		SG_Create_Grid		(const CSG_Grid &Grid);

/** Safe grid construction */
SAGA_API_DLL_EXPORT CSG_Grid *		SG_Create_Grid		(const CSG_String &File_Name, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal, bool bLoadData = true);

/** Safe grid construction */
SAGA_API_DLL_EXPORT CSG_Grid *		SG_Create_Grid		(CSG_Grid *pGrid, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);

/** Safe grid construction */
SAGA_API_DLL_EXPORT CSG_Grid *		SG_Create_Grid		(const CSG_Grid_System &System, TSG_Data_Type Type = SG_DATATYPE_Undefined, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);

/** Safe grid construction */
SAGA_API_DLL_EXPORT CSG_Grid *		SG_Create_Grid		(TSG_Data_Type Type, int NX, int NY, double Cellsize = 0.0, double xMin = 0.0, double yMin = 0.0, TSG_Grid_Memory_Type Memory_Type = GRID_MEMORY_Normal);

//---------------------------------------------------------
/** Get default directory for grid caching */
SAGA_API_DLL_EXPORT const SG_Char *	SG_Grid_Cache_Get_Directory		(void);

/** Set default directory for grid caching */
SAGA_API_DLL_EXPORT void			SG_Grid_Cache_Set_Directory		(const SG_Char *Directory);

SAGA_API_DLL_EXPORT void			SG_Grid_Cache_Set_Automatic		(bool bOn);
SAGA_API_DLL_EXPORT bool			SG_Grid_Cache_Get_Automatic		(void);

SAGA_API_DLL_EXPORT void			SG_Grid_Cache_Set_Confirm		(int Confirm);
SAGA_API_DLL_EXPORT int				SG_Grid_Cache_Get_Confirm		(void);

SAGA_API_DLL_EXPORT void			SG_Grid_Cache_Set_Threshold		(int nBytes);
SAGA_API_DLL_EXPORT void			SG_Grid_Cache_Set_Threshold_MB	(double nMegabytes);
SAGA_API_DLL_EXPORT sLong			SG_Grid_Cache_Get_Threshold		(void);
SAGA_API_DLL_EXPORT double			SG_Grid_Cache_Get_Threshold_MB	(void);


///////////////////////////////////////////////////////////
//														 //
//                                                       //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
class CSG_Grid_Stack : public CSG_Stack
{
public:
	CSG_Grid_Stack(void) : CSG_Stack(sizeof(TSG_Point_Int))	{}

	//-----------------------------------------------------
	virtual bool			Push			(int  x, int  y)
	{
		TSG_Point_Int	*pPoint	= (TSG_Point_Int *)Get_Record_Push();

		if( pPoint )
		{
			pPoint->x	= x;
			pPoint->y	= y;

			return( true );
		}

		return( false );
	}

	//-----------------------------------------------------
	virtual bool			Pop				(int &x, int &y)
	{
		TSG_Point_Int	*pPoint	= (TSG_Point_Int *)Get_Record_Pop();

		if( pPoint )
		{
			x	= pPoint->x;
			y	= pPoint->y;

			return( true );
		}

		return( false );
	}

};


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
class SAGA_API_DLL_EXPORT CSG_Grid_Cell_Addressor
{
public:
	CSG_Grid_Cell_Addressor(void);

	bool						Destroy				(void);

	CSG_Distance_Weighting &	Get_Weighting		(void)								{	return( m_Weighting );		}

	bool						Set_Radius			(double Radius, bool bSquare = false);
	bool						Set_Annulus			(double inner_Radius, double outer_Radius);
	bool						Set_Sector			(double Radius, double Direction, double Tolerance);

	int							Get_Count			(void)	const						{	return( m_Cells.Get_Count() );	}

	int							Get_X				(int Index, int Offset = 0)	const	{	return( Offset + (Index >= 0 && Index < Get_Count() ? m_Cells.Get_Record_byIndex(Index)->asInt(0) : 0) );	}
	int							Get_Y				(int Index, int Offset = 0)	const	{	return( Offset + (Index >= 0 && Index < Get_Count() ? m_Cells.Get_Record_byIndex(Index)->asInt(1) : 0) );	}

	double						Get_Distance		(int Index)	const					{	return( Index >= 0 && Index < Get_Count() ? m_Cells.Get_Record_byIndex(Index)->asDouble(2) : -1.0 );	}
	double						Get_Weight			(int Index)	const					{	return( Index >= 0 && Index < Get_Count() ? m_Cells.Get_Record_byIndex(Index)->asDouble(3) : -1.0 );	}

	bool						Get_Values			(int Index, int &x, int &y, double &Distance, double &Weight, bool bOffset = false)	const
	{
		if( Index >= 0 && Index < Get_Count() )
		{
			CSG_Table_Record	*pCell	= m_Cells.Get_Record_byIndex(Index);

			if( bOffset )
			{
				x	+= pCell->asInt(0);
				y	+= pCell->asInt(1);
			}
			else
			{
				x	 = pCell->asInt(0);
				y	 = pCell->asInt(1);
			}

			Distance	= pCell->asDouble(2);
			Weight		= pCell->asDouble(3);

			return( true );
		}

		return( false );
	}


private:

	CSG_Distance_Weighting		m_Weighting;

	CSG_Table					m_Cells;

};


///////////////////////////////////////////////////////////
//														 //
//														 //
//														 //
///////////////////////////////////////////////////////////

//---------------------------------------------------------
#endif // #ifndef HEADER_INCLUDED__SAGA_API__grid_H
