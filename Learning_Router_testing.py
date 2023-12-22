'''
Learning_Router_testing.py

'''

import logging

from pyats import aetest
import re
import subprocess
import time

# create a logger for this module
logger = logging.getLogger(__name__)

#Important variables
# Replace with the Project ID you are using.
project_id = "88d34736-b2a6-4086-b400-43556d9f74f3"
# Replace with the node IDs you want to start
node_ids = ["128dd764-bd3a-4909-9082-48fe5e919760", "2ae77fb4-e860-4747-b20c-8867fc5179cb"]
# Change according to your needs
interface_name_to_find = "FastEthernet0/0"
expected_ip = '10.1.1.2'
expected_protocol = 'up'
expected_status = 'up'

#-----------------------------Run Commands on Terminal------------------------------------#
def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error (return code {result.returncode}): {result.stderr}"
    except Exception as e:
        return f"Exception: {str(e)}"
#---------------------------------------END----------------------------------------------#

#-----------------------Regex for validating ip status and protocol----------------------#
def find_ip_status(interface_name, output):
        # Define the regular expression pattern
        pattern = re.compile(rf"{interface_name}\s+([\d.]+)\s+\S+\s+\S+\s+(\w+)\s+(\w+)")

        # Search for the pattern in the input string
        match = pattern.search(output)

        # If a match is found, extract IP address and status
        if match:
            ip_address = match.group(1)
            status = match.group(2)
            protocol = match.group(3)
            print(ip_address,status,protocol)
            return ip_address, status, protocol
        else:
            return None

def Validation(router):
    # Perform main logic here
    print(f"Connected to {router.name}")
    output= router.execute("sh ip int brief")
        
    ipaddress, status, protocol= find_ip_status(interface_name_to_find, output)
    if ipaddress == expected_ip and status == expected_status and protocol == expected_protocol:
        print("The router information is validated")
        return True
    else:
        print("Router information doesn't match:")
        print(f"Expected IP: {expected_ip}, Actual IP: {ipaddress}")
        print(f"Expected Status: {expected_status}, Actual Status: {status}")
        print(f"Expected Protocol: {expected_protocol}, Actual Protocol: {protocol}")
        return False
#-----------------------------------------END-------------------------------------------#
class GNS3_Server_Setup(aetest.CommonSetup):

    @aetest.subsection
    def Connect_To_GNS3_Server(self, testbed):
        try:
        # Start GNS3 server in the background
            self.parent.parameters['gns3_server_process'] = subprocess.Popen(['gns3server', '--local'])
            time.sleep(10)
            # gns3_server_process = subprocess.Popen(['gns3server', '--local'])
            # return gns3_server_process
        except Exception as e:
            print(f"Error starting GNS3 server: {e}")
            return None
    

    
    @aetest.subsection
    def Loading_Project(self):
        print(f"Loading GNS3 project with ID: {project_id}")
        command = "curl -i -X POST 'http://localhost:3080/v2/projects/load' -H 'Content-Type: application/json' -d '{\"path\": \"/home/sudhir-hegde/GNS3/projects/First Topology/First Topology.gns3\"}'"
        response = run_command(command)
        print(response)
    
    @aetest.subsection
    def start_nodes(self):

        for node_id in node_ids:
            print(f"Starting node with ID: {node_id}")
            command = f'curl -X POST "http://localhost:3080/v2/projects/{project_id}/nodes/{node_id}/start" -d "{{}}"'
            response = run_command(command)
            print(response)

class Router_Testing(aetest.Testcase):
    '''testcase_one

    < docstring description of this testcase >

    '''

    @aetest.setup
    def setup_testbed(self, testbed):
    # Connect to devices in the testbed

        for device_name, device in testbed.devices.items():
            print(f"Connecting to {device_name}")
            device.connect()
    
    @aetest.test
    def testRouter1(self,testbed):
        router1 =testbed.devices['R1']
        try:
            if Validation(router1):
                self.passed()
            else:
                self.failed()
        
        except Exception as e:
            self.failed(f"Error: {e}")

    @aetest.test
    def testRouter2(self,testbed):
        router2 =testbed.devices['R2']
        try:
            if Validation(router2):
                self.passed()
            else:
                self.failed()
        
        except Exception as e:
            self.failed(f"Error: {e}")

    @aetest.cleanup
    def cleanup_testbed(self, testbed):
        # Disconnect from devices in the testbed
        for device_name, device in testbed.devices.items():
            print(f"Disconnecting from {device_name}")
            device.disconnect()
    


class CommonCleanup(aetest.CommonCleanup):
    '''CommonCleanup Section

    < common cleanup docstring >

    '''
    @aetest.subsection
    def stop_nodes(self):
        for node_id in node_ids:
            print(f"Stopping node with ID: {node_id}")
            command = f'curl -X POST "http://localhost:3080/v2/projects/{project_id}/nodes/{node_id}/stop" -d "{{}}"'
            response = run_command(command)
            print(response)
        
          
      
    @aetest.subsection
    def stop_gns3_server(self):
        try:
            process = self.parent.parameters['gns3_server_process']
            # Send a termination signal to the GNS3 server process
            process.terminate()
            # Wait for the process to finish
            process.wait()
            print("GNS3 server stopped successfully.")
        except Exception as e:
            print(f"Error stopping GNS3 server: {e}")


if __name__ == '__main__':
    # for stand-alone execution
    import argparse
    from pyats import topology


#You would execute your tests by running main_script.py from the command line, 
# and the --testbed argument would specify the path to your testbed YAML file. 
   
# cmd : python Learning_Router_testing.py --testbed testbeds/testbed.yaml

    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--testbed', dest = 'testbed',
                        help = 'testbed YAML file',
                        type = topology.loader.load,
                        default = None)

    # do the parsing
    args = parser.parse_known_args()[0]

    aetest.main(testbed = args.testbed)