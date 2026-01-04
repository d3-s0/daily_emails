# Project: Daily emails

I want to create my own daily email newsletter.

Tasks:
- [ ] Sending email python script
- [ ] Create an executable bash script to run python script
- [ ] Edit the crontab file to run the script automatically
- [ ] Make the email inputs using argparse
- [ ] Write a script to parse any url and get the links from the URL
- [ ] Connect up random url to email script in body of email
- [ ] Move code to Raspberry pi to send the email so not reliant on laptop being on
- [ ] Add random quote from kindle clips file

## Bash script
```bash
#!/bin/bash

# Change to the directory containing the Python script
cd /path/to/directory

# Run the Python script
python3 send_email.py --from-address [INSERT] --password [INSERT] --to-address [INSERT] --clips path/to/clipps.t t
```

## csv file format
urls,

## Crontab
Crontab allows us to schedule tasks on the machine. I'm currently using the raspberry pi to run this everyday.

Run:
e port EDITOR=nano
crontab -e

Write:
min hour * * * /path/to/bash
