"""
Script to automate jira processes and automatically raise issues 
"""

#Import libraries
from jira import JIRA
from generic import load_json

#Define classes
class Jira:
    
    def __init__(self):
        self.data = load_json('jira_config.json')
        self.jira = self.connect()
    
    def connect(self):
        jira = JIRA(self.data['server'],
                    basic_auth=(self.data['username'], self.data['user_key']))
        return jira
    
    def create_issue(self, desc, proj='TRAD', summ='Error on script'):
        self.jira.create_issue(project=proj,
                               summary=summ,
                               description=desc,
                               issuetype={'name': 'Task'})
    
    def check_issue(self, issue):
        issue = self.jira.issue(issue)
        summary = issue.fields
        return summary