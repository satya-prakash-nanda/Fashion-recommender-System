# Fashion-recommender-System

## AI Reverse Engineering Challenge Report

### 1. Original System: Movie Recommender System

The original system was a content-based movie recommender that used features like genre and plot descriptions to suggest similar films. While effective, it had limitations:

Domain Restriction: Limited to text-based recommendations, not applicable to other areas like fashion.

Scalability Issues: As the movie dataset grows, the system may face challenges in processing and comparing the increasing number of movie descriptions, potentially leading to slower recommendation generation.

Cold Start Problem: The system struggles to recommend movies for new users or films with limited data since it relies heavily on user history and detailed descriptions to generate recommendations.

Overemphasis on Textual Data: The use of Count Vectorizer and Porter Stemmer focuses solely on textual analysis, which means the system might miss out on other important factors like user ratings, cast popularity, or visual aspects of the movies.

### 2. Innovation: Fashion Recommender System

I transformed this movie recommender into a Fashion Recommender System that uses advanced image recognition and similarity algorithms to recommend clothing items.

#### Technological Improvements: 

Transfer Learning with ResNet50: Extracts detailed visual features (patterns, textures) from fashion images, enabling accurate style recommendations.





![Screenshot 2024-08-14 164432](https://github.com/user-attachments/assets/e1306ef5-4800-42f0-a2b6-34c18cc472d5)




![Screenshot 2024-08-14 165749](https://github.com/user-attachments/assets/7779cc99-8077-411a-b694-09f225ca9eab)




Annoy Algorithm by Spotify: Replaces K-Nearest Neighbors, allowing fast, scalable similarity searches across large fashion catalogs.


![Screenshot 2024-08-14 164540](https://github.com/user-attachments/assets/9c2d6147-eea2-4ad8-b8b7-a806f0c498a7)


![Screenshot 2024-08-14 164551](https://github.com/user-attachments/assets/745ac311-4196-4be6-b444-f96f24801d5b)

#### Practical Applications:

E-commerce Personalization: Offers tailored recommendations, visual search, and outfit suggestions, enhancing the shopping experience.

Inventory Management: Automates the categorization of fashion items and tracks trends.

Sustainability: Promotes second-hand fashion by recommending similar pre-owned items.

#### Conclusion:

This transformation has broadened the original system's applicability, leveraging image-based analysis and scalable algorithms to meet the demands of the fashion industry. The upgraded system offers more precise, scalable, and practical recommendations, addressing the limitations of the previous model.
