# ML Entry Workshop: Building Your Own Tinder Model 🚀

Welcome to the Machine Learning Entry Workshop! This workshop is designed to introduce beginners to the fundamentals of machine learning through a fun, practical project: building a model that learns your personal photo preferences, similar to a dating app.

## Workshop Overview

In this hands-on workshop, you will:

1. Learn core machine learning concepts (supervised learning)
2. Create your own dataset by rating photos
3. Prepare data for model training
4. Train a CNN model to predict your preferences
5. Evaluate model performance

## Getting Started

### Prerequisites

- Basic understanding of Python
- Curiosity about machine learning

### Setup Instructions

1. Install uv (package manager):
   ```
   brew install uv
   ```

2. Clone this repository:
   ```
   git clone git@github.com:zaichyk/ml-entry-workshop.git
   ```

3. Navigate to the repo and install dependencies:
   ```
   cd ml-entry-workshop
   uv sync
   ```

4. Open the workshop notebook:
   ```
   cd ml_entry_workshop
   jupyter notebook workshop_notebook.ipynb
   ```

## Workshop Structure

### 1. Introduction to Machine Learning
- Types of machine learning
- When to use ML
- Core ML components: Data, Hypothesis Class, Learning Algorithm

### 2. Creating Your Dataset
- Using the Photo Rater app to collect your preferences
- Running the app: `uv run photo-rater.py` in the `ml_entry_workshop/photo_rater` directory
- Rating photos (like/dislike) to build your personal dataset

### 3. Data Preparation
- Splitting data into train/validation/test sets
- Understanding the importance of data in ML
- Preprocessing images for the model

### 4. Model Training
- Using a pre-trained CNN (MobileNetV2)
- Understanding loss functions and optimization
- Training with PyTorch

### 5. Evaluation & Next Steps
- Assessing model performance
- Ways to improve your model
- Further learning resources

## Key Takeaways

- **Data is Essential**: The quality and quantity of your data directly impact model performance
- **Supervised Learning**: Learning from labeled examples is the foundation of many ML applications
- **End-to-End Project**: Experience the complete ML workflow from data collection to model training

## Contributors

- Workshop created by [Hanan Zaichyk](https://github.com/zaichyk)