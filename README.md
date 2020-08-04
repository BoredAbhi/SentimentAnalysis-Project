# Sentiment Analysis App 
This application is being developed as a project to implement end to end Machine Learning. Then end goal is to train a sentiment analysis app using scraped data to predict the rating for a review and deploy it in cloud. 

### Phases of the project :
#### 1. Data Collection : 
The data is being collected form [Trustpilot](https://www.trustpilot.com/). This website has a huge collection of reviews on different shops. It also has a rating for each review which will be used to train the model. Two CSV files are saved, one with links to all companies and the other with the actual rating and reviews. A total of 1.3GB of reviews were scrapped from the website.
**Tools :** Python scraping using [Selenium](https://selenium-python.readthedocs.io/) and [Scrapy](https://scrapy.org/).
#### 2. Data Cleaning :
The data is loaded into a dataframe for basic cleaning and manupulation.
#### 3. Training with CNN :
To use CNN in this case, [1D-Convolutions](https://towardsdatascience.com/understanding-1d-and-3d-convolution-neural-network-keras-9d8f76e29610) is used. The CNN will try to predict if a review is good, average or bad. The review data is feeded to the CNN and after 3 to 4 epochs ~70% accuracy is achieved for all three cases. (I did not go further as I was training on my laptop with a i5-10210U)

