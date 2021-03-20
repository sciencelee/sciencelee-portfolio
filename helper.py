

# put all my changing info here
# gets imported into app.py

titles = {'portfolio': 'Data Science Portfolio',
          'about': 'More About Me',
          'index': "Hello, I'm Aaron Lee",
          }
messages = {'portfolio': ['Featured below are some of my recent Data Science projects.',
                          'The skills for each project are noted in the descriptions'],
          'about': ['I am a Data Scientist and Navy veteran who is passionate about STEM eduction and youth robotics mentorship.', 'See how I got here, and what skills I can bring to your business.'],
          'index': ["I am a Data Scientist with skills for most data projects: pre-processing, application of statistical methods, data visualization and results communication."],
          }

# latest projects
# each article [title, address, image]
blog_posts = [['Do Red Light Cameras Make Intersections Safe?',
               'https://towardsdatascience.com/chicago-red-light-cameras-and-traffic-safety-a6c5f08e5c4',
               'static/images/rlc_blog.png'],
              ['Do Red Light Cameras Make Intersections Safe?',
               'https://towardsdatascience.com/chicago-red-light-cameras-and-traffic-safety-a6c5f08e5c4',
               'static/images/rlc_blog.png'],
              ]

# each project [title, address, image, whet2lookfor]
projects = [['Chicago Red Light Camera Accident Study',
                'https://github.com/sciencelee/chicago_rlc',
                'static/images/rlc_project.png',
                '''Significant data engineering project which combines data from more than a dozen different sources and
                builds into a single SQLite database.  Features t-tests, Logistic Regression, Linear Regression, and Random Forest
                to build predictive and inferential models.'''],

            ['Red Light Camera Web App with Plotly Dash',
                'https://github.com/sciencelee/Red-Light-Camera-Dash-webapp',
                'static/images/RLC_webapp.png',
                '''Uses API queries to pull live data from multiple databases on Chicago Data Portal. Data visualization 
                in Plotly line/scatter/mapbox inside Dash application hosted on Heroku.'''],

            ['Pediatric X-ray classification',
                'https://github.com/sciencelee/xray-pneumonia-ML',
                'static/images/xray_project.png',
                '''Convolutional Neural Network to predict presence of pneumonia at >98% accuracy.  Model runs in google colab.'''],

            ['X-ray classification web app',
                'https://xray-pred.herokuapp.com/',
                'static/images/xray_webapp.png',
                '''Flask web application that classifies user loaded image using an h5 stored CNN model.'''],

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
                '''Significant feature engineering including addition of school districts, view features, and proximity
                to mapped locations.  Linear Regression model created with only 5 features and an r2 score of 0.70.'''],
            ]





about_title_text = "About title text"
skills = [["Programming Languages", [['Python', 4, '7+ years'],  # language, level, years
                                     ['C++', 3, '7+ years'],
                                     ['JavaScript', 2, '2 years'],
                                     ['Java', 2, '2 years'],
                                     ] ],
            ["Data Analysis", [['Data Wrangling', 4, 'Pandas, NumPy, SQL'],  # language, level, years
                                     ['Data Visualization', 4, 'Matplotlib, Plotly, Seaborn, Folium'],
                                     ['Statistics', 4, 'Inferential and Descriptive'],
                               ]
             ],

            ["Software Engineering", [['Front End', 3, 'HTML, CSS, JavaScript'],  # language, level, years
                                     ['Frameworks', 2, 'Flask, Dash, Jinja'],
                                     ['Database', 3, 'SQLite'],
                                     ['Deployment', 2, 'Heroku, Python-Anywhere, Twilio'],
                               ]
             ],

            ["Machine Learning", [['Supervised', 4, 'Classification, Regression, sklearn, statsmodel'],  # language, level, years
                                     ['Unsupervised', 3, 'CNN, K-means'],
                                     ['Deep Learning', 1, 'TensorFlow'],
                               ]
             ],

            ]