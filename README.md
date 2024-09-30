
**Author:** Muhammad Erico Ricardo

Deployment hugging face link : https://huggingface.co/spaces/EricoR/Image_transportation_classification

**Overview**

This repository presents a machine learning model designed to optimize delivery routes by classifying vehicle images. By integrating this model into a route optimization system, we can significantly enhance the efficiency of delivery operations.

**Problem Statement**
E-commerce companies face the challenge of delivering products to numerous customers efficiently and cost-effectively. Inefficient delivery routes can lead to increased delivery times, higher fuel costs, and decreased customer satisfaction.

**Solution**
Our proposed solution involves using image classification to identify the type of delivery vehicle. This information is then fed into a route optimization algorithm to determine the most efficient route.

**Key Features**

* **Vehicle Image Classification:** The model accurately classifies images of various vehicles (e.g., vans, trucks, motorcycles).
* **Route Optimization:** The classified data is integrated into a route optimization system to determine the optimal delivery route.
* **Dynamic Route Adjustment:** The system can dynamically adjust routes based on real-time traffic conditions and other factors.
* **Accurate Delivery Time Estimation:** The model provides more accurate delivery time estimates to customers.

**Benefits**

* **Faster Deliveries:** Optimized routes lead to quicker delivery times, improving customer satisfaction.
* **Reduced Fuel Costs:** Efficient routes minimize fuel consumption and operational costs.
* **Improved Resource Allocation:** Better understanding of vehicle types enables optimal resource allocation.
* **Data-Driven Decision Making:** The model provides valuable data for analyzing delivery performance and identifying areas for improvement.

**Technical Details**

* **Dataset:** Data set used 800 picture of every type of vehicle
* **Model Architecture:** Used CNN model like cov2d model, dense, etc.
* **Training Process:** Use 80% of data from every type of vihecle for training and rest is for testing
* **Evaluation Metrics:** We used accuracy for metrics because it was multiclass classification

**Future Work**

* **Real-time Implementation:** Integrate the model into a real-time delivery management system.
* **Multimodal Data:** Explore the use of additional data sources (e.g., GPS data, weather data) to improve accuracy.
* **Advanced Optimization Algorithms:** Investigate more sophisticated optimization algorithms for complex delivery scenarios.
