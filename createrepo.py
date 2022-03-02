from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time
import sys

# get argument as Repository name
strRepoName = sys.argv[1]

conf = yaml.safe_load(open('lgnDetails.yaml'))
strMail = conf['gh_user']['email']
strPwd = conf['gh_user']['password']
strUrlLogin = "https://www.github.com/login"
strUrlNew = "https://www.github.com/new"

driver = webdriver.Chrome()

# Login function
def login(url,usernameId, username, passwordId, password, submit_buttonName):
    driver.get(url)
    driver.find_element(By.ID, usernameId).send_keys(username)
    driver.find_element(By.ID, passwordId).send_keys(password)
    driver.find_element(By.NAME, submit_buttonName).click()

# Create repository function
def createRepo(url, repoId, repoName, submit_buttonName):
    driver.get(url)
    driver.find_element(By.ID, repoId).send_keys(repoName)
    # After filling new repo name script wait for GitHub to check if repo doesn't exist
    time.sleep(3)
    # Create repository button have no Name or ID, class name used
    driver.find_element(By.CLASS_NAME, submit_buttonName).click()
    

login(strUrlLogin, "login_field", strMail, "password", strPwd, "commit")
# After login wait for page load
time.sleep(5)

createRepo(strUrlNew, "repository_name", strRepoName, "btn-primary")
# After creating repo, wait before exit browser
time.sleep(5)

# Close browser session
driver.quit()

quit()

