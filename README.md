# Fashion-recommender-System

AI Reverse Engineering Challenge Report
1. Original System: Movie Recommender System

The original system was a content-based movie recommender that used features like genre and plot descriptions to suggest similar films. While effective, it had limitations:

Domain Restriction: Limited to text-based recommendations, not applicable to other areas like fashion.
Scalability Issues: Struggled with large datasets due to reliance on algorithms like K-Nearest Neighbors.
Cold Start Problem: Difficulty providing accurate recommendations for new users or items with little data.

2. Innovation: Fashion Recommender System

I transformed this movie recommender into a Fashion Recommender System that uses advanced image recognition and similarity algorithms to recommend clothing items.

Technological Improvements:

Transfer Learning with ResNet50: Extracts detailed visual features (patterns, textures) from fashion images, enabling accurate style recommendations.





![Screenshot 2024-08-14 164432](https://github.com/user-attachments/assets/e1306ef5-4800-42f0-a2b6-34c18cc472d5)




![Screenshot 2024-08-14 164455](https://github.com/user-attachments/assets/4b6f5d62-7f73-4afb-be43-14a1a6f9426c)



Annoy Algorithm by Spotify: Replaces K-Nearest Neighbors, allowing fast, scalable similarity searches across large fashion catalogs.


Practical Applications:

E-commerce Personalization: Offers tailored recommendations, visual search, and outfit suggestions, enhancing the shopping experience.
Inventory Management: Automates the categorization of fashion items and tracks trends.
Sustainability: Promotes second-hand fashion by recommending similar pre-owned items.
Conclusion:
This transformation has broadened the original system's applicability, leveraging image-based analysis and scalable algorithms to meet the demands of the fashion industry. The upgraded system offers more precise, scalable, and practical recommendations, addressing the limitations of the previous model.
