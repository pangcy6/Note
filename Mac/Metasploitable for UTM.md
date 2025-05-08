# Metasploitable for UTM

Date: 2023/05/23

----

1. Set up homebrew if you haven't already

2. Install qemu by running this in a terminal:
   
   > brew install qemu

3. Download UTM and install it by putting it in your applications

4. Download Metasploitable from rapid7 and extract the zip somewhere

5. Run this command in a terminal from directory you extracted MS to, It will convert the vmdk disk image to qcow2
   
   > qemu-img convert -p -f vmdk -O qcow2 Metasploitable.vmdk \ Metasploitable.qcow2

6. In UTM create a new VM
   
   1. Choose "Emulate"
   
   2. "Other"
   
   3. "Skip ISO boot"

7. For hardware, leave it as is. Lower the RAM as you want(512M or less)

8. For the rest of the options just next, next... until you get to the "Summary" page

9. Select "open vm settings" then save

10. Chang the name at the top if you want

11. Go to "qemu" in the settings and uncheck "UEFI Boot"

12. Go to "network" in the settings and set "NAT" and 192.168.2.0/24

13. Under "Drives" select "IDE Drive" and delete it

14. Click new drive--> import, select the qcow2 file you created in step 5

15. Click save and start the VM

Enjoy it.

![pic](../image/1VKR984.png)

<mark>END</mark>
