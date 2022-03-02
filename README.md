# RemoteRepositoryCreate-github
Create repository on GitHub via Windows command line (automatic logon with repo creation)

## EXAMPLE:
>
> python createrepo.py REPO_NAME
>

Where REPO_NAME is name of newly created repository

## REQUIREMENTS
- selenium
- yaml
- chromedriver.exe <https://chromedriver.chromium.org/downloads>

## lgnDetails.yaml
Do not forget to put your email/password instead of DUMMY values

gh_user:
  email: GITHUB_LOGIN_EMAIL_ADDRESS
  password: GITHUB_LOGIN_PASSWORD
