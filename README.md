<!-- ABOUT THE PROJECT -->
## About The Project
* This project solves a sub-problem related to another mission planning project for drones and UAVs. You can find another sub-problem of the mission planning project in this [article](https://medium.com/codex/optimal-region-partitioning-for-uavs-and-drones-in-cooperative-flight-settings-c0764a6450f9).
* **Note:** Please refer to [**extract-article.pdf**](https://github.com/mdiamantino/cyclic-flight-plan-travelling-salesman-problem/blob/main/extract-article.pdf) to learn more on the construction of the algorithm.



![fligh plan1](https://miro.medium.com/max/2400/1*FJyEIAsCm_HaTZXxUWfVzQ.png)
![fligh plan2](https://github.com/mdiamantino/cyclic-flight-plan-travelling-salesman-problem/blob/main/example.png)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Install tkinter
```sh
sudo apt-get install python3-tk
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mdiamantino/cyclic-flight-plan-travelling-salesman-problem.git
   ```
2. Enter the cloned directory and create a virtual environment
   ```sh
   cd cyclic-flight-plan-travelling-salesman-problem/
   ```
   ```sh
   python3 -m venv venv
   ```
3. Activate the virtual environment
   ```sh
   . venv/bin/activate
   ```
4. **Install requirements**
   ```sh
   pip3 install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage
* Run *demo.py* to find the cyclic path of maximal coverage inside the polygon [(0, 0), (6, 10), (6, 20), (10, 10), (10, 20), (14, 10), (14, 20), (20, 10), (14, 0), (14, 6)] 
   ```sh
   python3 demo.py
   ```
* Or, use your own polygon's coordinates and *vision radius* : a value representing the field of vision of the drone (refer to the brief article). This value should be a multiple of 0.5 AND where 0.5 is the minimum value):
   ```sh
   python3 main.py
   ```

* Or, use the project as module:
  
  1. (if you are using the command-line interface)
   ```sh
   python3
   ```
  2. 
   ```sh
   >>> from flight_plan_generator import get_best_route
   ```
  3. get_best_route(YOUR COORDINATES HERE, YOUR vision_radious HERE, \[debug=True|False\]) 
  Example:
   ```sh
   >>> get_best_route([(5, 0), (2, 2), (0, 6), (6, 6), (6, 14), (12, 12), (16, 8), (20, 15), (20, 5), (16, 0)], 0.5, debug=True)
   ```


<!-- CONTACT -->
## Contact

Mark Diamantino Caribé - Mark.Diamantinocaribe@student.kulevuen.be - [LinkedIn](https://be.linkedin.com/in/markdiamantinocaribe)

Project Link: [https://github.com/mdiamantino/cyclic-flight-plan-travelling-salesman-problem](https://github.com/mdiamantino/cyclic-flight-plan-travelling-salesman-problem)
