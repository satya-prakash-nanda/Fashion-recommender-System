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

#### Transfer Learning with ResNet50:

Advanced Visual Feature Extraction: ResNet50, a deep convolutional neural network pre-trained on ImageNet, was employed to extract detailed visual features from fashion images. This model excels at identifying intricate patterns, textures, and colors, making it ideal for understanding the visual nuances of fashion items.

Adaptability Across Fashion Categories: ResNet50 enables the system to be quickly adapted to various fashion categories, whether clothing, footwear, or accessories. The network’s deep layers allow for capturing complex visual hierarchies, which are crucial for making accurate fashion recommendations.



![Screenshot 2024-08-14 164432](https://github.com/user-attachments/assets/e1306ef5-4800-42f0-a2b6-34c18cc472d5)




![Screenshot 2024-08-14 165749](https://github.com/user-attachments/assets/7779cc99-8077-411a-b694-09f225ca9eab)




#### Annoy Algorithm by Spotify:

Efficient High-Dimensional Similarity Search: The Annoy algorithm (Approximate Nearest Neighbors Oh Yeah) was integrated to replace KNN. Annoy is specifically designed for fast and scalable nearest-neighbor searches in high-dimensional spaces, making it ideal for handling large-scale fashion image datasets.

Scalability and Speed: Unlike KNN, Annoy can efficiently manage millions of images, ensuring that the system remains responsive even as the dataset grows. It is particularly useful in scenarios requiring real-time recommendations, such as e-commerce platforms.

Approximate Nearest Neighbors: While Annoy sacrifices some precision for speed, this trade-off is beneficial in large-scale environments where performance is critical. The slight loss in precision is often imperceptible in practical applications but significantly boosts the system’s ability to scale.


![Screenshot 2024-08-14 164540](https://github.com/user-attachments/assets/9c2d6147-eea2-4ad8-b8b7-a806f0c498a7)


![Screenshot 2024-08-14 164551](https://github.com/user-attachments/assets/745ac311-4196-4be6-b444-f96f24801d5b)

#### Practical Applications:

E-commerce Personalization: Offers tailored recommendations, visual search, and outfit suggestions, enhancing the shopping experience.

Inventory Management: Automates the categorization of fashion items and tracks trends.

Sustainability: Promotes second-hand fashion by recommending similar pre-owned items.

#### Conclusion:

This transformation has broadened the original system's applicability, leveraging image-based analysis and scalable algorithms to meet the demands of the fashion industry. The upgraded system offers more precise, scalable, and practical recommendations, addressing the limitations of the previous model.
