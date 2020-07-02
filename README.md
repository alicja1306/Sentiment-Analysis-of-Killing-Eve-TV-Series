# Sentiment Analysis of Killing Eve TV Series 

Tools: beautifulsoup, selenium, pandas, plotly, nltk, scikit-learn

Performed web scraping to extract reviews of popular tv series to predict their polarity using lexicon-based approaches (TextBlob, VADER) and machine learning classifiers such as Naive Bayes, SVM, and Logistic Regression while dealing with imbalanced data. 

1. Implemented web scraper using BeautifulSoup and selenium to fetch reviews from IMDB and Rotten Tomatoes websites. 
2. Conducted data pre-processing and cleaning by removing stop words, punctuation, numbers and detected language of each review.
3. Visualized data using word clouds and barplots.
4. Calculated sentiment score of each review by comparing it’s tokens with positive and negative lexicon. 