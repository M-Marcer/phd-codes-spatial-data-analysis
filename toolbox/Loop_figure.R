### Code to make Figure of model runs

Loop_figure<-function(iteration_i,full_data,full_P,local_data,local_P,S,fig){
	#print(S)
	mdl<-gam(local_P~s(local_data),family=binomial)
	x<-data.frame(seq(min(local_data),max(local_data),(max(local_data)-min(local_data))/100))
	colnames(x)<-"local_data"
	y<-predict.gam(mdl,newdata=x,type="response")

	yc<-predict.gam(mdl,type="response")


	if (iteration_i==1){
		dev.new()
		plot(full_data,as.numeric(full_P)-1+runif(length(full_P),-0.03,0.03),
		type="p",pch=".",
		col=rgb(0.5,0.5,0.5,alpha=0.1),
		xlab=S,ylab="Destabilization Index")
		lines(x$local_data,y,col=rgb(0.5,0.5,0.5,alpha=0.1))
	}
	else{	
		dev.set(which=fig)
		lines(x$local_data,y,col=rgb(0.5,0.5,0.5,alpha=0.1))
	}
	OUT<-data.frame(array(-999,dim=c(101,2)))
	OUT$x<-as.numeric(x$local_data)
	OUT$y<-as.numeric(y)
	OUT$perf<-array(data.matrix(data.frame((err_default(local_P,yc))))[1],dim=c(length(OUT$x),1))
	return(OUT)
}