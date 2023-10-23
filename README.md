# Simple-Domain-Monitor
Practice project for detecting homographs domain names using python and Levinstein distance

# Requirements
Top 10000 domains from https://github.com/zer0h/top-1000000-domains

# Purpose
This project demonstrates base knowledge of python scripts in a security focused environment. The code could be used on an email server to detect potentially malicous emails by detecting domains that are similar to the most popular domains. The input file can be replaced with domains that are most frequently interacted with by the user base. Note: Using the top 10000 domains as a 'trusted' list will trigger many detections due to the nature of Levenstien distance. 

