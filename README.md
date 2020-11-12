# ScammerlistePythonDiscordbot

This is a Discord Bot that searches a Database for existing entrys by using the UUID of a Player from the Mojang API.
Parsing the Result of the Request into the SQL Query. Because the request only returns UUIDs its impossible to SQL Inject attack.

After the Request the UUID is parsed into the SQL QUery which searches the Database for a match by UUID. If a match is found the result is put into a
list for later ease of use. 

## Known Problems
If there are multiple UUID entry with different Usernames the List Approach could mess things really up. Working on a Array list
