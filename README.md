# ML Entry Workshop: Building Your Own Tinder Model 🚀

Welcome to the Machine Learning Entry Workshop! This workshop is designed to introduce beginners to the fundamentals of machine learning through a fun, practical project: building a model that learns your personal photo preferences, similar to a dating app.

## Workshop Overview

In this hands-on workshop, you will:

1. Learn core machine learning concepts (supervised learning)
2. Understand how neural networks work and visualize their components
3. Create your own dataset by rating photos
4. Prepare data for model training
5. Train a CNN model to predict your preferences
6. Evaluate model performance with interactive tools

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

4. Activate your venv and create a new ipykernel
   ```
   source .venv/bin/activate (you are now in your uv venv)
   python -m ipykernel install --user --name=mlworkshop --display-name "Python (ML Workshop)"
   ```
   
5. Important: If you plan to work with the men's dataset, you'll need to remove images 21, 37, and 243 as they may cause errors during processing.

6. Open the workshop notebooks:
   ```
   cd ml_entry_workshop
   jupyter notebook
   ```
   Then open either `workshop_notebook.ipynb` or `What is Neural Network.ipynb`

## Workshop Structure

### 1. Introduction to Machine Learning
- Types of machine learning
- When to use ML
- Core ML components: Data, Hypothesis Class, Learning Algorithm

### 2. Neural Network Theory (What is Neural Network.ipynb)
- Visual exploration of neural network components
- Interactive visualizations of neurons, layers, and activation functions
- Understanding forward propagation and backpropagation
- Gradient descent visualization and intuition

### 3. Creating Your Dataset
- Using the Photo Rater app to collect your preferences
- Running the app: `uv run photo-rater.py` in the `ml_entry_workshop/photo_rater` directory
- Rating photos (like/dislike) to build your personal dataset
- Reviewing and adjusting your selections for a balanced dataset

### 4. Data Preparation
- Splitting data into train/validation/test sets
- Understanding the importance of data in ML
- Preprocessing images for the model

### 5. Model Training
- Using a pre-trained CNN (MobileNetV2)
- Understanding loss functions and optimization
- Training with PyTorch
- Visualizing the learning process

### 6. Interactive Evaluation & Tuning
- Assessing model performance using confusion matrices
- Interactive threshold adjustment to balance precision and recall
- Visualizing model predictions and confidence levels
- Analyzing the impact of different thresholds on model performance

### 7. Next Steps
- Ways to improve your model
- Further learning resources
- Real-world applications of the techniques learned

## Key Takeaways

- **Data is Essential**: The quality and quantity of your data directly impact model performance
- **Neural Networks Demystified**: Visual understanding of how neural networks learn patterns
- **Supervised Learning**: Learning from labeled examples is the foundation of many ML applications
- **Interactive Evaluation**: Hands-on experience with model tuning and performance analysis
- **End-to-End Project**: Experience the complete ML workflow from data collection to model training

## Contributors

- Workshop created by [Hanan Zaichyk](https://github.com/zaichyk)