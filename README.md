# Plugin-Upload-Script
Python Script that runs 24/7 in the background on your PC, uploading built plugins to your Minecraft server, and reloading the plugin.
## How to use
**Prerequisites/ Requirements**
> [Plugman](https://dev.bukkit.org/projects/plugman) or [PlugmanX](https://www.spigotmc.org/resources/plugmanx.88135/)
> 
> [Screen running on your Linux Machine, more specifially for your MineCraft server](https://oscarhjelm.com/blag/2011/02/minecraft-server-on-linux-using-screen/)
> 
> [Python on your PC](https://www.python.org/downloads/)
> 
> Plugins building to one folder

**Setting up the Script**

Copy the [script.pyw](https://github.com/Siiant/Plugin-Upload-Script/blob/main/script.pyw) and paste it into your preferred text editor. Once you open the file, follow the directions below.

1. Change `path = "PLUGIN_BUILD_LOCATION"` to match your plugin build location.
   - It should go from `path = "PLUGIN_BUILD_LOCATION"` to something like `path = "C:\\PBuilds\\"`
   - Python will require two backslashes to act as one, so we must use `"C:\\PBuilds\\"` instead of `"C:\PBuilds\"`
2. Change ` client.connect('IP', username = 'SFTP_USERNAME', password = 'SFTP_PASSWORD')` to your SFTP IP, Username, and Password.
   - It should look something like `client.connect('192.168.1.1', username = 'admin', password = 'password')`
   - If your password contains unique characters, be sure to use the [Escape Characters](https://pythonexamples.org/python-escape-characters/) instead.
3. Change `sftp_client.put(file, 'SERVER_PLUGINS' + file_name)` to match your server plugin folder.
   - It should look similar to `sftp_client.put(file, '/home/admin/server/plugins/' + file_name)`
4. Replace `SCREEN_NAME` in both `...client.exec_command("screen -S SCREEN_NAME -p 0 -X stuff ...` with your Minecraft server screen name.
   - It should look like `...client.exec_command("screen -S minecraft -p 0 -X stuff ... `
5. Put the finished Script inside of `C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` on your PC. This will run it on PC startup.
6. (Optional) Add a shortcut to the desktop for the script.

**Usage** 

Assuming the Script is running, just build your plugin like normal inside your IDE, and wait about 5 seconds! You should see a broadcast message saying the plugin was reloaded.
