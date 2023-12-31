
# Project Title: pyATS Cisco Router Connection and Verification with GNS3 Integration (Beginners Guide)

Welcome to the pyATS Cisco Router Connection and Verification project with GNS3 Integration! This project serves as a comprehensive guide on using pyATS and aetest to connect two Cisco routers, extract information for verification, and seamlessly integrate with GNS3 for network topology emulation. Whether you're a network engineer, Python developer, or automation enthusiast, this project provides valuable insights into leveraging pyATS within a GNS3 environment.

### What is pyATS?

[pyATS](https://pubhub.devnetcloud.com/media/pyats/docs/getting_started/index.html) (Python Automation Test System) is a robust testing framework developed by Cisco. It simplifies network automation and testing, offering features such as test scripting, device connectivity, and result reporting.

## About the Project

Explore the synergy between pyATS and GNS3 as we demonstrate:

* Establishing SSH connections to emulated Cisco routers in GNS3.
* Retrieving information, such as IP addresses and interface status, from GNS3-integrated devices.
* Automating the startup of the GNS3 server and nodes for a streamlined testing experience.
## Getting Started
Follow the steps in the Getting Started section of the README.md file to set up your environment, install dependencies, and execute test scripts.Discover how to create GNS3 topologies and integrate emulated routers for a comprehensive testing environment.




## GNS3 Installation 

### Step 1: Install GNS3

#### 1. Visit the GNS3 Website:

Go to the [official GNS3 website]() and navigate to the "Download" section.

#### 2. Download GNS3:

Download the GNS3 software suitable for your operating system (Windows, macOS, or Linux).

#### 3. Install GNS3:
Follow the installation instructions provided on the GNS3 website for your specific operating system.

### Step 2: Set Up GNS3 Server

#### 1. Install GNS3 Server:
During the GNS3 installation, you'll have the option to install the GNS3 Server. Ensure that you install it, as it is necessary for running GNS3.

#### 2. Start GNS3 Server:
After installation, start the GNS3 Server. You might need to configure settings such as the server IP address and port.

### Step 3: Download Cisco Router Images

#### 1. Cisco Software Licensing:
Ensure you have the necessary licensing to use Cisco IOS images with GNS3. You can obtain these images through Cisco's official channels.

#### 2. Obtain Cisco Router Images:
Cisco IOS images are not freely available. You can use images you obtained legally, such as those from physical Cisco devices you own. Follow Cisco's guidelines for image usage.

#### 3. Import Cisco Router Images into GNS3:
* Open GNS3 and go to "Edit" > "Preferences."

* In the Preferences window, go to "QEMU" and then "QEMU VMs."

* Click "New" to add a new QEMU VM.

* In the "QEMU VM Settings" window, provide a name and select the Cisco router model (e.g., c7200).

* In the "Binary Image" section, select the Cisco IOS image file you obtained.

* Click "Finish" to add the router to GNS3.

### Step 4: Set Up Topologies

#### 1. Create a New Project:
* Open GNS3 and create a new project.
* Drag and drop routers from the "Devices" panel onto the workspace.

#### 2. Connect Devices:
* Use the "Add a link" tool to connect interfaces of routers.
* Configure interfaces with IP addresses, if needed.

#### 3. Start Devices:
* Right-click on each router and select "Start."
* Wait for the routers to boot up.

### Step 5: Verify Connectivity

#### 1. Console to Devices:
* Double-click on a router to open the console.
* Log in using the configured credentials.

#### 2. Verify Connectivity:
* Use basic Cisco commands (e.g., **'show ip interface brief', 'ping'** ) to verify connectivity between routers.


### For a more detailed and comprehensive guide on setting up GNS3 and integrating Cisco routers I recommend checking out This in-depth documentation:
[**Your First Topology**](https://docs.gns3.com/docs/getting-started/your-first-cisco-topology/)

[Video Link](https://www.youtube.com/watch?v=YQcWuWGjppY)


## Pyats Installation    

### Step 1: Install Python

* Ensure that Python is installed on your system. You can download the latest version of Python from the official Python website.
### Step 2: Install Virtualenv (Optional but Recommended)

While Python 3 comes with the built-in venv module for creating virtual environments, you can also install virtualenv, which provides additional features. Install virtualenv using the following command:

```bash

pip install virtualenv

```
### Step 3: Create a Virtual Environment
Using venv (Built-in):

```bash

#Replace 'myenv' with the desired name of your virtual environment
python3 -m venv myenv
```
Using **virtualenv**:

```bash

# Replace 'myenv' with the desired name of your virtual environment
virtualenv myenv
```
### Step 4: Activate the Virtual Environment
On Windows:

```bash

myenv\Scripts\activate
```
On macOS and Linux:

```bash

source myenv/bin/activate
```

### Step 5: Install pyATS

Once the virtual environment is activated, use pip to install pyATS:

```bash

pip install pyats[library]
```
This will install pyATS along with its dependencies.
### Step 6: Verify Installation

You can verify the installation by running:

```bash

pyats version
```
This should display the installed version of pyATS.
### Step 7: Deactivate the Virtual Environment

When you're done working in the virtual environment, you can deactivate it:

```bash

deactivate
```
**Additional Notes:**

Make sure to activate your virtual environment whenever you want to work on your project using pyATS.

if you're planning to use additional pyATS libraries, you can install them in the same virtual environment by running pip install **<library-name>** after activating the environment.

Always create a virtual environment for each project to avoid conflicts between project dependencies.

By following these steps, you'll have a virtual environment set up with pyATS installed, allowing you to work on your project in an isolated and controlled environment.

[For Detailed Installation](https://pubhub.devnetcloud.com/media/pyats/docs/getting_started/index.html)

## Installation of this Project

### Step 1: Set Up a Virtual Environment

```bash

# Create a new directory for your project
mkdir my_pyats_project

# Navigate to the project directory
cd my_pyats_project

# Create a virtual environment
python -m venv <desired-name>

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On Unix or MacOS
source bin/activate .
```
### Step 2: Fork this Project on GitHub

* Visit this project's GitHub repository.
* Click on the "Fork" button in the upper right corner to create a copy of the repository in your GitHub account.

### Step 3: Clone Your Forked Repository

```bash

# Clone your forked repository
git clone https://github.com/your-username/your-pyats-project.git

# Navigate to the project directory
cd your-pyats-project
```
### Step 4: Update Testbed and Python Script

Modify the testbed.yaml file in the tests directory to match your network setup.

```yaml

    devices:
      iosxe_1:
        alias: R1
        type: iosxe
        connections:
          a:
            protocol: telnet
            ip: your_device_ip
            port: your_device_port
            credentials:
              username: your_username
              password: your_password
```
Update your Python test script accordingly.

### Step 5: Install Dependencies

```bash

# Install project dependencies
pip install -r requirements.txt
```

### Step 6: Commit Changes and Push to Your Fork

```bash

# Add and commit your changes
git add .
git commit -m "Update testbed and script for my setup"

# Push the changes to your forked repository
git push origin main
```

### Step 7: Endpoint API Integration with GNS3

* In GNS3, set up an HTTP/REST endpoint in the GNS3 Server settings.
    
* Disable password protection for the GNS3 server by navigating to "Edit" > "Preferences" > "Server" and unchecking the "Protect server with password" option.
* Modify your Python script to interact with the GNS3 API for router start/stop actions.

For more Information, [Read](https://gns3-server.readthedocs.io/en/stable/)

### Step 8: Test Your Project

```bash

# Run your PyATS test script
pyats run job your_test_script.py
```
### Step 9: Deactivate Virtual Environment

```bash

# Deactivate the virtual environment
deactivate
```

**Notes:**

* Replace placeholders (like your_device_ip, your_device_port, your_username, etc.) with your actual values.
* The specifics of GNS3 API integration depend on your GNS3 setup. Refer to the GNS3 API documentation for details.


## Router Installation

The project includes router and topology files that are ready to use. Feel free to leverage them at your discretion based on your specific network setup. The router configurations are available in the `routers` directory, and the topology file is located in the `topology` directory.
## Feedback

If you have any feedback, please reach out to me at sudhirhegde242@gmail.com

