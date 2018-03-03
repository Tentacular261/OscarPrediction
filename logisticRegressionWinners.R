rm(list = ls())

# Author: Joseph Savold
# Date: April 6th, 2017
# Purpose: Determine probability of oscar winner with logistic regression

# read in data from file
mydata <- read.csv("~/Documents/OscarTeam2/Movies/movies2.csv", header = TRUE, sep = ",", quote = "\"",
  dec = ".", fill = TRUE, comment.char = "")

training_data <- mydata[6:nrow(mydata),]

# checking the data
dim(mydata)
names(mydata)

attach(mydata)
summary(mydata)

head(mydata)

# convert pimdb_ratings from strings to numeric
pimdb_rating <- as.numeric(as.character(imdb_rating))
pnum_imdb_votes <- as.numeric(as.character(num_imdb_votes))
pmetascore_rating <- as.numeric(as.character(metascore_rating))
pnum_metascore_positive <- as.numeric(as.character(num_metascore_positive))
pnum_metascore_mixed <- as.numeric(as.character(num_metascore_mixed))
pnum_metascore_negative <- as.numeric(as.character(num_metascore_negative))
puserscore_rating <- as.numeric(as.character(userscore_rating))
pnum_userscore_positive <- as.numeric(as.character(num_userscore_positive))
pnum_userscore_mixed <- as.numeric(as.character(num_userscore_mixed))
pnum_userscore_negative <- as.numeric(as.character(num_userscore_negative))
pall.critics.numbers <- as.numeric(as.character(all.critics.numbers))
ptop.critics.numbers <- as.numeric(as.character(top.critics.numbers))
ptop_average_rating <- as.numeric(as.character(top_average_rating))
ptop_reviews_counted <- as.numeric(as.character(top_reviews_counted))
ptop_fresh <- as.numeric(as.character(top_fresh))
ptop_rotten <- as.numeric(as.character(top_rotten))
prt_audience_score <- as.numeric(as.character(rt_audience_score))
pwinner <- as.numeric(as.character(winner))
pbafta_winner <- as.numeric(as.character(bafta_winner))
pbafta_loser <- as.numeric(as.character(bafta_nom))
pgg_drama_nom <- as.numeric(as.character(gg_drama_nom))
pgg_drama_win <- as.numeric(as.character(gg_drama_win))
pgg_musical_nom <- as.numeric(as.character(gg_musical_nom))
pgg_musical_win <- as.numeric(as.character(gg_musical_win))

attach(training_data)

##############################
# Tests for Numeric Predictors
##############################

# do logistic regression for imdb rating
probs <- glm(pwinner ~ pimdb_rating, family = binomial)
summary(probs)

plot(pimdb_rating, pwinner,xlab="IMdB Rating",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pimdb_rating=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for metascore
probs <- glm(pwinner ~ pmetascore_rating, family = binomial)
summary(probs)

plot(pmetascore_rating, pwinner,xlab="Metascore Rating",ylab="Probability of Winning Oscar")
curve(predict(probs.meta,data.frame(pmetascore_rating=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for negative metascore
probs <- glm(pwinner ~ neg_, family = binomial)
summary(probs)

plot(pnum_metascore_negative, pwinner,xlab="Metascore Rating",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pnum_metascore_negative=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for ptop_rotten
probs <- glm(pwinner ~ ptop_rotten, family = binomial)
summary(probs)

plot(ptop_rotten, pwinner,xlab="ptop_rotten",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(ptop_rotten=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model


# do logistic regression for bafta win
probs <- glm(pwinner ~ pbafta_winner, family = binomial)
summary(probs)

plot(pbafta_winner, pwinner,xlab="pbafta_winner",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pbafta_winner=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for bafta loss
probs <- glm(pwinner ~ pbafta_loser, family = binomial)
summary(probs)

plot(pbafta_loser, pwinner,xlab="pbafta_loser",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pbafta_loser=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for gg musical nom
probs <- glm(pwinner ~ pgg_musical_nom, family = binomial)
summary(probs)

plot(pgg_musical_nom, pwinner,xlab="pgg_musical_nom",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pgg_musical_nom=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for gg musical win
probs <- glm(pwinner ~ pgg_musical_win, family = binomial)
summary(probs)

plot(pgg_musical_win, pwinner,xlab="pgg_musical_win",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pgg_musical_win=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for gg musical win
probs <- glm(pwinner ~ pgg_drama_nom, family = binomial)
summary(probs)

plot(pgg_drama_nom, pwinner,xlab="pgg_drama_nom",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pgg_drama_nom=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model

# do logistic regression for gg musical win
probs <- glm(pwinner ~ pgg_drama_win, family = binomial)
summary(probs)

plot(pgg_drama_win, pwinner,xlab="pgg_drama_nom",ylab="Probability of Winning Oscar")
curve(predict(probs,data.frame(pgg_drama_win=x),type="resp"),add=TRUE) # draws a curve based on prediction from logistic regression model


##################################################################
# Tests for Non-Numeric Predictors
##################################################################

# year test
m <- glm(pwinner ~ year, family = binomial)
summary(m)

# mpaa test
m <- glm(pwinner ~ mpaa, family = binomial)
summary(m)

# director test
m <- glm(pwinner ~ director, family = binomial)
summary(m)


##########################################
# Train Model On Multiple Predictors
##########################################

m <- glm(pwinner ~ pimdb_rating + pnum_imdb_votes + pmetascore_rating +
         + pall.critics.numbers + ptop_average_rating
         + prt_audience_score + pbafta_winner, family = binomial)
summary(m)

###################################################################
# Accuracy / Precision Calculation + Visualization (not yet adapted)
###################################################################

attach(mydata)

pred.probs <- predict (m, mydata, type = "response")
pred.pwinner <- rep("No", nrow(mydata))
pred.pwinner[pred.probs > 0.2] <- "Yes"

data.frame(name, pred.probs, pwinner, year)
write.csv(data.frame(name, pred.probs, pwinner, year), file = "~/Documents/OscarTeam2/Movies/probs_of_winning.csv")

confusion.matrix <- table(default, pred.default)
print(addmargins(confusion.matrix))

print(c("accuracy", (confusion.matrix[1,1] + confusion.matrix[2,2]) / 10000 ))
