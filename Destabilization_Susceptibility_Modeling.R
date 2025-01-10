#############################################################
# Understanding Destabilisation 	     				 
#										
# Version created to revise manuscript
# Implemented changes :
#  	1. Gullies are no longer destabilisation signs
# 	2. Geology introduced
#											
# Created 06/08/2018			
# 
#
# In this version is used the final version of the Destabilization evicences and Inventory
#############################################################


########################################################################
#
#	PART 0 - Data Preparation - This step is common to any setting. Can be skypped after first run
#
########################################################################


# Step 0 - Set Working station
rm(list = ls(all.names = TRUE))

root = "D:/Marcer_Materials"

# Set R Working Directory
wd<-paste(root,"codes",sep="/")
setwd(wd)

# Add libraries
source(paste(wd,"TOOLBOX/Libraries.R",sep='/'))

# RSAGA working environment
SAGAWD=paste(wd,"SAGAWD",sep='/')
myenv<-rsaga.env(workspace=SAGAWD,path=paste(wd,"saga_2.2.2_x64/saga_2.2.2_x64",sep="/"))

# GRID DATABASE DATA FOLDER
GRIDSPATH=paste(root,"data/grids",sep="/")

# OUTPUT DATA FOLDER
OUTPUT=paste(wd,"RESULTS",sep="/")

# MODELING ENVIRONMENT/French Alps
ME=paste(wd,"Modeling_Environment",sep="/")

#####################
# Define Data sources
######################

#Inventories
inv<-paste(root,"data/shapes/inventory_RTM/rock_glaciers_france_inventory.shp",sep='/')
invC<-paste(root,"final_products/regional/shapes/rock_glacier_inventory/rock_glaciers_centroids_MM.shp",sep='/')
cracks<-paste(root,"final_products/regional/shapes/surface_disturbances/cracks_lines.shp",sep='/')
clusters<-paste(root,"final_products/regional/shapes/surface_disturbances/cracks_clusters.shp",sep='/')
scarps<-paste(root,"final_products/regional/shapes/surface_disturbances/scarps.shp",sep='/')
crevasses<-paste(root,"final_products/regional/shapes/surface_disturbances/crevasses.shp",sep='/')

# Grids
DEM<-paste(GRIDSPATH,"DEM25.tif",sep='/')
PISR<-paste(GRIDSPATH,"PISR25.tif",sep='/')
Slope<-paste(GRIDSPATH,"slope25.tif",sep='/')
DC<-paste(GRIDSPATH,"Downslope_Curvature.sgrd",sep='/')

dPFI<-paste(root,"final_products/regional/grids/Marcer_etal_2019_PTP.tif",sep='/')
PFI<-paste(root,"final_products/regional/grids/Marcer_etal_2017_PFI_LIA.tif",sep='/')

# Shapes
geol<-paste(root,"data/shapes/PFI_data/Lithology_BRGM_1000000.shp",sep='/')

########################################################################

#Step 1 - Data Preparation 


# Create a layer using only active rock glaciers -- for making sampling faster
inv_lay<-readOGR(dsn=paste(root,"data/shapes/inventory_RTM",sep="/"),layer="rock_glaciers_france_inventory")
inv_a<-subset(inv_lay,Activity=="A")
writeOGR(inv_a,dsn=SAGAWD,layer="inv_actives_subset",driver="ESRI Shapefile",overwrite_layer=T)

# Create Base sampling points (common to each possible buffer) -- this is supposed to take lots of time
rsaga.geoprocessor("shapes_grid",3,list(GRIDS=DEM,POLYGONS="inv_actives_subset.shp",SHAPES="sampling_points.shp"),env=myenv)

# Sample GRIDS
rsaga.geoprocessor("shapes_grid",0,list(GRIDS=Slope,SHAPES="sampling_points.shp",RESULT="sampling_points.shp"),env=myenv)
rsaga.geoprocessor("shapes_grid",0,list(GRIDS=dPFI,SHAPES="sampling_points.shp",RESULT="sampling_points.shp"),env=myenv)
rsaga.geoprocessor("shapes_grid",0,list(GRIDS=PISR,SHAPES="sampling_points.shp",RESULT="sampling_points.shp"),env=myenv)
rsaga.geoprocessor("shapes_grid",0,list(GRIDS=DC,SHAPES="sampling_points.shp",RESULT="sampling_points.shp"),env=myenv)

# Buffer line data
buffer<-30 #Destabilisation evidences Buffer
rsaga.geoprocessor("shapes_tools",18,list(SHAPES=cracks,BUFFER="cracks_buffer.shp",DIST_FIELD=buffer,DIST_FIELD_DEFAULT=buffer),env=myenv)
rsaga.geoprocessor("shapes_tools",18,list(SHAPES=clusters,BUFFER="clusters_buffer.shp",DIST_FIELD=5,DIST_FIELD_DEFAULT=buffer),env=myenv)
rsaga.geoprocessor("shapes_tools",18,list(SHAPES=scarps,BUFFER="scarps_buffer.shp",DIST_FIELD=5,DIST_FIELD_DEFAULT=buffer),env=myenv)
rsaga.geoprocessor("shapes_tools",18,list(SHAPES=crevasses,BUFFER="crevasses_buffer.shp",DIST_FIELD=5,DIST_FIELD_DEFAULT=buffer),env=myenv)


# Import data and merge 
lay1<-readOGR(dsn=SAGAWD,layer="cracks_buffer")
lay2<-readOGR(dsn=SAGAWD,layer="clusters_buffer")
lay3<-readOGR(dsn=SAGAWD, layer="scarps_buffer")
lay4<-readOGR(dsn=SAGAWD,layer="crevasses_buffer")
spl<-list(lay1,lay2,lay3,lay4)
m <- do.call(bind, spl) 
writeOGR(m,dsn=SAGAWD,layer="unstable_areas",driver="ESRI Shapefile",overwrite_layer=T)

# Make a "transition buffer" around unstable areas
rsaga.geoprocessor("shapes_tools",18,list(SHAPES="unstable_areas.shp",BUFFER="transition_area.shp",DIST_FIELD=20,DIST_FIELD_DEFAULT=30),env=myenv)

# Cut buffers with inventory
rsaga.geoprocessor("shapes_polygons",11,list(CLIP="inv_actives_subset.shp",
	S_INPUT="unstable_areas.shp",S_OUTPUT="unstable_areas.shp",
	M_INPUT="unstable_areas.shp",M_OUTPUT="unstable_areas.shp"),env=myenv)
rsaga.geoprocessor("shapes_polygons",11,list(CLIP="inv_actives_subset.shp",
	S_INPUT="transition_area.shp",S_OUTPUT="transition_area.shp",
	M_INPUT="transition_area.shp",M_OUTPUT="transition_area.shp"),env=myenv)


########################################################################

# Step 2 : SAMPLING Stable-Unstable Areas and rock glacier properties.

# Sample Shapefiles
rsaga.geoprocessor("shapes_points",10,list(INPUT="sampling_points.shp",OUTPUT="sampling_points.shp",POLYGONS="unstable_areas.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="sampling_points.shp",OUTPUT="sampling_points.shp",POLYGONS="transition_area.shp",FIELDS="ID"),env=myenv)

rsaga.geoprocessor("shapes_polygons",20, list(INPUT="inv_actives_subset.shp",POINTS=invC,FIELDS="Dest_rate",OUTPUT="inv_actives_subset_DI.shp"),env=myenv)
rsaga.geoprocessor("shapes_polygons",20, list(INPUT="inv_actives_subset_DI.shp",POINTS=invC,FIELDS="sample_spe",OUTPUT="inv_actives_subset_DI.shp"),env=myenv)
rsaga.geoprocessor("shapes_polygons",20, list(INPUT="inv_actives_subset_DI.shp",POINTS=invC,FIELDS="ID_complet",OUTPUT="inv_actives_subset_DI.shp"),env=myenv)


rsaga.geoprocessor("shapes_points",10,list(INPUT="sampling_points.shp",OUTPUT="sampling_points.shp",POLYGONS="inv_actives_subset_DI.shp",FIELDS="Dest_rate"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="sampling_points.shp",OUTPUT="sampling_points.shp",POLYGONS="inv_actives_subset_DI.shp",FIELDS="sample_spe"),env=myenv)
rsaga.geoprocessor("shapes_points",10,list(INPUT="sampling_points.shp",OUTPUT="sampling_points.shp",POLYGONS="inv_actives_subset_DI.shp",FIELDS="ID_complet"),env=myenv)


####################################################################################################################################################################
####################################################################################################################################################################

########################################################################
#
#	PART 1 - MODELING 
#
########################################################################

library(rgdal)
library(sperrorest)
library(mgcv)

# Model specifications 

	nsp<-5 	# How many points per rock glacier to be used in the model?

########################################################################

#Step 0 - Create Modeling Database


# 1.1 Load shapefile with sampling points and initialize database

P<-readOGR(dsn=SAGAWD,layer="sampling_points")

# Define here which points use in the database
P1f<-subset(P,ID.1==0 & Dest_rate=="3" | Dest_rate=="4")
P0f<-subset(P,is.na(ID.1)==TRUE & strtoi(Dest_rate)<2 & sample_spe==strtoi(1))

# Write file to check
writeOGR(P1f,dsn=SAGAWD,layer="P1f",driver="ESRI Shapefile",overwrite_layer=T)
writeOGR(P0f,dsn=SAGAWD,layer="P0f",driver="ESRI Shapefile",overwrite_layer=T)

# Give factor variables
P1f$p<-1
P0f$p<-0

DB<-rbind(P1f,P0f)
DB$P<-factor(DB$p)

# 1.2 Get IDs of rock glaciers (There are multiple points per rock glacier)

	idx<-unique(as.numeric(as.character(DB$ID_complet)))	  
	idx = idx[!is.na(idx)]
	nP<-length(idx)


# 1.3 Obtain a random subsample of nsp points per rock glacier. All rock glaciers are used
	
	# Initialize modeling database for modeling based on model specifications
	NDB<-array(NA,dim=c(nsp*nP,ncol(DB)+2))
	colnames(NDB)<-names(as.data.frame(DB))

	# Create database for modeling based on model specifications
	for (i in 1:nP){
		temp<-subset(DB,ID_complet==idx[[i]])								# Get points in the ith rock glaciers
		if (length(temp)>nsp){mysample <- temp[sample(1:nrow(temp),nsp,replace=FALSE),]}	# If in the ith rock glaciers there are more than nsp points, than random subset
		else{mysample <- temp[sample(1:nrow(temp),nsp,replace=TRUE),]}				# Otherwise, random subset with replacement
		NDB[(nsp*i-nsp+1):(nsp*i),]<-as.numeric(as.matrix(as.data.frame(mysample,stringsAsFactors = FALSE)))
		}

# 1.4 Final arrangements to the ,modeling database

	destab<-data.frame(NDB)
	
	destab$x<-destab$X
	destab$y<-destab$Y
	destab$P<-factor(destab$p)

	colnames(destab)<-colnames(NDB) # was: factor(colnames(NDB)

	keeps <- c("X","Y","p","DEM25","PISR25","Marcer_etal","slope25","Downslope_C","ID_complet")
	destab<-destab[,keeps]	
	destab$unstable <- factor(destab$p == 1)
	destab$dPFI <- destab$Marcer_etal


# Step 2 -  GAM Modeling
# Sperrorest using GAM and partition.kmeans

  # Note that I am limiting the flexibility of the GAM
	# manually using s(...,k=4) to avoid weird oscillating
	# behaviour in the transformation function! I think that
	# this is reasonable and I (and others, I believe) have
	# done this before. It should only be mentioned in the
	# manuscript, in case we keep it as is.
my_gam <- function(formula, data, ...) {
  response <- all.vars(formula)[1]
  predictors <- all.vars(formula)[-1]
  s_pred <- paste("s(", predictors, ",k=4)", sep="")
  formula <- paste( response, "~",
                    paste(s_pred, collapse="+") )
  formula <- as.formula(formula)
  fit <- mgcv::gam(formula, data, ...)
  return(fit)
}

# check that it works:
fo <- unstable ~ DEM25 + slope25 + PISR25 + Downslope_C
testfit <- my_gam(fo, destab, family="binomial")
summary(testfit)
plot(testfit)
	
out <- sperrorest(data = destab, formula = fo,
	                  coords = c("X","Y"),
	                  model_fun = my_gam,
	                  model_args = list(family = "binomial"),
	                  pred_fun = predict,
	                  pred_args = list(type = "response"),
	                  smp_fun = partition_kmeans,
	                  smp_args = list(nfold=2, repetition=1:5, seed1=123), #use 100 repetitions in final run
	                  err_fun = err_default,
                    par_args = list(par_mode="sequential"),
                   importance = TRUE, 
	                  imp_permutations = 5 # use 100 in your final run
	                  # --> may take several hours
	)
	
	# Training set AUROC, and spatial cross-validation estimate of AUROC:	
	#summary(out$error_rep)
	round(summary(out$error_rep)[c("train_auroc","test_auroc"),c("mean","sd")],3)
	
	imp <- summary(out$importance)
	nms <- rownames(imp)
	imp <- imp[,"mean.auroc"]
	names(imp) <- nms
	# mean AUROC reduction based on 
	# permutation of each predictor:
	sort(imp, decr=TRUE) 
	
	out.gam <- out
	imp.gam <- imp
	
	####### do something like this:
	save(out.gam, imp.gam, file="results_gam_dem.Rdata")
	
	
#####################################################################################################################
# Step 3 - Transformation Plots

	point0<-subset(destab,p==0)
	point1<-subset(destab,p==1)
	ep=0.2
	M=4	
	m=-7

	# GAM:
fit <- my_gam(fo, destab, family="binomial")
	summary(fit)

	plot(fit,scheme = 1,unconditional = TRUE,pages=0,select=1,ylim=c(-8,5),cex.axis=2)
	points(point1$dPFI,runif(length(point1$dPFI),M-ep,M+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)
	points(point0$dPFI,runif(length(point0$dPFI),m-ep,m+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)


	plot(fit,scheme = 1,unconditional = TRUE,pages=0,select=1,ylim=c(-8,5),cex.axis=2)
	points(point1$DEM25,runif(length(point1$DEM25),M-ep,M+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)
	points(point0$DEM25,runif(length(point0$DEM25),m-ep,m+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)

	plot(fit,scheme = 1,unconditional = TRUE,pages=0,select=2,ylim=c(-8,5),cex.axis=2)
	points(point1$Slope25,runif(length(point1$Slope25),M-ep,M+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)
	points(point0$Slope25,runif(length(point0$Slope25),m-ep,m+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)

	plot(fit,scheme = 1,unconditional = TRUE,pages=0,select=3,ylim=c(-8,5),cex.axis=2)
	points(point1$PISR25,runif(length(point1$PISR25),M-ep,M+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)
	points(point0$PISR25,runif(length(point0$PISR25),m-ep,m+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)

	plot(fit,scheme = 1,unconditional = TRUE,pages=0,select=4,ylim=c(-8,5),cex.axis=2)
	points(point1$Downslope_C,runif(length(point1$PISR25),M-ep,M+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)
	points(point0$Downslope_C,runif(length(point0$PISR25),m-ep,m+ep),
	pch=19,col=rgb(0.5,0.5,0.5,alpha=0.3),cex=0.7)

	# GLM:
fit.glm <- glm(fo, destab, family="binomial")
summary(fit.glm) # don't trust the standard errors and p-values	

######################################################################
# Step 4 - Mapping

# For this part the user needs to convert the needed data in asc format and put them in the ME folder. Make sure that asc grids have the same grid system


setwd(ME)

multi.local.function(in.grids = c("PISR25","Slope25","Downslope_C","DEM25"),out.varnames = "GAM_DEM_Slope_TWI_PISR_DC_5samples_V3.asc",fun = grid.predict,control.predict=list(type="response"),fit=fit)

#########################################################################"

# Step 5 - Surface Calculator per destabilization susceptility values

# Sample destabilization susceptibility map

	# DSM, at this stage the one produced in Marcer et al 2019. Change to the one produced in step 4 if needed to work on the new map
	defrost<-paste(root,"final_products/regional/grids/Marcer_etal_2019_Destabilization_Susceptibility_Map_Unclipped.asc",sep='/')

	# Sample DEFROST index map
	rsaga.geoprocessor("shapes_grid",0,list(GRIDS=defrost,SHAPES="sampling_points.shp",RESULT="sampling_points.shp"),env=myenv)

# Import points, compute surfaces

	p<-readOGR(dsn=SAGAWD,layer="sampling_points")
	
	p$defrost<-p$Marcer_etal.1
	p$Dest_Index<-p$Dest_rate

	boxplot(defrost ~ Dest_rate, data=p)

	# Find percentiles (values by Rudy et al., 2017), classified by very low, low, medium, high, very high.
	breaks<-quantile(p$defrost,probs=c(0,0.5,0.75,0.90,0.95,1),na.rm=TRUE)
	M.cut = cut(p$defrost,breaks, right=TRUE)
	M.freq = table(M.cut)
	
	# ---- RESULT ---- SURFACES BY DEFROST INDEX ON ROCK GLACIERS
	model.surface=data.frame(M.freq*25*25/(10^6)) #surface in km2


# Make a table per rock glaciers with how many points are in breaks of defrost
# This code is very sensitive to number of breaks. Change that, need to change all the indexing

	breaks<-quantile(p$defrost,probs=c(0,0.5,0.75,0.90,0.95,1),na.rm=TRUE)
	idx<-unique(p$ID_complet)

	res<-array(-999,dim=c(length(idx),length(breaks)+1))
	n=dim(res)[2]

	for (i in 1:length(idx)){
		temp<-subset(p, ID_complet==idx[[i]])
		temp.cut<-cut(temp$defrost,breaks,right=TRUE)
		temp.freq<-table(temp.cut)

		res[i,1]<-as.numeric(as.character(idx[i]))
		res[i,2]<-as.numeric(as.character(temp$Dest_Index[1]))
		res[i,3:n]<-as.vector(temp.freq)
	}
	
	colnames(res)=c("ID","Dest_idx","very low","low","medium","high","very high")

	# Compute % surfaces
	res_perc<-res


	for (i in 1 : length(idx)){
		res_perc[i,3:n]  <- res[i,3:n]*100/sum (res[i,3:n])

	}

	# --- RESULT --- Surface % per defrost class per rock glacier
	final<-data.frame(res_perc)

	boxplot(very.high ~ Dest_idx,data=final)

	# Surface by class and dest index
	resdf<-data.frame(res)
	
	di.surface<-array(-999,dim=c(5,5))
	
	for (i in 1:5){
		temp<-subset(resdf,Dest_idx==i-1)
		di.surface[i,]<-colSums(temp)[3:n]*25*25/(10^6)		
	}

	# --- RESULT ---- Surface per defrost class in each Destabilization index
	rownames(di.surface)<-c("DI = 0","DI = 1","DI = 2","DI = 3","DI = 4")



########################################################################

#	Step 6 - Stats for article 



# 6.1 - Number of destabiised RGs, geology

rsaga.geoprocessor("shapes_points",10, list(INPUT=invC,OUTPUT="invC_geol.shp",POLYGONS=geol,FIELDS="id"),env=myenv)

invc<-data.frame(readOGR(dsn=SAGAWD,layer="invC_geol"))

keeps <- c("Dest_rate","id")
temp<-invc[,keeps]
x<-table(temp)
as.numeric(rowSums(x))

invc$geol<-as.numeric(as.character(invc$id))
resgeol<-array(-999,dim=c(5,length(unique(invc$geol))))

par(mfrow=c(2,3))
for (i in 1:5){
	temp<-subset(invc,Dest_Idx_2==i-1)
	pie(count(as.numeric(as.character(temp$id)))$freq,labels=as.character(count(as.numeric(as.character(temp$id)))$x))
	
	for (j in 1:length(unique(invc$geol))){
		temp2<-subset(temp,geol==j)
		resgeol[i,j]<-nrow(temp2)
	}
}

colnames(resgeol)=c("ophiolites","schist","sandstone","mica-schist","gneiss","granite","limestone","basalt")

# 6.2 - Number of destabilized rockg per idx

invc$idnum<-as.numeric(as.character(invc$Dest_Idx_2))
count(invc$idnum>1)
count(invc$idnum==1)
count(invc$idnum==2)
count(invc$idnum==3)
count(invc$idnum==4)




# 1 - Get the table that answer the question : which surface disturbance occur per rock glacier 
#	in relation to their destabilization index?
# 	This part of the code counts how many RGs have a surface disturbance and 
#	relate it to the dest_index
# 	results are saved as table "in counts", giving the percentage of RG dest_index
#	showing a certain surface disturbance

# Convert shapefiles to points
rsaga.geoprocessor("shapes_polygons",6,list(SHAPES=clusters,POINTS="points_clusters.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",5,list(LINES=cracks,POINTS="points_scars.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",5,list(LINES=scarps,POINTS="points_scarps.shp"),env=myenv)
rsaga.geoprocessor("shapes_points",5,list(LINES=crevasses,POINTS="points_crevasses.shp"),env=myenv)


# Stats for layer 
name.series<-c("points_scarps","points_clusters","points_scars","points_crevasses")
counts<-array(-999,dim=c(5,length(name.series)))
colnames(counts)=name.series
for (j in 1:length(name.series)){
	layer.points<-readOGR(dsn=SAGAWD,layer=name.series[j])
	res<-over(layer.points,inv_a)
	restable<-data.frame(table(res$ID_complet))
	restable$ID_Complet<-restable$Var1
	test<-merge(restable,invc,by.x="ID_Complet",by.y="ID_complet")
	test.positive<-subset(test,Freq>0)

	for (i in 1:4){
		counts[[i,j]]<-nrow(subset(test.positive,idnum==i))
	}
	counts[[5,j]]<-nrow(test.positive)
}


keeps=c("ID_Complet","Dest_Idx_2")
aux<-test.positive[,keeps]

############################"

# Figure as Rudy

brvarP=c(0,0.4,0.95,1) # breaks of the variable (here dPFI)
brvarD=c(0,2400,2600,2700,2800,2900,3000,4000) # breaks of the variable (here DEM25)

countP<-array(-9999,dim=c(length(as.matrix(breaks))-1,length(brvarP)-1))
countD<-array(-9999,dim=c(length(as.matrix(breaks))-1,length(brvarD)-1))


for (i in 1:length(breaks)-1){
	temp<-subset(p,defrost<as.matrix(breaks)[i+1] & defrost>as.matrix(breaks)[i])
	for (j in 1:length(brvarP)-1){
		temp2<-subset(temp,dPFI<brvarP[j+1] & dPFI>brvarP[j])
		countP[i,j]<-nrow(temp2)
	}
	for (j in 1:length(brvarD)-1){
		temp2<-subset(temp,DEM25<brvarD[j+1] & DEM25>brvarD[j])
		countD[i,j]<-nrow(temp2)
	}
}


 barplot(prop.table(t(countP), 2),col=c("green","yellow","red") )
 barplot(prop.table(t(countD), 2),col=c("green","yellow","red","purple","blue","black","orange") )




