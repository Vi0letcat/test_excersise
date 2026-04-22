import json
import subprocess


class Requests:

    def __init__(self):
        self.base_url = "https://localhost/api/v3.11/"
        self.key_request_address = r"C:\Program Files\TrueConf Server\tc_regkey.exe"
        self.request_users = "users"
        self.request_conferences = "conferences"
        self.api_key = self.get_api_key()
        
    def get_api_key(self):
        command =  [self.key_request_address,"get","Configuration","Status Security",]
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error executing curl: {result.stderr}")
                return None
            else:
                return(result.stdout).strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing curl: {e}")
            print(f"Error output: {e.stderr}")
            return None
        
    def api_request(self, method, request_method, headers=None, data=None):
        url = f"{self.base_url}{request_method}?access_token={self.api_key}"
        command = ["curl", "--insecure", "-X", method, url]
        if headers:
            for key, value in headers.items():
                command.extend(["-H", f"{key}: {value}"])
        if data:
            command.extend(["-d", json.dumps(data)])
        
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error executing curl: {result.stderr}")
                return result.stderr
            else:
                return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing curl: {e}")
            print(f"Error output: {e.stderr}")
            return None
        
    def create_user(self, name: str, password: str, email: str):
        url = f"{self.base_url}{self.request_users}?access_token={self.api_key}"
        request_body = {
            "password": password,
            "email": email,
            "login_name": name
        }
        response = json.loads(self.api_request("POST", request_method=self.request_users, data=request_body))
        return response

    def create_conference(self, conf_data: dict):
        url = f"{self.base_url}{self.request_conferences}?access_token={self.api_key}"
        response = json.loads(self.api_request("POST", request_method=self.request_conferences, data=conf_data))
        return response