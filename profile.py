"""An example of constructing a profile with a single Xen VM from CloudLab.
Instructions:
Wait for the profile instance to start, and then log in to the VM via the
ssh port specified below.  (Note that in this case, you will need to access
the VM through a high port on the physical host, since we have not requested
a public IP address for the VM itself.)
"""



import geni.portal as portal
import geni.rspec.pg as rspec
import git
import os

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

# Run the bash file to set up Anaconda
node.addService(rspec.Execute(shell="sh", command="sudo chmod 755 /local/repository/setup.sh"))
node.addService(rspec.Execute(shell="sh", command="sudo /local/repository/setup.sh"))

# Run the bash file to set up gdb-peda
node.addService(rspec.Execute(shell="sh", command="sudo chmod 755 /local/repository/gdb.sh"))
node.addService(rspec.Execute(shell="sh", command="sudo /local/repository/gdb.sh"))

#node.addService(rspec.Execute(shell="/bin/sh",
#                             command='git clone https://github.com/longld/peda.git ~/peda'))
#node.addService(rspec.Execute(shell="/bin/sh",
#                              command='echo "source ~/peda/peda.py" >> ~/.gdbinit'))
# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
