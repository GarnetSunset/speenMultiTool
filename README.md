# speenMultiTool
Multiple Uses for Vinny's "Speen"

## Knowledgebase
Scheduled Tasks should be used to run the grandfather clock mechanism. Very easy to make work. I'll probably build a linux version with cron later. Windows for now. 

``C:\ProgramData\Microsoft\Windows\Start Menu\Programs`` is the only location where a shortcut with 
key combo privileges can exist and register those combos. Putting a shortcut in there but hidden would be very useful, means I'll have to include a check for Admin prior to that copy being done, as programdata is a protected dir. (I can probably escalate too).

## Scratch

Hardcode the name of that .lnk. That way we can delete it if the user hates it. 

When building the lnk make sure to ask the user for a set of keys to trigger them. 

Make a UI, these are degenerates just like me. 

https://www.blog.pythonlibrary.org/2010/01/23/using-python-to-create-shortcuts/
