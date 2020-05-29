#install.packages('ggplot2') # visualization
#install.packages('ggthemes') # visualization
#install.packages('scales') # visualization
#install.packages('dplyr') # data manipulation
#install.packages('mice') # imputation
#install.packages('randomForest') # classification algorithm
install.packages("nnet")
install.packages("rattle")
install.packages('ggvis')

# Load packages
library('ggplot2') # visualization
library('ggthemes') # visualization
library('scales') # visualization
library('dplyr') # data manipulation
library('mice') # imputation
library('randomForest') # classification algorithm
library('nnet')
library('rattle')
library('ggvis')


mydata <- read.csv("wine.csv")
str(mydata)
summary(mydata)
sapply(mydata, sd)
head(mydata)

# there are no n.a.values
table(is.na(mydata))

# Looking at quality data - 6 categories from 3-8
# mainly of 5 or 6 quality level
table(mydata$quality)

# QUality 
# 3   4   5   6   7   8 
# 10  53 681 638 199  18 

#categories data as good and bad 3-5= bad, 6-8 = good
mydata$quality <- ifelse(mydata$quality > 5, 'Good', 'Bad')
mydata$quality <- factor (mydata$quality)
summary(mydata$quality)

#a Need to turn quality into a numeric factor
mydata$quality = as.numeric(as.factor(mydata$quality))

#a Confirm the conversion has happened
str(mydata)

# Standardize the variables
df <- scale(mydata[-1])

# Data looks quite centred between plus and mius 2
head(df)

# correlation
# In terms of quality: alcohol, suplphates and citric acid have the strongest positive correlation and 
# volatile.acidity has the highest negative correlation
res <- cor(df)
round(res, 2)


# But there is a huge st.dev scores for some variables
# check if there are a large amount ouf outliers for Total Sulphur DIoxide dur to huge St.Dev

summary(mydata$total.sulfur.dioxide)


b <- boxplot(mydata$total.sulfur.dioxide, col='green',
        main="Total Sulphur Dioxide Box plot",
        xlab="Total Sulphur Dioxide", ylab="y label", las = 1)


# check if there are a large amount ouf outliers for Free Sulphur DIoxide 
summary(mydata$free.sulfur.dioxide)


a <- boxplot(mydata$free.sulfur.dioxide, col='red',
        main="Free Sulphur Dioxide Box plot",
        xlab="Free Sulphur Dioxide", ylab="", las = 1)


################################################
##### Linear regression using all variables ####
################################################

# We see that along with the estimates, 
# many  of our observations are significant - including Total Sulfur Dioxide and 
# free sulfur dioxide
# Only the 2 acidity variables, citiric.acid, sugar and density are not significant


linearmodel = lm(quality ~ fixed.acidity+volatile.acidity+
                      citric.acid+residual.sugar+chlorides+free.sulfur.dioxide+total.sulfur.dioxide+
                      density+pH+sulphates+alcohol, data=mydata)
summary(linearmodel)


##############################################
##### K-means clustering  ####################
##############################################




# 1 Using the WSS Plot there and plotting the dataframe
# There is a distinct drop in within groups sum of squares when moving from 1- 7
# after which there is an elbow or distinct drop off.
# suggests that a 7-cluster solution might be the best fit to the data.
wssplot <- function(mydata, nc=15, seed=1234){
  wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
  for (i in 2:nc){
    set.seed(seed)
    wss[i] <- sum(kmeans(mydata, centers=i)$withinss)}
  plot(1:nc, wss, type="b", xlab="Number of Clusters",
       ylab="Within groups sum of squares")}

wssplot(df)

# 2 Running K means function  to discover the optimal no of clusters
install.packages('NbClust')
library(NbClust)
set.seed(1234)
nc <- NbClust(df, min.nc=2, max.nc=15, method="kmeans")
table(nc$Best.n[1,])

# Output states that 2 clusters might be the best. 
# 0  1  2  3  4  5  7  8 10 14 15 
# 2  1  6  2  2  3  1  4  1  1  3 

barplot(table(nc$Best.n[1,]),
        xlab="Numer of Clusters", ylab="Number of Criteria",
        main="Number of Clusters Chosen by 26 Criteria")

# 3 Final cluster solution  with kmeans() function and the cluster centroids are printed
set.seed(1234)
fit.km <- kmeans(df, 2, nstart=25)                           
fit.km$size
# output shows 1599 observations apportioned to 2 clusters
# clusters 2 being the bigger by about 50%; 
# 634 965


fit.km$centers
#4 
# The result of the confusion table shows that the clusters of the wine are not well based on all 2 quality categories
# There are too many false negative and false positives. Its not a good model

ct.km <- table(mydata$quality, fit.km$cluster)
ct.km






# 5: Adjusted rank index

# A quantified agreement between quality  and cluster, # using an adjusted Rank index from  the flexclust package
# The adjusted Rand index score is 0.1. 
# As the index ranges from -1 (no agreement) to 1 (perfect agreement) this tells us that there is only a slight agreement
# between the wine  quality type and the cluster solution.
# The model could be further refined to get a solution with higher agreement

# I could not use this model fully unsupervised to get an accurate prediction

install.packages('flexclust')
library(flexclust)

randIndex(ct.km)


####################################################
##### Logisitc regression #########################
###################################################

# Decided to create numerics 0 for bad, 1 for good. I want to predict what will be a good wine
mydata$quality <- ifelse(mydata$quality == '1', 0,1)
mydata$quality <- factor (mydata$quality)
summary(mydata$quality)



# normalisation
normalize <- function(x){
  return ( 
    (x - min(x))/(max(x) - min(x)) 
  )}

mydata_norm<- mydata
mydata_norm[,-12] <- sapply(mydata_norm[,-12], normalize)
summary(mydata_norm)


# convert quality to a factor to indicate that quality should be treated as a categorical variable.
mydata$quality <- factor(mydata$quality)

# Estimating a logistic regression model using the glm (generalized linear model) function using all variables
# Many observations are significant:
# volatile.acidity, citric.acid, chlorides, total.Sulfur.dioxide and free.sulfur.dioxide, sulphates, and alcohol

mylogit <- glm(quality ~ fixed.acidity + volatile.acidity + citric.acid + residual.sugar + chlorides +
                 +         free.sulfur.dioxide + total.sulfur.dioxide + density + pH +
                 +         sulphates + alcohol, data = mydata, family = "binomial")
summary(mylogit)

## CIs using standard errors
# Shows us that a few are crossing over from positive/negative, meaning they are not important i.e. 
# fixed.acidity, residual.sugar, free.sulfur.dioxide, density and pH    

confint(mylogit)
confint.default(mylogit)



#                         2.5 %       97.5 %
#   (Intercept)          -1.128392e+02 198.98215058
# fixed.acidity        -5.620145e-02   0.33019918
# volatile.acidity     -4.256097e+00  -2.34100218
# citric.acid          -2.385011e+00  -0.17767465
# residual.sugar       -5.073615e-02   0.16107063
# chlorides            -7.063033e+00  -0.89225374
# free.sulfur.dioxide   6.113848e-03   0.03843118
# total.sulfur.dioxide -2.215115e-02  -0.01083238
# density              -2.102836e+02 108.10847717
# pH                   -1.789297e+00   1.03622647
# sulphates             1.928803e+00   3.70238567
# alcohol               6.647308e-01   1.07342065

# run logit again without those variables mentioned
mylogit2<- glm(formula = quality ~ volatile.acidity + citric.acid + chlorides +
                 total.sulfur.dioxide + sulphates + alcohol, family = "binomial", 
               data = mydata_norm)
mylogit2

# Create a tale wih coefficients and odd ratio
data.frame(coefficient = round(coef(mylogit2),3),
           odds_ratio = round(exp(coef(mylogit2)),3))

# sulphates and alcohol level will massively increase the odds of 
# having a wine classified as good. All other variables have negligible odds
#                      
#                       coefficient odds_ratio
# (Intercept)               -0.172      0.842
# volatile.acidity          -4.814      0.008
# citric.acid               -0.540      0.583
# chlorides                 -2.458      0.086
# total.sulfur.dioxide      -3.377      0.034
# sulphates                  4.637    103.249
# alcohol                    5.742    311.820




