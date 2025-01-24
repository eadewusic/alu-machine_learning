# Binary Image Classifier  
This project implements a binary image classifier from scratch using Python and NumPy. It involves developing a neural network capable of classifying images into two categories based on a dataset. The project is designed to deepen understanding of key machine learning concepts such as logistic regression, forward propagation, backpropagation, and gradient descent.

## Features  
- Logistic Regression from scratch.  
- Implementation of key neural network components:  
  - Forward Propagation  
  - Backpropagation  
  - Cost and Loss Functions  
  - Gradient Descent  
- Data preprocessing and one-hot encoding.  
- Vectorized implementations for performance optimization.  
- Model evaluation on train, validation, and test datasets.  
- Visualization of results and predictions.  

## Requirements  
- Python 3.5+  
- NumPy (version 1.15)  
- Matplotlib (for visualization)  

## Installation  
1. Clone this repository.  
   ```bash
   git clone https://github.com/eadewusic/alu-machine_learning.git
   cd supervised_learning
   ```  
2. Ensure Python 3.5+ and NumPy are installed.  

## Dataset  
Place the following datasets in a `data` directory in the project root:  
- `Binary_Train.npz`  
- `Binary_Dev.npz`  
- `MNIST.npz`  

The dataset includes:  
- Binary data for training and development.  
- Multi-class MNIST data for additional exploration.  

## How to Use  
1. View Sample Data:  
   Visualize dataset images using the provided scripts:  
   ```bash
   ./show_data.py  
   ./show_multi_data.py  
   ```  

2. Train the Model:  
   Implement and train the binary image classifier. Ensure all required files are in the appropriate directories.  

3. Test the Model:  
   Evaluate the model's performance on validation and test datasets.  

4. Save and Load Models:  
   Use Python's `pickle` module to save and reload the trained model.  

## Example Output  
Visualizations for the training process, including:  
- Loss curves.  
- Accuracy plots.  
- Sample predictions and corresponding labels.  
