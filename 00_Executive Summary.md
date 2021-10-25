## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) GA Capstone: Executive Summary

### Problem Statement

Our goal with this project is to provide students with a reasonable means of being able to record themselves and predict their tone and emotion in hopes that it benefits them as they prepare for technical interviews. In this, we hope to classify emotions off of audio data and develop a web app that can be utilized by other students. 

A successful model would score higher than an average baseline metric of 12%, and we would include a fully functioning web app.

### Background

Audio has been used in prediction modeling for the better part of several years. In primary use cases, audio can function similarly to text and visual feedback in that we can derive sentiment from it. In the market, 70% of managers expect negotiations to happen at the time of the offer, while only 46% and 34% of men and women take them up on it. We are looking to provide a means for our students to be fully equipped for their next interview opportunities.

We pulled our data from RAVDESS, a dataset encompassing 1,440 files of actor-contributed snippets of audio data. This data is standardized and encompasses 8 ranges of emotions.

### Modeling

In our modeling process, we utilized a variety of audio classification features, choosing to model off of two subsets of features. One, a baseline that only involved MFCC data, the most common baseline metric for audio, while the other encompassed more features.

Our chosen model, a CNN model analyzing the MCC (Mel-frequency Cepstrum), scored 67% on our test data, which was higher than our null baseline (12% chance of guessing an emotion correctly). This model is overfitting, however, and improvements must be made to the underlying audio data and model before it is to be deployed.

Surprisingly, our baseline model performed better than our model with the additional features. However, both models tended to not be able to classify happiness and sadness to a great degree, which is the key indicator in an actual interview setting.

### Conclusions and Recommendations

To conclude, our model, while not quite ready for deployment, scores higher than our null hypothesis. Additionally, our baseline should be the primary model moving forward as we look to further improve the application.

Our next steps are as follows

- Further data augmentation, with pitch and white noise, should improve our overall model scoring.

- Adding 10,000 files from other data sources should give us better model fitting and better capabilities.

- Further developing the web app out to include real-time predictions across the entire audio file, not just a sample, should allow students a seamless experience with the app.