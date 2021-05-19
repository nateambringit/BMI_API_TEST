# BMI (Body-Mass Index) Restful API Calculation

BMI API Calculation build based on Flask.

How to use the service :
```
1. Click the link : https://bmi-test-hf.herokuapp.com/?height=0&weight=0
2. Set the height and weight
3. Enjoy!
```

How to run in your environment :
```
1. Requirement python 3.x (will be good if you use python 3.6) 
2. pip install requirement.txt
3. python3 app.py
```

Example:

``` 
https://bmi-test-hf.herokuapp.com/?height=170&weight=70

Result : 
{"message": "success", "bmi": 24.22, "label": "normal", "statusCode": 200}
```

I deployed the apps service in Heroku using Github Actions for CI/CD, you can check in Github Actions in this project and you can check SAST (Static Application Security Testing) and DAST (Dynamic Application Security Testing) Report in Artifacts Build Github Actions. 

## You can check configuration deploy on : .github/workflows/appsecure.yml.


```
Security Vulnerability Check :
- sast-scan (SAST) : https://github.com/AppThreat/sast-scan (bandit, gitleaks, depscan) 
- OWASP ZAP (DAST) : https://github.com/marketplace/actions/owasp-zap-full-scan
```   

To answer about question "explanation of what you are implementing to secure the application and/ or server" :

- Implementation SSDLC (Secure Software Development Lifecycle) for Development
- Implementation Firewall for Adding Secure Layer Apps and Networks
- Validation and Configuration must be compliance for example unused port in server must be closed and for application must be explicit validation to preventing injection point
- Use management store credentials
- Educate specific people who manage apps and network like security awareness, secure configuration/code, and etc for reduce human error. 
