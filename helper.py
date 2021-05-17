

# put all my changing info here
# gets imported into app.py

titles = {'portfolio': 'Data Science Portfolio',
          'about': 'More About Me',
          'index': "Hello, I'm Aaron Lee",
          'arcade': "My Arcade",
          'blog': 'My Blog'
          }
messages = {'portfolio': ['Featured below are some of my recent Data Science projects.',
                          'The skills for each project are noted in the descriptions'],
          'about': ['I am a Data Scientist and Navy veteran who is passionate about STEM education and youth robotics mentorship.',
                    "See how I got here, and what skills I can bring to your business."],
          'index': ["I am a creative and curious Data Scientist with expertise in data acquisition, data modeling, statistical analysis, machine learning, deep learning, and NLP. With a background as a Naval Officer, STEM teacher, and robotics coach, I bring strong skills in team building and project management, and can confidently communicate complex subject matter with a broad audience."],
          'arcade': ['I taught Python to high school students, and the vehicle I used was game making with the Pygame library.',
                     'Each semester, I made a gaming project right alongside my students.',
                     'Below, are a few examples of my games.  Enjoy!'],
           'blog': ['As a teacher, I enjoy reading and writing tutorial blogs.',
                    "I write for four different publications on Medium, including, '{}', '{}', and '{}'".format('The Startup', 'Towards Data Science', 'Level Up Coding')]
          }

# latest projects
# each article [title, address, image]
blog_posts = [
            ['NLP Classification Using Keras RNN/LSTM',
             'https://levelup.gitconnected.com/painless-classification-model-using-rnn-b90cb0982543',
             'static/images/rnn_project.png', 'Level Up Coding'],
            ['Baseline Accuracy',
             'https://towardsdatascience.com/calculating-a-baseline-accuracy-for-a-classification-model-a4b342ceb88f#30fd-8213094caad9',
             'static/images/baseline_blog.png', 'Towards Data Science'],
            ['Do Traffic Cameras Make Intersections Safe?',
               'https://towardsdatascience.com/chicago-red-light-cameras-and-traffic-safety-a6c5f08e5c4',
               'static/images/rlc_blog.png', 'Towards Data Science'],
            ['Geocoding with Nomantim',
               'https://levelup.gitconnected.com/simple-geocoding-in-python-fb28ee5272e0',
               'static/images/geo_blog.png', 'Level Up Coding'],
              ['Plots With Pandas Groupby',
               'https://python.plainenglish.io/making-plots-with-the-pandas-groupby-ac492941af28',
               'static/images/groupby_blog.png', 'Python in Plain English'],
              ['Deploy Predictive Model with Flask',
               'https://levelup.gitconnected.com/deploy-a-predictive-model-with-flask-33c1976293cc',
               'static/images/deploy_flask.png', 'Level Up Coding'],
            ['PySpark in Google Colab',
               'https://sciencelee.medium.com/using-pyspark-with-google-colab-8bca09c11f91',
               'static/images/pyspark_blog.png', 'Medium'],
            ['Chain Store Election Modeling',
               'https://towardsdatascience.com/are-you-a-trader-joes-democrat-or-a-walmart-republican-a7b156131435',
               'static/images/election_blog.png', 'Towards Data Science'],
            ['Folium Maps (Housing)',
               'https://levelup.gitconnected.com/visualizing-housing-data-with-folium-maps-4718ed3452c2',
               'static/images/folium_blog.png', 'Level Up Coding'],
            ['Boruta Feature Selection',
               'https://towardsdatascience.com/simple-example-using-boruta-feature-selection-in-python-8b96925d5d7a',
               'static/images/boruta_blog.png', 'Towards Data Science'],
            ['Folium Maps (Earthquakes)',
               'https://levelup.gitconnected.com/plotting-usgs-earthquake-data-with-folium-8f11ddc21950',
               'static/images/earthquake_blog.png', 'Level Up Coding'],
            ['Multivariate Linear Regression',
               'https://medium.com/swlh/multivariable-linear-regression-basics-62425ac4eafa',
               'static/images/linreg_blog.png', 'The Startup'],
              ]

# each project [title, address, image, whet2lookfor]
projects = [['Chicago Red Light Camera Accident Study',
                'https://github.com/sciencelee/chicago_rlc',
                'static/images/rlc_project.png',
                '''Significant data engineering project which combines data from more nine different sources and builds them into a single SQLite database.  Features t-tests, Logistic Regression, Linear Regression, and Random Forest to build predictive and inferential models.'''],

            ['Pediatric X-ray classification',
                'https://github.com/sciencelee/xray-pneumonia-ML',
                'static/images/xray_project.png',
                '''Convolutional Neural Network to predict presence of pneumonia at >98% accuracy.  Model runs in google colab.'''],

            ['Red Light Camera Web App (Plotly Dash)',
                'https://rlc.sciencelee.com/',
                'static/images/RLC_webapp.png',
                '''Uses API queries to pull live data from multiple databases on Chicago Data Portal. Data visualizations in Plotly line/scatter/mapbox inside Dash application hosted on Heroku.  Explore 150+ intersections and more than 8,000 red light crashes in an easy to use map.'''],

            ['FIRST Tech Challenge Team Maps Web App (Plotly Dash)',
                'http://ftcapp.sciencelee.com//',
                'static/images/ftc-app.png',
                '''I have coached robotics teams hundreds of robotics students since 2008.
                One of the competitions I have coached is FIRST Tech Challenge (FTC).  
                This dashboard web application uses API queries from The Orange Alliance (theorangealliance.com/api). 
                Maps are made in Plotly scatter_mapbox/geo_scatter/chorpletch within a Dash application hosted on Heroku.  
                Explore high score data for city, state, and country for over 3000 teams and 75k matches worldwide.'''],

            ['X-ray Classification Web App',
                'https://xray.sciencelee.com/',
                'static/images/xray_webapp.png',
                '''Flask web application that classifies user loaded image using an h5 stored CNN model hosted on Heroku.'''],

            ['Chain Store Voting Habits',
                'https://github.com/sciencelee/chainstore-election-model',
                'static/images/vote_project.png',
                '''Significant data engineering to combine 2018 congressional election results with state and county information, 
                combined with the presence of more than 20 store chains including: Starbucks, Target, Cracker Barrel, WalMart etc.  
                Web scraping with Beautiful Soup was used to get many store locations.  GeoPandas used to place stores inside voting
                districts.  XGBoost and Random Forest models used to predict party voting habits by presence of stores at > 70% accuracy.  
                Use of Folium and Mapbox with Plotly.'''],

            ['King County Housing Model',
                'https://github.com/sciencelee/seattle-housing-model',
                'static/images/king_project.png',
                '''Significant feature engineering including addition of school districts and other proximity features
                to mapped locations.  A linear Regression model created with only 5 features and an r2 score of 0.70'''],

            ['Twitter Sentiment Evaluator',
                'https://github.com/sciencelee/twitter-sentiment-evaluator',
                'static/images/twitter_project.png',
                '''Features Natural Language Processing with nltk, GloVe vectors, and a data set of labeled twitter reviews on Apple and Google Products'''],
            ]



# Arcade games
games = [['Blasteroids',
                'https://sciencelee.trinket.io/sites/sciencelee-blasteroids',
                'static/images/blasteroids.png',
                '''Fun "Asteroids" style shooter with a few twists.  
                Made with primitive shapes and lots of classes and trigonometry.  
                I aimed for fast processing and low resources on this game.
                The physics with the force shield make this a blast to play.  I love this game.  Takes about 10 seconds to load.
                 '''],

         ['Word Jumble',
          'https://sciencelee.trinket.io/sites/word-jumble',
          'static/images/word_jumble.png',
          '''"Boggle" style word game.  
          Spell as many words as you can in the time limit from the available letters.
          Earn bonus points and time for big scrabble score words.
          This project features a binary dictionary lookup, and a lot of debugging and tuning. 
          Warning: can be addictive!  May take a few seconds to load.
           '''],

    ['Missile Defense',
          'https://sciencelee.trinket.io/sites/mirv',
          'static/images/mirv.png',
          '''"Missile Command" style defense game.  
          I made this during first full year as a CS teacher, and set it up as a Raspberry Pi arcade game in my classroom.
          This game gets wild pretty quickly.
           '''],

    ['Tank Wars',
          'https://sciencelee.trinket.io/sites/tank_wars',
          'static/images/tanks.png',
          '''"Two player tank battle.  
          Head to head on the keyboard.  First to 10 wins.  Look out for lots of powerups!
        '''],

         ]




about_title_text = "About title text"
skills = [["Programming Languages", [['Python', 4, '7+ years'],  # language, level, years
                                     ['C++', 1, '7+ years'],
                                     ['JavaScript', 1, '2 years'],
                                     ['Java', 1, '2 years'],
                                     ] ],
            ["Data Analysis", [['Data Wrangling', 4, 'Pandas, NumPy, SQL'],  # language, level, years
                                     ['Data Visualization', 4, 'Matplotlib, Plotly, Seaborn, Folium'],
                                     ['Statistics', 4, 'Inferential and Descriptive'],
                               ]
             ],

            ["Software Engineering", [['Front End', 3, 'HTML, CSS, JavaScript'],  # language, level, years
                                     ['Frameworks', 2, 'Flask, Dash, Jinja'],
                                     ['Database', 3, 'SQLite, MongoDB'],
                                     ['Deployment', 2, 'Heroku, Python-Anywhere, Twilio'],
                               ]
             ],

            ["Machine Learning", [['Supervised', 4, 'Classification, Regression, sklearn, statsmodel'],  # language, level, years
                                     ['Unsupervised', 3, 'Clustering, PCA'],
                                     ['Deep Learning', 2, 'CNN, RNN, TensorFlow'],
                               ]
             ],

            ]