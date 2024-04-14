import vk_api
#from config import token, user_id


import os
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
 

# with open('.env', 'r') as f:
#     token = f.readline()

session = vk_api.VkApi(token = os.getenv("TOKEN"))

vk = session.get_api()

def get_user_name(user_id):
    with open('resume.txt', 'w') as f:
        account = session.method("account.getProfileInfo", {"user_id": user_id})
        name = "Имя: " + account['first_name']
        f.write(name + '\n')
        surname = "Фамилия: " + account['last_name']
        f.write(surname + '\n')
        bday = "Дата рождения: " + account['bdate']
        f.write(bday + '\n')
        stat = "Статус профиля в VK: " + account['status']
        f.write(stat + '\n')
        hometown = "Родной город: " + account['home_town']
        f.write(hometown + '\n')
        per_name = "Имя пользователя: " + account['screen_name']
        f.write(per_name + '\n')
        gender = "Пол: "
        if (account['sex'] == 1):
            gender += "женский"
            f.write(gender + '\n')
        elif(account['sex'] == 2):
            gender += "мужской"
            f.write(gender + '\n')
        else:
            gender += "не указан"
            f.write(gender + '\n')

        
if __name__ == "__main__":
    get_user_name(os.getenv("USER_ID"))