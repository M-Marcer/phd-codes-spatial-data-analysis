#############################################################
# MODEL MAIN SCRIPT							#
#										#
#										#	
# Created 27/01/2016							#
#############################################################

#############################################################
# 0. SET UP									#
#############################################################

# 0.1 Libraries

 	# Mapping Libraries     
 
	library(rgdal)
	library(RSAGA)
	library(sp)
	library(raster)
	library(rgeos)
	library(spatstat)    
	library(maptools)
	library(sperrorest)

 	library(geoR)
	library(ncf)
	library(fields)

	# Model Libraries

	library(gam)
	library(aod)
	library(ggplot2)
	library(mgcv)
	library(pROC)
	library(ROCR)
	library(sperrorest)

# 0.2 Working Directories

  root = "D:/Marcer_Materials"

	# Set R Working Directory
	wd<-paste(root,"codes",sep="/")
	setwd(wd)
	
	# RSAGA working environment
	SAGAWD=paste(wd,"SAGAWD",sep='/')
	myenv<-rsaga.env(workspace=SAGAWD,path=paste(wd,"saga_2.2.2_x64/saga_2.2.2_x64",sep="/"))
	
	# GRID DATABASE DATA FOLDER
	GINPUT=paste(root,"data/grids",sep="/")

	# SHAPES DATABASE DATA FOLDER
	SINPUT=paste(root,"data/shapes/PFI_data",sep="/")

	# OUTPUT DATA FOLDER
	OUTPUT=paste(wd,"RESULTS",sep="/")

	# MODELING ENVIRONMENT/French Alps
	ME=paste(wd,"Modeling_Environment",sep="/")

############################################################

# PART 1 - IMPORT VARIABLES AND SAMPLING

#	1 . 1 - Define Variables
		
		# Dependent Variables
		
		PA="P1_poly"
		FI="P0_poly"

		# GRID Predictors 		
		DEM=paste(GINPUT,"DEM25.tif",sep='/')
		PISR=paste(GINPUT,"PISR25.tif",sep='/')
		MAAT=paste(GINPUT,"MAAT25.sgrd",sep='/')
		
		# SHAPE Predictors
		MASSIF=paste(SINPUT,"Groups.shp",sep='/')	
		GEOL=paste(SINPUT,"Lithology_BRGM_1000000.shp",sep='/')	
		
		# EDF Seasonal Winter Snow Pattern
		MWvsTW=paste(GINPUT,"MWvsTW.tif",sep='/')
		LWvsTW=paste(GINPUT,"LWvsTW.tif",sep='/')		

#	1 . 2 - Define Sampling Points
#			Here sample rock glaciers that have been identified as proper to modeling. 

		# Preapre P1 --  All Active Production Areas
#			When uncertainty == 1 then the Active rock glacier has been identified as mooving on IGN
#			When uncertainty == 2 then the Active rock glacier has geomoorphological evidences of movements, although it could have not been observed
	
		temp<-readOGR(dsn=SINPUT,layer=PA)
		temp<-subset(temp,Uncrtnt>0)    
		writeOGR(temp,dsn=SAGAWD,layer="temp",driver="ESRI Shapefile",overwrite_layer=T)
		rsaga.geoprocessor("shapes_polygons",1,list(POLYGONS="temp.shp",CENTROIDS="P1.shp"),env=myenv)  # P(pF|Rg)=1
	
		# Prepare P0 -- Well shaped and monorphic fossil rock glaciers with PA
		temp<-readOGR(dsn=SINPUT,layer=FI)
		temp<-subset(temp,PA>0)			
		writeOGR(temp,dsn=SAGAWD,layer="temp",driver="ESRI Shapefile",overwrite_layer=T)
		rsaga.geoprocessor("shapes_polygons",1,list(POLYGONS="temp.shp",CENTROIDS="P0.shp"),env=myenv)  # P(pF|Rg)=0

		
#	1 . 3 - Sample Grids

		 # Get coordinates
		rsaga.geoprocessor("shapes_points",6,list(INPUT="P1.shp",OUTPUT="P1.shp"),env=myenv)
		rsaga.geoprocessor("shapes_points",6,list(INPUT="P0.shp",OUTPUT="P0.shp"),env=myenv)

		# Sample Grids
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P1.shp",GRIDS=MAAT,RESULT="P1.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P1.shp",GRIDS=DEM,RESULT="P1.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P1.shp",GRIDS=PISR,RESULT="P1.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P1.shp",GRIDS=MWvsTW,RESULT="P1.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P1.shp",GRIDS=LWvsTW,RESULT="P1.shp"),env=myenv)

		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P0.shp",GRIDS=MAAT,RESULT="P0.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P0.shp",GRIDS=DEM,RESULT="P0.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P0.shp",GRIDS=PISR,RESULT="P0.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P0.shp",GRIDS=MWvsTW,RESULT="P0.shp"),env=myenv)
		rsaga.geoprocessor("shapes_grid",0,list(SHAPES="P0.shp",GRIDS=LWvsTW,RESULT="P0.shp"),env=myenv)

		# Sample Massif Shapes
		rsaga.geoprocessor("shapes_points",10,list(INPUT="P1.shp",POLYGONS=MASSIF,FIELDS="Group",OUTPUT="P1.shp"),env=myenv)
		rsaga.geoprocessor("shapes_points",10,list(INPUT="P0.shp",POLYGONS=MASSIF,FIELDS="Group",OUTPUT="P0.shp"),env=myenv)

		# Sample Geology Shapes
		rsaga.geoprocessor("shapes_points",10,list(INPUT="P1.shp",POLYGONS=GEOL,FIELDS="GEOL_ID",OUTPUT="P1.shp"),env=myenv)
		rsaga.geoprocessor("shapes_points",10,list(INPUT="P0.shp",POLYGONS=GEOL,FIELDS="GEOL_ID",OUTPUT="P0.shp"),env=myenv)

#####	1 . 4 - Create DataBase for modeling (IF SAMPLING ALREADY SAVED, START FROM HERE)
#		  CAREFUL! here it depends on the number of predictors!

		P0<-readOGR(dsn=SAGAWD,layer="P0")
		P1f<-readOGR(dsn=SAGAWD,layer="P1")

		#P1=P1f	
		#S<-sprintf("\n \n##############################################\n Working on UC=2,1 \n #############################")
		#write(S,file="results.txt",append=TRUE,ncolumns=1)

		P1<-subset(P1f,Uncrtnt==1)  # Select only moving rock glaciers
		#S<-sprintf("\n \n##############################################\n Working on UC=1 \n #############################")
		#write(S,file="results.txt",append=TRUE,ncolumns=1)

		DB<-matrix(c(P1$X,	P0$X,
				P1$Y,		P0$Y,
				P1$MAAT25,	P0$MAAT25,
				P1$PISR25,	P0$PISR25,
				P1$DEM25,	P0$DEM25,
				P1$Group,	P0$Group,
				P1$MWvsTW,	P0$MWvsTW,
				P1$LWvsTW,	P0$LWvsTW,
				P1$GEOL_ID,	P0$GEOL_ID),ncol=9)
		
		colnames(DB)<-c("x","y","MAAT25","PISR25","DEM25","Group","MWvsTW","LWvsTW","geol")
		DB<-data.frame(DB)

		# Add Factor Variables
		
		DB$GROUP<-factor(DB$Group)

		v0<-rep(0,length(P0$X))
		v1<-rep(1,length(P1$X))						
		DB$P=factor(c(v1,v0))	

		DB<-subset(DB,PISR25>0)

		DB$GROUP2<-as.numeric(DB$GROUP)+1
		idx<-which(DB$GROUP2==6)
		for (i in 1:length(idx)){
			DB$GROUP2[idx[i]]=1
			}
		
		# Putting proper geology groups
		DB$geoln<-as.numeric(DB$geol)

		for (i in 1:length(DB$geoln)){
			if  (DB$geoln[[i]]==5 || DB$geoln[[i]]==6){
				DB$geolf[[i]]=1}
			else{
				DB$geolf[[i]]=0}
			}
		DB$geolF<-factor(DB$geolf)

		DB_U2<-DB
		DB_U1<-DB
############################################################

# PART 2 - INDEPENDENT VARIABLES ANALYSIS
	plot(DB)

#	2 . 1 - Boxplot by group

	plot(DB$x,DB$y,col=c("red","blue","green","orange","black")[DB$GROUP],pch=20)
	legend(x="topright",legend=levels(DB$GROUP),col=c("red","blue","green","orange","black"),pch=20)

	par(mfrow=c(2,2))
	boxplot(PISR25~P*GROUP2,data=DB,col=(c("green","red")),xlab="Group",ylab="PISR")
	boxplot(MAAT25~P*GROUP2,data=DB,col=(c("green","red")),xlab="Group",ylab="MAAT")
	boxplot(MWvsTW~P*GROUP2,data=DB,col=(c("green","red")),xlab="Group",ylab="MWvsTW")
	boxplot(LWvsTW~P*GROUP2,data=DB,col=(c("green","red")),xlab="Group",ylab="LWvsTW")
#	
	pie(table(DB$GROUP2))	

# Compare Moving and Not moving RGs

	par(mfrow=c(2,2))
	plot(P1,pch=21)
	points(P1f,pch-3)

	hist(P1f$PISR25,col="yellow",20)
	hist(P1$PISR25,col="red",add=T,20)

	hist(P1f$MAAT25,col="yellow",20)
	hist(P1$MAAT25,col="red",add=T,20)

	hist(P1f$Y,col="yellow",20)
	hist(P1$Y,col="red",add=T,20)


############################################################

# PART 3 - MODEL SELECTION 

	ETAB=list()   # Initialize Table of perfomances
	stats=list()
	
	# Define the models to be tested
	F=list()
	F[[1]]=P~MAAT25+PISR25
	F[[2]]=P~MAAT25+PISR25+y
	F[[3]]=P~MAAT25+PISR25+y+x
	F[[4]]=P~MAAT25+PISR25+MWvsTW
	F[[5]]=P~MAAT25+PISR25+LWvsTW
	F[[5]]=P~DEM25+PISR25+y+x
	F[[6]]=P~DEM25+PISR25+y
	F[[7]]=P~DEM25+PISR25+y+geolF

for (mdlid in 5:(length(F)))
{
	mdl<-glm(F[[mdlid]],data=DB,family=binomial)									# Train Model GLM
	temp<-as.numeric(predict.glm(mdl,data=DB,type="response"))							# Prediction (for the err.default AUROC

	# Write Model Name to file
	s<-Reduce(paste,deparse(F[[mdlid]]))
	S<-sprintf("\n \n##############################################\n Model  :  %s\n",s)
	write(S,file="results.txt",append=TRUE,ncolumns=1)

	# Wirte non cross validated model AUROC and AIC to file
	AUROC<-err.default(DB$P,temp)$auroc
	AIC<-AIC(mdl)
	mstats=data.frame(c(AUROC,AIC))
	rownames(mstats)=c("AUROC","AIC")
	colnames(mstats)=c("")
	S<-sprintf("\n \nNon Cross Validated Model Performance \n")
	write(S,file="results.txt",append=TRUE,ncolumns=1)	
	write.table(mstats,file="results.txt",append=TRUE,sep=" ")

	# Wirte model predictors coefficients to file
	pstat<-summary(mdl)$coefficients	 #Get coefficients
	S<-sprintf("\n \nNon Cross Validated Model Predictors \n")
	write(S,file="results.txt",append=TRUE,ncolumns=1)	
	capture.output(pstat,file="results.txt",append=TRUE)								# Write coefficients to file,append=TRUE


	mypred = function(object,newdata) as.vector(predict.glm(object,newdata,type="response"))		# Create prediction function object

	# Cross Validation by Groups

	S<-sprintf("\n \nGroup-Cross Validated Model Performances \n")
	write(S,file="results.txt",append=TRUE,ncolumns=1)
	for (i in 1:5)
	{
	DB$CGROUP<-DB$GROUP==i
	spres = sperrorest(data = DB, formula = F[[mdlid]],
   			model.fun = glm, model.args = list(family = binomial),
			pred.fun=mypred,
    			smp.fun = partition.factor, smp.args = list(repetition=1, fac="CGROUP"),
    			err.pooled = TRUE, err.unpooled = TRUE, err.fun = err.default)
	tstat<- summary(spres$error,level=1)
	stats[[i]]<-c(tstat$train.auroc[[1]],tstat$test.auroc[[1]],tstat$train.count[[1]],tstat$test.count[[1]])

	}
	l<-data.frame(matrix(unlist(stats),nrow=5,byrow=T))
	colnames(l)<-c("Training AUROC","Test AUROC","Training size","Test size")
	rownames(l)<-c("Group 1","Group 2","Group 3","Group 4","Group 5")
	write.table(l,file="results.txt",append=TRUE,sep="   ")
	
	# Get 10 k fold AUROCcv
	spres = sperrorest(data = DB, formula = F[[mdlid]],
   			model.fun = glm, model.args = list(family = binomial),
			pred.fun=mypred,
    			smp.fun = partition.cv, smp.args = list(repetition=1:5, nfold=10),
    			err.pooled = TRUE, err.unpooled = TRUE, err.fun = err.default)

	l<-data.frame(summary(spres$pooled.error)$mean[[1]],summary(spres$pooled.error)$mean[[14]])
	colnames(l)<-c("Train 10-kfold AUROCcv","Test 10-kfold AUROCcv")
	write.table(l,file="results.txt",append=TRUE,sep="   ")

	#Get partition k-means cross validation
	spres = sperrorest(data = DB, formula = F[[mdlid]],
   			model.fun = glm, model.args = list(family = binomial),
			pred.fun=mypred,
    			smp.fun = partition.kmeans, smp.args = list(coords=matrix(c(DB$x,DB$y),ncol=2),nfold=10),
    			err.pooled = TRUE, err.unpooled = TRUE, err.fun = err.default)
	
	l<-data.frame(summary(spres$pooled.error)$mean[[1]],summary(spres$pooled.error)$mean[[14]])
	colnames(l)<-c("Train 10-kmeans AUROCcv","Test 10-kmeans AUROCcv")
	write.table(l,file="results.txt",append=TRUE,sep="   ")

	#Get group partition cross validation
	spres = sperrorest(data = DB, formula = F[[mdlid]],
   			model.fun = glm, model.args = list(family = binomial),
			pred.fun=mypred,
    			smp.fun = partition.factor, smp.args = list(repetition=1,fac="GROUP"),
    			err.pooled = TRUE, err.unpooled = TRUE, err.fun = err.default)
	
	l<-data.frame(summary(spres$pooled.error)$mean[[1]],summary(spres$pooled.error)$mean[[14]])
	colnames(l)<-c("Train group factor AUROCcv","Test group factor AUROCcv")
	write.table(l,file="results.txt",append=TRUE,sep="   ")
}

# Go through the File and select your models to inspect residuals

	finalMdl=list()

	finalMdl[[1]]=P~DEM25+PISR25+y+geolF
	
	par(mfrow=c(1,2))

#	for (i in 1:length(finalMdl))
	for (i in 1)
	{
	mdl=glm(finalMdl[[i]],data=DB,family=binomial)
	summary(mdl)
	temp<-as.numeric(predict.glm(mdl,data=DB,type="response"))							# Prediction (for the err.default AUROC
	AUROC<-err.default(DB$P,temp)$auroc
	#AIC<-AIC(mdl)
	residuals<-temp-(as.numeric(DB$P)-1)
	DB$residuals<-residuals
	plot(DB$x,DB$y,cex=abs(DB$residuals*5),col=DB$P)
	legend(7,4.3,unique(DB$P),col=1:length(DB$P),pch=1)
	t<-as.character(finalMdl[[i]])
	title(main=t[3])
	legend(x="topright",legend=levels(DB$P),col=c("green","red"),pch=1)
	}

	# Evaluate ODDS RATIO
	logit2prob <- function(logit){
  	odds <- exp(logit)
  	prob <- odds / (1 + odds)
  	return(prob)
	}
	exp(coef(mdl))
	logit2prob(coef(mdl))

	# Write final Dataframe to shapefile
	db<-data.frame(DB)
	coordinates(db)=~x+y
	rs<-proj4string(P1)	# get CRS
	proj4string(db)=rs
	writeOGR(db,dsn=SAGAWD,layer=DB,driver="ESRI Shapefile",overwrite_layer=T)

	write.table(DB,file="DATABASE_.csv")


############################################################

# PART 4 - MODEL UNCERTAINTY

# The users' excercise gave the following values in uncertainty, evaluated as differences between users:
# 		-  MAAT :  max(MAAT) = 0.37 , MEAN(MAAT) ~ 0  SD(MAAT) = 0.11
#		-  PISR :  max(PISR)=167.69 , MEAN(PISR) = 8.36 , SD(PISR) = 76.79
# Here we perform a Monte Carlo analysis, by randomly varying the data, assuming a normal distribution

niter=10   # Number iterations

# Uncertainties on MAAT and PISR
eMAAT<-0.11
ePISR<-76.79

# Create Matrix to map uncertainty
n=100
MAATmatrix=matrix(nrow=n,ncol=n)
PISRmatrix=MAATmatrix
MAATvec=seq(-4,4,8/(n-1))
PISRvec=seq(300,2000,(2000-300)/(n-1))
for ( i in 1:n){
	MAATmatrix[i,]=MAATvec
	PISRmatrix[,i]=PISRvec
}

# Initialize Data frame for the simulation
tempR<-data.frame(matrix(nrow=1,ncol=1))
tempR$x=965619.8
tempR$y=6357000

# Initialize Matrix to store Data
PFI=array(-9999, dim=c(niter,n,n))
values=array(-9999,dim=c(niter,7))

for (i in 1:niter)
{
	print(i)
	tempDB<-DB
	tempDB$MAAT25<-tempDB$MAAT25+rnorm(length(DB$MAAT25), mean=0, sd=eMAAT)
	tempDB$PISR25<-tempDB$PISR25+rnorm(length(DB$PISR25), mean=0, sd=ePISR)

	tempMDL<-glm(P~MAAT25+PISR25+y+x,data=tempDB,family=binomial)

	#values[i,1]=AUROC
	values[i,2]=AIC(tempMDL)
	values[i,3]=tempMDL$coefficients[1]
	values[i,4]=tempMDL$coefficients[2]
	values[i,5]=tempMDL$coefficients[3]
	values[i,6]=tempMDL$coefficients[4]
	values[i,7]=tempMDL$coefficients[5]
	
	for (j in 1:n){
		for (k in 1:n){
			tempR$MAAT25=MAATmatrix[j,k]
			tempR$PISR25=PISRmatrix[j,k]
			
			PFI[i,j,k]=predict(tempMDL,newdata=tempR,type="response")
			}
		}
}

# Evaluate Mean and sd of each cell
SD_PFI=array(-999,dim=c(n,n))
ME_PFI=array(-999,dim=c(n,n))
MX_PFI=array(-999,dim=c(n,n))


for (i in 1:n){
	for (j in 1:n){
		SD_PFI[i,j]=sd(PFI[,i,j])
		ME_PFI[i,j]=mean(PFI[,i,j])
		MX_PFI[i,j]=(max(PFI[,i,j])-min(PFI[,i,j]))
		}
	}
par(mfrow=c(1,3))
image.plot(PISRvec,MAATvec,SD_PFI)
image.plot(PISRvec,MAATvec,ME_PFI)
image.plot(PISRvec,MAATvec,MX_PFI)

	

#########################################################################################

# PART 5 - Model Uncertainty on UAI

DB_U2   # Database with all active production areas
DB_U1	  # Database with moving active rock glaciers


# Create Matrix to map uncertainty
n=100
MAATmatrix=matrix(nrow=n,ncol=n)
PISRmatrix=MAATmatrix
MAATvec=seq(-4,4,8/(n-1))
PISRvec=seq(300,2000,(2000-300)/(n-1))
for ( i in 1:n){
	MAATmatrix[i,]=MAATvec
	PISRmatrix[,i]=PISRvec
}


PFI1=array(-9999, dim=c(n,n))
PFI2=array(-9999, dim=c(n,n))

# Initialize Data frame for the simulation
tempR<-data.frame(matrix(nrow=1,ncol=1))
#Mercantour
#tempR$x=965619.8
#tempR$y=6357000
#Vanoise
tempR$x=994000
tempR$y=6515000

mdlU1<-glm(P~MAAT25+PISR25+y+x,data=DB_U1,family=binomial)
mdlU2<-glm(P~MAAT25+PISR25+y+x,data=DB_U2,family=binomial)
	

	for (j in 1:n){
		for (k in 1:n){
			tempR$MAAT25=MAATmatrix[j,k]
			tempR$PISR25=PISRmatrix[j,k]
			
			PFI1[j,k]=predict(mdlU1,newdata=tempR,type="response")
			PFI2[j,k]=predict(mdlU2,newdata=tempR,type="response")

			}
		}

Uncertainty_PFI=abs(PFI1-PFI2)
image.plot(PISRvec,MAATvec,Uncertainty_PFI)

###################################################################################

# 6 . Evaluate Lower Limits of Possible Permafrost at the French Alps Scale

	# Initialize model
	mdl<-glm(P~MAAT25+PISR25+MWvsTW,data=DB_U1,family=binomial)

	# Import EWPR Data
	grd<-raster(paste(GINPUT,"MWvsTW.tif",sep='/'))
	grdVEC<-as.data.frame(grd)
	
	# Resolution of the simulation
	n=100
	
	demVEC<-seq(2000,3500,1500/(n-1))
	maatVEC<-seq(-4,4,8/(n-1))
	ewprVEC<-seq(0.3,0.4,0.1/(n-1))

	DEMmatrix=array(-9999,dim=c(n,n))
	MAATmatrix=DEMmatrix
	EWPRmatrix=array(-9999,dim=c(n,n))

	for ( i in 1:n){
		DEMmatrix[i,]=demVEC
		MAATmatrix[i,]=maatVEC
		EWPRmatrix[,i]=ewprVEC
	}

	# Initialize model data frame
	tempR<-data.frame(matrix(nrow=1,ncol=1))
	tempR$PISR25<-500

	# Initalize matrix to store data
	PFI=array(-999,c(n,n))
	for (j in 1:n){
		for (k in 1:n){
			tempR$DEM25=DEMmatrix[j,k]
			tempR$MWvsTW=EWPRmatrix[j,k]
			tempR$MAAT25=MAATmatrix[j,k]
			
			PFI[j,k]=predict(mdl,newdata=tempR,type="response")
			}
		}


image.plot(ewprVEC,maatVEC,PFI)

# Find the linear model for PFI = 0.6

idx<-which(PFI<0.62 & PFI>0.58)
subDEM<-DEMmatrix[idx]
subMAAT<-MAATmatrix[idx]
subEWPR<-EWPRmatrix[idx]
plot(subDEM,subEWPR)

# Fit a linear Model on the Probability and Predict using the MWvsTW Grid
mdl_PFI06<-lm(subMAAT~subEWPR)
tempgrd<-data.frame(as.numeric(grdVEC$MWvsTW))
colnames(tempgrd)<-c("subEWPR")	
prediction<-predict(mdl_PFI06,newdata=tempgrd,type="response")
MAAT_PFI06_PISR2000<-array(prediction, dim=c(ncol(grd),nrow(grd)))  # Reshape
image.plot(MAAT_PFI06_PISR2000)

r <-raster(
             t(MAAT_PFI06_PISR2000),
             xmn=xmin(grd), xmx=xmax(grd),
             ymn=ymin(grd), ymx=ymax(grd), 
             crs=crs(grd)
            )
writeRaster(r,file="MAAT_PISR06_P500.tif",overwrite=TRUE)
plot(r)

#####################################################################################

 #PART 7 - PREDICTING AT FRENCH ALPS SCALE

	# Function grid.predict Needs:

	#	1. ASC grids Inputs, same grids (need to resample over a reference)
	#	2. Grids in R working directory
	#	3. Model variable have the same name of the grids

	mdl<-glm(P~DEM25+PISR25+y,data=DB_U1,family=binomial)


	# Need to resample grids on each others). This takes long, do it once
	# Before resampling go to check what has already been reasmpled, is stored in the modeling environment

	#PISR
	rsaga.geoprocessor("grid_tools",0,list(INPUT="INPUT/PISR.asc",OUTPUT="PISR_resampled.asc",TARGET_DEFINITION=1,TARGET_TEMPLATE="INPUT/D25.asc",SCALE_DOWN=1),env=myenv)
	rsaga.sgrd.to.esri(in.sgrds="PISR_resampled.sgrd",out.grids="PISR_resampled_ASC.asc",georef="corner",env=myenv)
	
	#MAAT_G
	rsaga.sgrd.to.esri(in.sgrds=MAAT_G,out.grids="MAAT_G.asc",georef="corner",env=myenv)
	
	# Move manually the new ASC resampled files to the modeling environment to keep the stuffs clean

	# Go to the modeling environment for grid.predict function
	setwd(MEPR)
		
	modelname<-"GLM_DEM_PISR_y"
	multi.local.function(in.grids = c("DEM25","PISR25","y"),out.varnames = modelname,fun = grid.predict,control.predict=list(type="response"),fit=mdl) 

	# Go back to R environment

	setwd(wd)

###############################################################
# END
###############################################################
